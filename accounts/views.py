from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from customers.models import Customer
from leads.models import Lead
from opportunities.models import Opportunity
from followups.models import FollowUp


@login_required
def dashboard(request):

    total_customers = Customer.objects.count()

    total_leads = Lead.objects.count()

    open_leads = Lead.objects.exclude(
        status__in=['Converted', 'Lost']
    ).count()

    total_opportunities = Opportunity.objects.count()

    open_opportunities = Opportunity.objects.exclude(
        stage__in=['Won', 'Lost']
    ).count()

    won_opportunities = Opportunity.objects.filter(
        stage='Won'
    ).count()

    lost_opportunities = Opportunity.objects.filter(
        stage='Lost'
    ).count()

    total_pipeline_value = sum(
        opportunity.weighted_value()
        for opportunity in Opportunity.objects.exclude(
            stage__in=['Won', 'Lost']
        )
    )

    lead_status_data = []

    for status, label in Lead.STATUS_CHOICES:
        lead_status_data.append({
            'status': label,
            'count': Lead.objects.filter(
                status=status
            ).count()
        })

    opportunity_stage_data = []

    for stage, label in Opportunity.STAGE_CHOICES:
        opportunity_stage_data.append({
            'stage': label,
            'count': Opportunity.objects.filter(
                stage=stage
            ).count()
        })

    context = {
        'total_customers': total_customers,
        'total_leads': total_leads,
        'open_leads': open_leads,
        'total_opportunities': total_opportunities,
        'open_opportunities': open_opportunities,
        'won_opportunities': won_opportunities,
        'lost_opportunities': lost_opportunities,
        'total_pipeline_value': total_pipeline_value,
        'lead_status_data': lead_status_data,
        'opportunity_stage_data': opportunity_stage_data,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )