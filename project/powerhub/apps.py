from django.apps import AppConfig


class PowerhubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'powerhub'

    def ready(self):
        import powerhub.signals