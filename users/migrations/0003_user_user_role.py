# Generated by Django 5.0.6 on 2024-06-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher'), ('admin', 'admin')], default='student', max_length=250),
        ),
    ]
