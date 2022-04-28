from django.db import models


# Create your models here.
class Flight(models.Model):

    flight_number = models.IntegerField()
    airline = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    date_of_departure = models.DateField()
    departure_time = models.TimeField()

    class Meta:
        verbose_name = 'Flight'

    def __str__(self):
        return f'{self.flight_number} -> {self.airline}'


class Passenger(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(unique=True, max_length=14)

    class Meta:
        verbose_name = 'Passenger'

    def __str__(self):
        return f'{self.first_name} {self.last_name} -> {self.email}.'


class Reservation(models.Model):

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Reservation'

    def __str__(self):
        return f'{self.passenger.first_name}{self.passenger.last_name} is reserved in {self.flight.airline}'