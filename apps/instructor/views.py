from django.shortcuts import render

from apps.instructor.models import Author


def instructors_list(request):
    authors = Author.objects.all()
    return render(request, 'instructors/intstructors.html', {'authors': authors})