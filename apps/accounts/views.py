from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, FormView

from apps.courses.models import Categories, Course
from .forms import ContactForm
from .forms import loginForm


class BaseView(TemplateView):
    template_name = 'base.html'


class ContactView(FormView):
    template_name = 'main/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class errorView(TemplateView):
    template_name = '404_Error/404.html'

    def get_context_data(self, **kwargs):
        # First, call the base implementation to get a context
        context = super().get_context_data(**kwargs)
        # Add custom context data, here assuming Categories is properly imported and get_all_categories is a valid method
        context['categories'] = Categories.get_all_categories()
        return context


class signupView(TemplateView):
    template_name = 'accounts/signup.html'

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists!')
            return redirect('signup')

        # Check username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists!')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')

    def get(self, request):
        return render(request, self.template_name)


class loginView(TemplateView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = loginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Email and password are invalid!')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, "{}: {}".format(field, error))
        return render(request, self.template_name, {'form': form})


class homeView(TemplateView):
    template_name = 'main/home.html'  # Ensure you specify your template

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the queryset of categories, ordered by 'id' and limited to the first 5
        context['categories'] = Categories.objects.all().order_by('id')[:5]
        context['course'] = Course.objects.filter(status='PUBLISH').order_by('-id')
        return context


class about_usView(TemplateView):
    template_name = 'main/about_us.html'

    def get_context_data(self, **kwargs):
        # First, call the base implementation to get a context
        context = super().get_context_data(**kwargs)
        # Add custom context data, here assuming Categories is properly imported and get_all_categories is a valid method
        context['categories'] = Categories.get_all_categories()
        return context


class contact_usView(TemplateView):
    template_name = 'main/contact_us.html'

    def get_context_data(self, **kwargs):
        # First, call the base implementation to get a context
        context = super().get_context_data(**kwargs)
        # Add custom context data, here assuming Categories is properly imported and get_all_categories is a valid method
        context['categories'] = Categories.get_all_categories()
        return context
