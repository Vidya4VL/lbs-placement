# Generated by Django 4.1.7 on 2023-04-10 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placement_app', '0009_remove_student_gpa_unique_student_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_gpa',
            name='cgpa',
        ),
        migrations.CreateModel(
            name='Student_CGPA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_app.student_gpa')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_app.student')),
            ],
        ),
    ]
