from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from customers.models import Customer
from leads.models import Lead
from opportunities.models import Opportunity

from .serializers import (
    CustomerSerializer,
    LeadSerializer,
    OpportunitySerializer,
)


class CustomerListCreateAPI(generics.ListCreateAPIView):

    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class LeadListCreateAPI(generics.ListCreateAPIView):

    queryset = Lead.objects.all().order_by('-created_at')
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]


class OpportunityListCreateAPI(generics.ListCreateAPIView):

    queryset = Opportunity.objects.all().order_by('-created_at')
    serializer_class = OpportunitySerializer
    permission_classes = [IsAuthenticated]