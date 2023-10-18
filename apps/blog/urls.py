from django.urls import path
from .views import (
    base_view,
    country_details,
    city_details,
    pricing_view,
)



urlpatterns = [
    path("", base_view, name="base_view"),
    path("country/details/<int:pk>", country_details, name="country_details"),
    path("city/details/<int:pk>", city_details, name="city_details"),
    path("price", pricing_view, name="pricing_view")
]