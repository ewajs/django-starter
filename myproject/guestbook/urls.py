from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.sign, name="sign"),
]
