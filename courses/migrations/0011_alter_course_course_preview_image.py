# Generated by Django 3.2.4 on 2021-07-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_homework_studentshomeworks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_preview_image',
            field=models.FileField(null=True, upload_to='course_preview_image', verbose_name='Изображение курса'),
        ),
    ]
