from auth_users.models import Register


def subject_renderer(request):
    return {
        "register_all": Register.objects.all(),
    }
