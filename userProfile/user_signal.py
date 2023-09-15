from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
#from django.contrib.auth.models import User
#from .models import Profile
from django.conf import settings
from . import models

#for ip address in case of user login
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return

    # create the profile objects, only if it is newly created
    profile = models.profile.Profile(user=instance)
    profile.save()

#for ip address after that go to views.py and define
@receiver(user_logged_in, sender = User)
def login_success(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip

# First create class Profile in home->models.py and also define user as a OneToOneField mapping and image field
#after that forms.py for this Profile and then use in dashboard. Also define signals.py in apps and then some code
# in apps.py for ready method, and some code in __init__.py for running this profile properly