from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),

    path(
        'create/',
        views.customer_create,
        name='customer_create'
    ),

    path(
        '<int:customer_id>/edit/',
        views.customer_edit,
        name='customer_edit'
    ),

    path(
        '<int:customer_id>/delete/',
        views.customer_delete,
        name='customer_delete'
    ),
]