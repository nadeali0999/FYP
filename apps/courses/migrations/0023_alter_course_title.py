# Generated by Django 5.0.6 on 2024-06-12 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_remove_course_featured_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=500, validators=[django.core.validators.RegexValidator(code='invalid_title', message='Title must not contain numbers.', regex='^[^\\d]*$')]),
        ),
    ]
