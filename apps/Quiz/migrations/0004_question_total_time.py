# Generated by Django 5.0.4 on 2024-06-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_remove_quiz_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='total_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]