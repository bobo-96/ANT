# Generated by Django 3.2.4 on 2021-06-03 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
    ]
