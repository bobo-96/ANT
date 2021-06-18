from django.db.models import F
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status

from courses.models import Course, Category, Subcategory, Comments, CourseAccess
from courses.serializers import CategorySerializer, SubCategorySerializer, SubCategoryWithCoursesSerializer, \
    CourseSerializer, CommentSerializer


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class SubCategoryWithCoursesView(ModelViewSet):
    serializer_class = SubCategoryWithCoursesSerializer
    queryset = Subcategory.objects.prefetch_related('course_subcategory').all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class SubCategoryView(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = Subcategory.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CourseView(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().annotate(
        owner_nick_name=F('owner__username'),
        owner_avatar=F('owner__avatar'),
    ).order_by('-date')
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_object(self):
        obj = Course.objects.all().annotate(
            owner_nick_name=F('owner__username'),
            owner_avatar=F('owner__avatar')
        ).get(id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        user = request.user
        course = request.data.get('course')
        if CourseAccess.objects.filter(owner=user, course_id=course):
            return super().create(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        user = request.user
        comment = self.get_object()
        if comment.owner == user:
            return super().update(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        comment = self.get_object()
        if comment.owner == user:
            self.perform_destroy(comment)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)







