from django.contrib.auth import views
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gramapp.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/logout/$', views.logout_then_login, {"next_page": '/'}),
]
