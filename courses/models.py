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

