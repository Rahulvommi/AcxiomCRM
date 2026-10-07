from rest_framework import serializers

from customers.models import Customer
from leads.models import Lead
from opportunities.models import Opportunity


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'address',
            'status',
            'notes',
            'created_at',
        ]


class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'source',
            'status',
            'priority',
            'expected_value',
            'notes',
            'created_at',
        ]


class OpportunitySerializer(serializers.ModelSerializer):

    weighted_pipeline = serializers.SerializerMethodField()

    class Meta:
        model = Opportunity
        fields = [
            'id',
            'name',
            'customer',
            'owner',
            'stage',
            'amount',
            'probability',
            'expected_close_date',
            'source',
            'notes',
            'weighted_pipeline',
            'created_at',
        ]

    def get_weighted_pipeline(self, obj):
        return obj.weighted_value()