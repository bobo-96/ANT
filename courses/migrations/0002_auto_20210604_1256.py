# Generated by Django 3.2.4 on 2021-06-04 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название главы')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_preview_image',
            field=models.ImageField(null=True, upload_to='course_preview_image', verbose_name='Изображение курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_preview_video',
            field=models.FileField(null=True, upload_to='course_preview_video', verbose_name='Вступительное видео курса'),
        ),
        migrations.DeleteModel(
            name='CourseMedia',
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_chapter', to='courses.course'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]