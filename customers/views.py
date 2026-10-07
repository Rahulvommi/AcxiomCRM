from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Customer
from audit.models import AuditLog
from accounts.decorators import role_required


@login_required
def customer_list(request):

    query = request.GET.get('q', '')

    customers = Customer.objects.all().order_by('-created_at')

    if query:
        customers = customers.filter(
            name__icontains=query
        )

    return render(
        request,
        'customers/list.html',
        {
            'customers': customers,
            'query': query
        }
    )


@login_required
def customer_create(request):

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()
        status = request.POST.get('status', 'Active')
        notes = request.POST.get('notes', '').strip()

        if not name or not email or not phone:
            messages.error(
                request,
                'Name, email and phone are required.'
            )

            return render(
                request,
                'customers/form.html'
            )

        if Customer.objects.filter(email=email).exists():
            messages.error(
                request,
                'A customer with this email already exists.'
            )

            return render(
                request,
                'customers/form.html'
            )

        if Customer.objects.filter(phone=phone).exists():
            messages.error(
                request,
                'A customer with this phone number already exists.'
            )

            return render(
                request,
                'customers/form.html'
            )

        customer = Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            status=status,
            notes=notes
        )

        # Audit log
        AuditLog.objects.create(
            user=request.user,
            action='CREATE',
            entity_name='Customer',
            record_id=str(customer.id),
            old_value='',
            new_value=name,
            ip_address=request.META.get('REMOTE_ADDR')
        )

        messages.success(
            request,
            'Customer created successfully.'
        )

        return redirect('customer_list')

    return render(
        request,
        'customers/form.html'
    )


@login_required
def customer_edit(request, customer_id):

    customer = get_object_or_404(
        Customer,
        id=customer_id
    )

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()
        status = request.POST.get('status', 'Active')
        notes = request.POST.get('notes', '').strip()

        if not name or not email or not phone:
            messages.error(
                request,
                'Name, email and phone are required.'
            )

            return render(
                request,
                'customers/form.html',
                {'customer': customer}
            )

        if Customer.objects.filter(
            email=email
        ).exclude(
            id=customer.id
        ).exists():

            messages.error(
                request,
                'A customer with this email already exists.'
            )

            return render(
                request,
                'customers/form.html',
                {'customer': customer}
            )

        if Customer.objects.filter(
            phone=phone
        ).exclude(
            id=customer.id
        ).exists():

            messages.error(
                request,
                'A customer with this phone number already exists.'
            )

            return render(
                request,
                'customers/form.html',
                {'customer': customer}
            )

        customer.name = name
        customer.email = email
        customer.phone = phone
        customer.address = address
        customer.status = status
        customer.notes = notes

        customer.save()

        messages.success(
            request,
            'Customer updated successfully.'
        )

        return redirect('customer_list')

    return render(
        request,
        'customers/form.html',
        {'customer': customer}
    )


@role_required('Admin', 'Manager')
def customer_delete(request, customer_id):

    customer = get_object_or_404(
        Customer,
        id=customer_id
    )

    if request.method == 'POST':

        customer.delete()

        messages.success(
            request,
            'Customer deleted successfully.'
        )

    return redirect('customer_list')