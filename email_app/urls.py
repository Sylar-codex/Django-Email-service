from .api import EmailMessengerAPI
from django.urls import include, path

urlpatterns = [
    path("api/send_email",EmailMessengerAPI.as_view())
]