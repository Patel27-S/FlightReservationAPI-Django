from django.urls import path, include
from .api_views import ListCreateFlights, ListCreatePasssengers, ListCreateReservations


urlpatterns = [
    path('find_create_flights/', ListCreateFlights.as_view()),
    path('find_create_passengers/', ListCreatePasssengers.as_view()),
    path('find_create_reservations/', ListCreateReservations.as_view())
]
