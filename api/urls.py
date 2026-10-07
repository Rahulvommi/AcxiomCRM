from django.urls import path

from .views import (
    CustomerListCreateAPI,
    LeadListCreateAPI,
    OpportunityListCreateAPI,
)


urlpatterns = [

    path(
        'customers/',
        CustomerListCreateAPI.as_view(),
        name='api_customers'
    ),

    path(
        'leads/',
        LeadListCreateAPI.as_view(),
        name='api_leads'
    ),

    path(
        'opportunities/',
        OpportunityListCreateAPI.as_view(),
        name='api_opportunities'
    ),
]