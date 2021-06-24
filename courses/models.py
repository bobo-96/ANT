from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField('Категория', max_length=255)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField('Подкатегории', max_length=255)
    category = models.ForeignKey('courses.Category', models.CASCADE, 'category_subcategory')

    def __str__(self):
        return self.name


class Comments(models.Model):
    comment = models.TextField(null=True)
    course = models.ForeignKey('courses.Course', models.CASCADE, 'post_comments')
    owner = models.ForeignKey('user.User', models.CASCADE, 'user_comments')
    created_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text


class Course(models.Model):
    owner = models.ForeignKey('user.User', models.CASCADE, 'course_owner')
    category = models.ForeignKey('courses.Category', models.CASCADE, 'course_category')
    subcategory = models.ForeignKey('courses.Subcategory', models.CASCADE, 'course_subcategory', null=True)
    name = models.CharField('Название курса', max_length=255)
    description = models.TextField('Описание курса')
    lessons_count = models.IntegerField('Количество уроков', null=True)
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2, null=True)
    course_preview_image = models.ImageField('Изображение курса', upload_to='course_preview_image', null=True)
    course_preview_video = models.FileField('Вступительное видео курса', upload_to='course_preview_video', null=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class CourseAccess(models.Model):
    owner = models.ForeignKey('user.User', models.CASCADE, 'user_course_access')
    course = models.ForeignKey('courses.Course', models.CASCADE, 'course_access')


class Chapter(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'chapter_owner')
    course = models.ForeignKey('courses.Course', models.CASCADE, 'course_chapter')
    name = models.CharField('Название главы', max_length=255)
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):
    owner = models.ForeignKey('user.User', models.CASCADE, 'lesson_owner')
    course = course = models.ForeignKey('courses.Course', models.CASCADE, 'course_lesson')
    name = models.CharField('Название урока', max_length=255)
    lesson_video_material = models.FileField('Видео материалы', upload_to='lesson_video_material', null=True)
    description = models.TextField('Описание урока', null=True)
    lesson_materials = models.FileField('Материалы по уроку', upload_to='lesson_materials', null=True)

    def __str__(self):
        return f'{self.name} {self.description}'


class Homework(models.Model):
    owner = models.ForeignKey('user.User', models.CASCADE, 'homework_owner')
    lesson = models.ForeignKey('courses.Lesson', models.CASCADE, 'lesson_homework')
    name = models.CharField('Название домашнего задания', max_length=255)
    description = models.TextField('Описание домашнего задания')
    homework_materials = models.FileField('Материалы по домашнему заданию', upload_to='homework_materials', null=True)


class StudentsHomeworks(models.Model):
    owner = models.ForeignKey('user.User', models.CASCADE, 'student_homework_owner')
    homework = models.ForeignKey('courses.Homework', models.CASCADE, 'student_homework')
    url = models.URLField(max_length=200)