# Generated by Django 4.1.7 on 2023-04-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement_app', '0016_remove_student_gpa_cgpa_student_cgpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_TPO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpo_name', models.CharField(default='', max_length=100)),
                ('tpo_join', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(default='', max_length=10)),
                ('tpo_mail', models.CharField(default='', max_length=100)),
                ('tpo_phone', models.CharField(default='', max_length=12)),
                ('password', models.CharField(default='', max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Student_CGPA',
        ),
    ]
