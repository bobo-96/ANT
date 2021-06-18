from rest_framework import serializers

from courses.models import Category, Chapter, Course, Subcategory, Comments
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'avatar',)


class CourseForCategories(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('name', 'owner', 'course_preview_image', 'lessons_count', 'price')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryWithCoursesSerializer(serializers.ModelSerializer):
    course_subcategory = CourseForCategories(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ('name', 'course_subcategory')


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('name',)


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'


    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comments.objects.create(owner=user, **validated_data)
        return comment


    def update(self, instance, validated_data):
        data = validated_data.copy()
        data.pop('course', None)
        for attr, value, in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CourseSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True, many=False)
    post_comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('name', 'lessons_count', 'owner', 'description', 'post_comments')


















# class CourseSerializer(serializers.ModelSerializer):
#
#     owner = UserSerializer(read_only=True, many=False)
#     category = CategorySerializer(read_only=True, many=False)
#     # chapter = ChapterSerializer(many=True)
#
#     class Meta:
#         model = Course
#         fields = ('category', 'owner', 'name', 'description', 'course_preview_image', 'course_preview_video', 'date')

    # def create(self, validated_data):
    #     user = self.context.get('request').user
    #     course = Course.objects.create(owner=user, **validated_data)
    #     chapters = self.context.get('request').data.getlist('Chapter.name')
    #     chapter_list = [Chapter(name=item, course=course) for item in chapters]
    #     Chapter.objects.bulk_create(chapter_list)
    #     return course
    #
    # def update(self, instance, validated_data):
    #     for attr, value, in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     chapters = self.context.get('request').data.getlist('Chapter.name')
    #     if chapters:
    #         Chapter.objects.filter(course=instance).delete()
    #         chapter_list = [Chapter(name=item, course=instance) for item in chapters]
    #         Chapter.objects.bulk_create(chapter_list)
    #     return instance






