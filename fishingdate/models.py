from django.db import models


class User(models.Model):

    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    languages = models.JSONField(null=True)
    URLAvatar = models.CharField(max_length=255)
    boatLicenseNumber = models.CharField(max_length=255)
    insuranceNumber = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    activity = models.CharField(max_length=1023)
    siretNumber = models.IntegerField(null=True)
    tradeRegisterNumber = models.CharField(max_length=255)


class Notebook(models.Model):

    URLFish = models.CharField(max_length=255)
    comment = models.CharField(max_length=1023)
    size = models.DecimalField(max_digits=1, decimal_places=1)
    weight = models.DecimalField(max_digits=3, decimal_places=3)
    place = models.CharField(max_length=255)
    date = models.DateTimeField(null=True)
    released = models.BooleanField(null=True)

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='notebook')


class Boat(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    brand = models.CharField(max_length=255)
    year = models.IntegerField(null=True)
    URLBoat = models.CharField(max_length=255)
    boatLicenseType = models.CharField(max_length=255)
    boatType = models.CharField(max_length=255)
    equipments = models.JSONField(null=True)
    deposit = models.IntegerField(null=True)
    capacity = models.IntegerField(default=2)
    bedsNumber = models.IntegerField(null=True)
    harbor = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    motor = models.CharField(max_length=255)
    horsepower = models.IntegerField(null=True)

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='boatsList')


class Excursion(models.Model):
    excursionTitle = models.CharField(max_length=255)
    information = models.CharField(max_length=1023)
    excursionType = models.CharField(max_length=255)
    tariff = models.CharField(max_length=255)
    dateTimeList = models.JSONField(null=True)
    numberOfPassengers = models.IntegerField(null=True)
    excursionPrice = models.DecimalField(max_digits=3, decimal_places=2)
    idOwner = models.IntegerField(null=True)
    idBoat = models.IntegerField(null=True)

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='fishingExcursionsList')


class Booking(models.Model):
    idExcursion = models.IntegerField(null=True)
    date = models.DateTimeField(null=True)
    nbBookedSeats = models.IntegerField(null=True)
    totalPrice = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    idBooker = models.IntegerField(null=True)

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='bookingsList')