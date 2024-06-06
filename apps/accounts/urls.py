from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [

     path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name= 'password_reset'),
     path('login/', loginView.as_view(), name='login'),
     path('signup/', signupView.as_view(), name='signup'),
     path('', homeView.as_view(), name='home'),
     path('base', BaseView.as_view(), name='base'),
     path('aboutus/', about_usView.as_view(), name='about_us'),
     path('contact_us/', contact_usView.as_view(), name='contact_us'),
     path('404/', errorView.as_view(), name='404'),
     path('contact/', ContactView.as_view(), name='contact'),
     path('contact/success/', TemplateView.as_view(template_name="main/contact_success.html"), name='contact_success'),

]
