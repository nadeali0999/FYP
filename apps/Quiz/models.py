from django.db import models

from apps.courses.models import Course


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=1024)
    option1 = models.CharField(max_length=255, verbose_name='Option 1', default='Default Option 1')
    option2 = models.CharField(max_length=255, verbose_name='Option 2', default='Default Option 2')
    option3 = models.CharField(max_length=255, verbose_name='Option 3', default='Default Option 3')
    option4 = models.CharField(max_length=255, verbose_name='Option 4', default='Default Option 4')
    correct_answer = models.CharField(max_length=255, help_text="Enter the correct answer exactly as one of the options", default='Default Option 1')

    def __str__(self):
        return self.text

