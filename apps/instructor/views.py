from django.shortcuts import render

def instructor(request):
    return render(request, 'instructors/intstructors.html')