# Generated by Django 5.0.4 on 2024-06-05 13:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_alter_course_author_delete_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='completed_by',
            field=models.ManyToManyField(blank=True, related_name='completed_videos', to=settings.AUTH_USER_MODEL),
        ),
    ]