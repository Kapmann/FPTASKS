from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name="back_office.products"),
]