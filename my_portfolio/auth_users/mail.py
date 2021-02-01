from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views import View


class SendMailToUser(object):
    def post(self):
        user_email = User.objects.GET.get('email')
        send_mail('django test mail', 'body', 'glessapp@gmail.com', [user_email], fail_silently=False)
        return send_mail
