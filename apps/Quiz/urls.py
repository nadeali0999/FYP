# quizzes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<slug:course_slug>/quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_details'),
    path('quiz_start/<slug:course_slug>/quiz/<int:quiz_id>/', views.quiz_start, name='quiz_start'),
]
