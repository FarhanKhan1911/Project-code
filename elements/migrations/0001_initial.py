# Generated by Django 3.0.7 on 2020-09-11 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0003_auto_20200912_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elements_status', models.CharField(choices=[('experiment', 'Experiment'), ('assignment', 'Assignment'), ('mini project', 'Mini Project')], default='experiment', max_length=15)),
                ('element_name', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
                ('upload', models.FileField(upload_to='assignments/')),
                ('due_date', models.DateField()),
                ('created_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_status', models.CharField(choices=[('unsubmitted', 'Unsubmitted'), ('submitted', 'Submitted')], default='unsubmitted', max_length=15)),
                ('upload', models.FileField(upload_to='submissions/')),
                ('submitted_at', models.DateField(auto_now=True)),
                ('grade', models.IntegerField(default=0)),
                ('feedback', models.CharField(blank=True, default='No feedback yet', max_length=255, null=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elements.Elements')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]