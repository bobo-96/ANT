# Generated by Django 3.2.4 on 2021-06-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Cтатус учителя'),
        ),
    ]
