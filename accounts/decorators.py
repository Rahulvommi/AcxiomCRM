from django.contrib.auth.decorators import user_passes_test


def role_required(*roles):

    def check_role(user):

        if not user.is_authenticated:
            return False

        return user.groups.filter(
            name__in=roles
        ).exists()

    return user_passes_test(
        check_role,
        login_url='/login/'
    )