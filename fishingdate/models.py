from django.db import models


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

    boats = models.ForeignKey('fishingdate.Boat', on_delete=models.CASCADE, related_name='user')
    fishingLogs = models.ForeignKey('fishingdate.FishingLog', on_delete=models.CASCADE, related_name='user')

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

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='boats')