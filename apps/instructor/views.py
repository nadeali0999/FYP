from django.db.models import Q
from django.shortcuts import render

from apps.instructor.models import Author


def instructors_list(request):
    query = request.GET.get('q')
    authors = Author.objects.all()

    if query:
        authors = authors.filter(
            Q(name__icontains=query) |
            Q(profession__icontains=query)
        )

    return render(request, 'instructors/intstructors.html', {'authors': authors})