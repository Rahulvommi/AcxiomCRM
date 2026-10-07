from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.shortcuts import redirect

from accounts.views import dashboard


urlpatterns = [
    path('', lambda request: redirect('dashboard')),

    path('admin/', admin.site.urls),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('dashboard/', dashboard, name='dashboard'),

    path('customers/', include('customers.urls')),
    path('leads/', include('leads.urls')),
    path('opportunities/', include('opportunities.urls')),
    path('followups/', include('followups.urls')),
    path('api/', include('api.urls')),
    path('audit/', include('audit.urls')),
  
]