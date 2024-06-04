from django.contrib import admin

from apps.Quiz.models import Quiz, Question


class QuestionTabularInline(admin.TabularInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionTabularInline]  # Only include QuestionTabularInline


 # admin.site.register(Question)
