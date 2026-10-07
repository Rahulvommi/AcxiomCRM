from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Lead
from audit.utils import log_action

@login_required
def lead_list(request):
    leads = Lead.objects.all().order_by('-created_at')

    return render(
        request,
        'leads/list.html',
        {'leads': leads}
    )


@login_required
def lead_create(request):

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        source = request.POST.get('source', '').strip()
        status = request.POST.get('status', 'New')
        priority = request.POST.get('priority', 'Medium')
        expected_value = request.POST.get(
            'expected_value', '0'
        )
        notes = request.POST.get('notes', '').strip()

        lead = Lead.objects.create(
            name=name,
            email=email,
            phone=phone,
            source=source,
            status=status,
            priority=priority,
            expected_value=expected_value,
            notes=notes
        )
        log_action(
    request,
    'CREATE',
    'Lead',
    lead.id,
    '',
    name
)

        return redirect('lead_list')

    return render(request, 'leads/form.html')