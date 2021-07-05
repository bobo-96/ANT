from django.db.models import F
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status

from courses.models import Course, Category, Subcategory, Comments, CourseAccess, Lesson, Homework, StudentsHomeworks
from courses.permissions import IsCourseOwnerOrReadOnly, IsLessonOwnerOrReadOnly, IsHomeworOwnerOrReadOnly
from courses.serializers import CategorySerializer, SubCategorySerializer, SubCategoryWithCoursesSerializer, \
    CourseSerializer, CommentSerializer, CategoryWithSubcategory, LessonSerializer, HomeworkSerializer, \
    StudentsHomeworksSerializer, CourseAccessSerializer


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CategoryWithSubcategoryView(ModelViewSet):
    serializer_class = CategoryWithSubcategory
    queryset = Category.objects.prefetch_related('category_subcategory').all()
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


class CourseAccessView(ModelViewSet):
    serializer_class = CourseAccessSerializer
    queryset = CourseAccess.objects.all()
    lookup_field = 'pk'





class CourseView(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().annotate(
        owner_nick_name=F('owner__username'),
        owner_avatar=F('owner__avatar'),
    ).order_by('-date')
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = (IsCourseOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)


    def get_object(self):
        obj = Course.objects.all().annotate(
            owner_nick_name=F('owner__username'),
            owner_avatar=F('owner__avatar')
        ).get(id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        user = request.user
        course = self.get_object()
        if course.owner == user:
            return super().update(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        course = self.get_object()
        if course.owner == user:
            self.perform_destroy(course)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)


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


class LessonView(ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsLessonOwnerOrReadOnly,)

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        lesson = self.get_object()
        if CourseAccess.objects.filter(owner=user, course_id=lesson.id):
            return super().retrieve(request, *args, **kwargs)
        return Response('нет доступа',status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        user = request.user
        lesson = self.get_object()
        if CourseAccess.objects.filter(owner=user, course_id=lesson.id):
            return super().retrieve(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)


    def create(self, request, *args, **kwargs):
        user = request.user
        course = request.data.get('course')
        if Course.objects.filter(owner=user, id=course):
            return super().create(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        user = request.user
        lesson = self.get_object()
        if lesson.owner == user:
            return super().update(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        lesson = self.get_object()
        if lesson.owner == user:
            self.perform_destroy(lesson)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)


class HomeworkView(ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsHomeworOwnerOrReadOnly,)

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        homework = self.get_object()
        if CourseAccess.objects.filter(owner=user, course_id=homework.id):
            return super().retrieve(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        user = request.user
        homework = self.get_object()
        if CourseAccess.objects.filter(owner=user, course_id=homework.id):
            return super().retrieve(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        user = request.user
        lesson = request.data.get('lesson')
        if Lesson.objects.filter(owner=user, id=lesson):
            return super().create(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        user = request.user
        homework = self.get_object()
        if homework.owner == user:
            return super().update(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        homework = self.get_object()
        if homework.owner == user:
            self.perform_destroy(homework)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)


class StudentsHomeworksView(ModelViewSet):
    serializer_class = StudentsHomeworksSerializer
    queryset = StudentsHomeworks.objects.all()
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        user = request.user
        course = request.data.get('course')
        if CourseAccess.objects.filter(owner=user, course_id=course):
            return super().create(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        user = request.user
        studentshomeworks = self.get_object()
        if studentshomeworks.owner == user:
            return super().update(request, *args, **kwargs)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        studentshomeworks = self.get_object()
        if studentshomeworks.owner == user:
            self.perform_destroy(studentshomeworks)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)
