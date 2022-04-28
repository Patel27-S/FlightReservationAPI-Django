from django.shortcuts import render
from rest_framework import generics
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer

# Create your views here.


# API view for listing all the flights and adding a new one if have to :
class ListCreateFlights(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


# API view for listing all the passengers and adding a new one if have to :
class ListCreatePasssengers(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


# API view for listing all the reservations and creating a new one if have to :
class ListCreateReservations(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


