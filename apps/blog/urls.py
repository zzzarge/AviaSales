from django.urls import path
from .views import (
    base_view,
    country_details,
)



urlpatterns = [
    path("", base_view, name="base_view"),
    path("country_details/<int:pk>", country_details, name="country_details"),
    
]