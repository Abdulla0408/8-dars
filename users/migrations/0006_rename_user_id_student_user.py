# Generated by Django 5.0.6 on 2024-06-08 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_student_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user_id',
            new_name='user',
        ),
    ]
