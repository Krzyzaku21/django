from django.shortcuts import render, reverse
from .models import Notifications
from django.http import HttpResponseRedirect
# Create your views here.

def show_notification(request, notification_id):
    n = Notifications.objects.get(id=notification_id)
    return render(request, 'notification.html', {'notification' : n})

def delete_notification(request, notification_id):
    n = Notifications.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect(reverse('loggedin'))
