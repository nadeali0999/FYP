from django.core.validators import RegexValidator
from django.db import models

class Author(models.Model):
    author_profile = models.ImageField(upload_to="Media/author")
    name = models.CharField(
        max_length=100,
        null=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='Name must only contain alphabetic characters.',
                code='invalid_name'
            )
        ]
    )
    about_author = models.TextField()

    def __str__(self):
        return self.name
