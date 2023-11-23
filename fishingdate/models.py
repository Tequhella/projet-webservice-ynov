from django.db import models
from typing import List
from pydantic import (
    BaseModel,
)


class User(models.Model):

    lastname = models.CharField(max_lenght=255)
    firstname = models.CharField(max_lenght=255)
    birthday = models.DateTimeField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    languages = models.JSONField()
    url = models.CharField(max_length=255)
    boatLicenseNumber = models.CharField(max_length=255)
    insuranceNumber = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    activity = models.CharField(max_length=1025)
    siretNumber = models.IntegerField()
    tradeRegisterNumber = models.CharField(max_length=255)


class Notebook(models.model):

    url = models.CharField(max_length=255)
    comment = models.CharField(1023)
    size = models.DecimalField(decimal_places=1)
    weight = models.DecimalField(decimal_places=3)
    place = models.CharField(max_length=255)
    date = models.DateTimeField()
    released = models.BooleanField()

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='notebook')


class Boat(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    brand = models.CharField(max_length=255)
    fabrication_year = models.IntegerField()
    url_boat_photo = models.CharField(max_length=255)
    boat_license_type = models.CharField(max_length=255)
    boatType = models.CharField(max_length=255)
    equipments = models.JSONField()
    deposit = models.IntegerField()
    capacity = models.IntegerField()
    bedsNumber = models.IntegerField()
    harbor: models.CharField(max_length=255)
    longitude = models.DecimalField()
    latitude = models.DecimalField()
    motor = models.CharField(max_length=255)
    horsepower = models.IntegerField()

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='boatsList')


class DateTimeList(BaseModel):
    start_date: models.DateTimeField()
    end_date: models.DateTimeField()


class Excursion(models.Model):
    title = models.CharField(max_length=255)
    information = models.CharField(max_length=1023)
    excursion_yype = models.CharField(max_length=255)
    tariff = models.CharField(max_length=255)
    date_time_list = List[DateTimeList]
    number_of_passengers = models.IntegerField()
    excursion_price = models.DecimalField(decimal_places=2)
    id_owner = models.IntegerField()
    id_boat = models.IntegerField()

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='fishingExcursionsList')


class Booking(models.Model):
    id_excursion = models.IntegerField()
    date= models.DateTimeField()
    nb_booked_seats = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2)
    id_booker = models.IntegerField()

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='bookingsList')