from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Opportunity
from customers.models import Customer
from audit.utils import log_action


@login_required
def opportunity_list(request):
    opportunities = Opportunity.objects.select_related(
        'customer',
        'owner'
    ).order_by('-created_at')

    return render(
        request,
        'opportunities/list.html',
        {'opportunities': opportunities}
    )


@login_required
def opportunity_create(request):

    customers = Customer.objects.all().order_by('name')

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        customer_id = request.POST.get('customer')
        stage = request.POST.get('stage', 'Qualification')
        amount = request.POST.get('amount', '')
        probability = request.POST.get('probability', '')
        expected_close_date = request.POST.get(
            'expected_close_date'
        )
        source = request.POST.get('source', '').strip()
        notes = request.POST.get('notes', '').strip()

        # Required fields
        if not name or not customer_id or not amount or not probability or not expected_close_date:
            messages.error(
                request,
                'Please fill all required fields.'
            )
            return render(
                request,
                'opportunities/form.html',
                {'customers': customers}
            )

        # Amount validation
        try:
            amount_value = float(amount)
        except ValueError:
            messages.error(
                request,
                'Opportunity Amount must be a valid number.'
            )
            return render(
                request,
                'opportunities/form.html',
                {'customers': customers}
            )

        if amount_value <= 0:
            messages.error(
                request,
                'Opportunity Amount must be greater than 0.'
            )
            return render(
                request,
                'opportunities/form.html',
                {'customers': customers}
            )

        # Probability validation
        try:
            probability_value = int(probability)
        except ValueError:
            messages.error(
                request,
                'Probability must be a number between 0 and 100.'
            )
            return render(
                request,
                'opportunities/form.html',
                {'customers': customers}
            )

        if probability_value < 0 or probability_value > 100:
            messages.error(
                request,
                'Probability must be between 0 and 100.'
            )
            return render(
                request,
                'opportunities/form.html',
                {'customers': customers}
            )

        # Close date validation
        try:
            close_date = date.fromisoformat(
                expected_close_date
            )
        except ValueError:
            messages.error(
                request,
                'Please enter a valid close date.'
            )
            return render(
                request,
                'opportunities/form.html',
                {'customers': customers}
            )

        if stage not in ['Won', 'Lost'] and close_date < date.today():
            messages.error(
                request,
                'Expected close date cannot be in the past for an active opportunity.'
            )
            return render(
                request,
                'opportunities/form.html',
                {'customers': customers}
            )

        customer = Customer.objects.get(id=customer_id)

        opportunity = Opportunity.objects.create(
            name=name,
            customer=customer,
            owner=request.user,
            stage=stage,
            amount=amount_value,
            probability=probability_value,
            expected_close_date=close_date,
            source=source,
            notes=notes
        )
        log_action(
    request,
    'CREATE',
    'Opportunity',
    opportunity.id,
    '',
    name
)

        messages.success(
            request,
            'Opportunity created successfully.'
        )

        return redirect('opportunity_list')

    return render(
        request,
        'opportunities/form.html',
        {'customers': customers}
    )