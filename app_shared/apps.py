from django.apps import AppConfig


class AppSharedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_shared'
