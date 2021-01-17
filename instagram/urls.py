from django.conf.urls import url,include
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gramapp.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.LoginView.as_view(template_name='django_registration/registration_form.html')),
    path('accounts/login/', views.LoginView.as_view(template_name='django_registration/login.html')),
    path('accounts/logout/',views.LogoutView.as_view(next_page= '/')),
]
