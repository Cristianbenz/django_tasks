# Generated by Django 4.1.4 on 2022-12-06 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_tasks_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(default='undefined', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
