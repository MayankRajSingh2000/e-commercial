from django.apps import AppConfig
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _



class UserprofileConfig(AppConfig):
    name = 'userProfile'
    verbose_name = _('profiles')

    def ready(self):
        import userProfile.user_signal
