from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError

def trigger_signal_view(request):
    try:
        # Check if the user already exists, if not create a new one
        user, created = User.objects.get_or_create(username='Balaji Sabat', email='Balaji@gmail.com')
        if created:
            message = "New user created and signal triggered"
        else:
            message = "User already exists, no signal triggered"
    except IntegrityError:
        return HttpResponse("Error creating the user", status=500)

    return HttpResponse(message)
