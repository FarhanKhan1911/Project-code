# Generated by Django 3.0.7 on 2020-11-11 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0006_batch'),
        ('management', '0003_auto_20200912_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('teacher', models.CharField(max_length=200)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Department')),
                ('student', models.ManyToManyField(to='student.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Subject')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Year')),
            ],
        ),
    ]
