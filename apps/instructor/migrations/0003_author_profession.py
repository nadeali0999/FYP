# Generated by Django 5.0.4 on 2024-06-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_alter_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profession',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
