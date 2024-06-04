from django.urls import path

from apps.instructor import views

urlpatterns = [
    path('instructor/', views.instructor, name='instructor'),
]