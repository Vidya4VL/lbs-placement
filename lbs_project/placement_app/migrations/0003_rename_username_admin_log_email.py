# Generated by Django 4.1.7 on 2023-04-04 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement_app', '0002_student_student_gpa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_log',
            old_name='username',
            new_name='email',
        ),
    ]
