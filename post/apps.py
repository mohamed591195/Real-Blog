from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'post'
    def ready(self):
        from . import signals