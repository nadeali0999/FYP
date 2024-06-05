from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic import TemplateView, ListView

from apps.courses.models import *
from apps.payments.models import Enrollment


class SingleCourseView(TemplateView):
    template_name = 'main/single_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['FreeCourse_count'] = Course.objects.filter(price=0).count()
        context['PaidCourse_count'] = Course.objects.filter(price__gte=1).count()
        context['levels'] = Level.objects.all()
        context['course'] = Course.objects.all()
        context['categories'] = Categories.get_all_categories()  # Ensuring correct method call
        return context


class SearchCourseView(ListView):
    model = Course
    template_name = 'search/search.html'
    context_object_name = 'course'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Course.objects.filter(title__icontains=query)


class course_detailsView(TemplateView):
    template_name = 'courses/course_details.html'

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            self.course = Course.objects.get(slug=slug)
        except Course.DoesNotExist:
            # Redirect to the custom 404 page
            return redirect('404')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course

        # Calculate the total duration of videos related to the course
        total_duration = Video.objects.filter(course=self.course).aggregate(total=Sum('time_duration'))['total']
        context['time_duration'] = total_duration

        user = self.request.user
        is_enrolled = Enrollment.objects.filter(user=user, course=self.course).exists()
        context['is_enrolled'] = is_enrolled

        return context


def watch_course(request, slug):
    print('here is...', slug)
    course = Course.objects.get(slug=slug)
    return render(request, 'courses/watch_course.html', {'course': course, 'time_duration':
        Video.objects.filter(course=course).aggregate(total=Sum('time_duration'))['total'],
                                                         'is_enrolled': Enrollment.objects.filter(user=request.user,
                                                                                                  course=course).exists()})


def my_learning(request):
    return render(request, 'main/my_learning.html')


def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['PriceFree']:
        course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
        course = Course.objects.filter(price__gte=1)
    elif price == ['PriceAll']:
        course = Course.objects.all()
    elif categories:
        course = Course.objects.filter(category__id__in=categories).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in=level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    t = render_to_string('ajax/course.html', {'course': course})

    return JsonResponse({'data': t})
