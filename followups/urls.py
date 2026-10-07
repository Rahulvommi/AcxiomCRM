from django.urls import path
from . import views

urlpatterns = [
    path('', views.followup_list, name='followup_list'),
    path('create/', views.followup_create, name='followup_create'),
]