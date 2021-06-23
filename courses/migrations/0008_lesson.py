# Generated by Django 3.2.4 on 2021-06-21 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0007_auto_20210609_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название урока')),
                ('lesson_video_material', models.FileField(upload_to='lesson_video_material', verbose_name='Видео материалы')),
                ('description', models.TextField(verbose_name='Описание урока')),
                ('lesson_materials', models.FileField(upload_to='lesson_materials', verbose_name='Материалы по уроку')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_lesson', to='courses.course')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]