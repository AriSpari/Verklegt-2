from django.apps import AppConfig
from django.contrib.auth import signals

class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "User"

    def ready(self):
        signals.user_logged_in.disconnect(dispatch_uid='update_last_login')