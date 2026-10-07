from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):

    help = 'Create demo users and roles for AcxiomCRM'

    def handle(self, *args, **kwargs):

        admin_group, _ = Group.objects.get_or_create(name='Admin')
        manager_group, _ = Group.objects.get_or_create(name='Manager')
        sales_group, _ = Group.objects.get_or_create(name='Sales Executive')

        users = [
            ('admin', 'Admin@12345', admin_group),
            ('manager', 'Manager@12345', manager_group),
            ('salesuser', 'Sales@12345', sales_group),
        ]

        for username, password, group in users:

            user, created = User.objects.get_or_create(
                username=username
            )

            user.set_password(password)
            user.is_active = True

            if username == 'admin':
                user.is_staff = True
                user.is_superuser = True

            user.save()
            user.groups.add(group)

            self.stdout.write(
                self.style.SUCCESS(
                    f'Created/updated {username}'
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Demo users are ready.'
            )
        )
