from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:nr>", views.monthly_challenge_num),
    path("<str:maand>", views.monthly_challenge, name="month-challenge")
]
