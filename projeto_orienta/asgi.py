from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import app_chat.routing
import os
import django
django.setup()

application = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_orienta.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            app_chat.routing.websocket_urlpatterns
        )
    ),
})