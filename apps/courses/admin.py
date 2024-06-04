from django.contrib import admin
from apps.Quiz.models import Quiz
from .models import *

class WhatToLearnTabularInline(admin.TabularInline):
    model = what_to_learn


# Inline admin for the Requirements model
class RequirementsTabularInline(admin.TabularInline):
    model = requirements


class VideoTabularInline(admin.TabularInline):
    model = Video


class LessonTabularInline(admin.TabularInline):
    model = Lesson




# Admin class for the Course model
class CourseAdmin(admin.ModelAdmin):
    inlines = [RequirementsTabularInline, WhatToLearnTabularInline, LessonTabularInline, VideoTabularInline]


# Register your models and their respective admin classes

admin.site.register(Author)  # Assuming Author does not need a custom admin
admin.site.register(Course, CourseAdmin)

# we just show these at inlines only we dont want it to separtly showw so we unregister using admin.site.unregister
# admin.site.register(Level)
# admin.site.register(requirements)
# admin.site.register(what_to_learn)
# admin.site.register(Categories)
# admin.site.register(Lesson)
# admin.site.register(Language)
