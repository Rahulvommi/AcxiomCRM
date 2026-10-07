from django.urls import path
from . import views

urlpatterns = [
    path('', views.opportunity_list, name='opportunity_list'),
    path('create/', views.opportunity_create, name='opportunity_create'),
]