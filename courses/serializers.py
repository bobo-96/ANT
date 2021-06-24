from rest_framework import serializers

from courses.models import Category, Chapter, Course, Subcategory, Comments, Lesson, Homework, StudentsHomeworks
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'avatar', 'id')


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
        fields = ('id', 'name', 'course_subcategory')


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('name',)


class CategoryWithSubcategory(serializers.ModelSerializer):
    category_subcategory = SubCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'category_subcategory')


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
        fields = (
            'name', 'lessons_count', 'owner', 'description',
            'post_comments', 'date', 'price', 'course_preview_image',
            'course_preview_video', 'category', 'id',
        )

    def create(self, validated_data):
        user = self.context.get('request').user
        course = Course.objects.create(owner=user, **validated_data)
        return course


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'lesson_video_material', 'description', 'lesson_materials', 'course')

    def create(self, validated_data):
        user = self.context.get('request').user
        lesson = Lesson.objects.create(owner=user, **validated_data)
        return lesson


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('id', 'name', 'description', 'homework_materials', 'lesson')

    def create(self, validated_data):
        user = self.context.get('request').user
        lesson = Homework.objects.create(owner=user, **validated_data)
        return lesson


class StudentsHomeworksSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentsHomeworks
        fields = ('id', 'url')

    def create(self, validated_data):
        user = self.context.get('request').user
        lesson = StudentsHomeworks.objects.create(owner=user, **validated_data)
        return lesson
















