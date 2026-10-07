from .models import AuditLog


def log_action(
    request,
    action,
    entity_name,
    record_id='',
    old_value='',
    new_value=''
):

    ip_address = request.META.get(
        'REMOTE_ADDR'
    )

    AuditLog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        action=action,
        entity_name=entity_name,
        record_id=str(record_id),
        old_value=str(old_value),
        new_value=str(new_value),
        ip_address=ip_address
    )