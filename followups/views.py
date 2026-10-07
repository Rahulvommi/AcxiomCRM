from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import FollowUp
from customers.models import Customer
from leads.models import Lead
from opportunities.models import Opportunity


@login_required
def followup_list(request):
    followups = FollowUp.objects.select_related(
        'customer',
        'lead',
        'opportunity',
        'assigned_to'
    ).order_by('date')

    return render(
        request,
        'followups/list.html',
        {'followups': followups}
    )


@login_required
def followup_create(request):

    customers = Customer.objects.all().order_by('name')
    leads = Lead.objects.all().order_by('name')
    opportunities = Opportunity.objects.all().order_by('name')

    if request.method == 'POST':

        customer_id = request.POST.get('customer')
        lead_id = request.POST.get('lead')
        opportunity_id = request.POST.get('opportunity')
        followup_date = request.POST.get('date')
        subject = request.POST.get('subject', '').strip()
        followup_type = request.POST.get('type', 'Call')
        status = request.POST.get('status', 'Planned')
        notes = request.POST.get('notes', '').strip()

        if not followup_date or not subject:
            messages.error(
                request,
                'Date and subject are required.'
            )
            return render(request, 'followups/form.html', {
                'customers': customers,
                'leads': leads,
                'opportunities': opportunities
            })

        try:
            selected_date = date.fromisoformat(followup_date)
        except ValueError:
            messages.error(request, 'Please enter a valid date.')
            return render(request, 'followups/form.html', {
                'customers': customers,
                'leads': leads,
                'opportunities': opportunities
            })

        # Planned follow-ups cannot be in the past
        if status == 'Planned' and selected_date < date.today():
            messages.error(
                request,
                'Follow-up date cannot be in the past.'
            )
            return render(request, 'followups/form.html', {
                'customers': customers,
                'leads': leads,
                'opportunities': opportunities
            })

        customer = Customer.objects.filter(
            id=customer_id
        ).first() if customer_id else None

        lead = Lead.objects.filter(
            id=lead_id
        ).first() if lead_id else None

        opportunity = Opportunity.objects.filter(
            id=opportunity_id
        ).first() if opportunity_id else None

        FollowUp.objects.create(
            customer=customer,
            lead=lead,
            opportunity=opportunity,
            date=selected_date,
            subject=subject,
            type=followup_type,
            status=status,
            notes=notes,
            assigned_to=request.user
        )

        messages.success(
            request,
            'Follow-up created successfully.'
        )

        return redirect('followup_list')

    return render(request, 'followups/form.html', {
        'customers': customers,
        'leads': leads,
        'opportunities': opportunities
    })