from django.urls import path
from . import views

urlpatterns = [
        path("/text", views.get_text, name="get_text"),
        path("/speech", views.set_speech, name="set_speech")
    ]
