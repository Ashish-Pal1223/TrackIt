from django.urls import path
from .  import views

urlpatterns = [
    path('', views.anime, name="anime"),
]