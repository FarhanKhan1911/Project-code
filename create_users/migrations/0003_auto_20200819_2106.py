# Generated by Django 3.0.7 on 2020-08-19 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200817_2203'),
        ('create_users', '0002_auto_20200819_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
