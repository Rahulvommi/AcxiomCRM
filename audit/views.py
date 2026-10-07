from django.shortcuts import render

from accounts.decorators import role_required
from .models import AuditLog


@role_required('Admin', 'Manager')
def audit_list(request):

    logs = AuditLog.objects.select_related(
        'user'
    ).order_by('-created_date')

    return render(
        request,
        'audit/list.html',
        {'logs': logs}
    )