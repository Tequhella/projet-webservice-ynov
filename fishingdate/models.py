from django.db import models


class User(models.Model):

    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    URLAvatar = models.CharField(max_length=255)
    boatLicenseNumber = models.CharField(max_length=255)
    insuranceNumber = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    activity = models.CharField(max_length=1025)
    siretNumber = models.IntegerField()
    tradeRegisterNumber = models.CharField(max_length=255)

    def boatList(self):
        return [{"id" : boat.id, "name" : boat.name} for boat in self.boatsList.all()]

    def notebookPageList(self):
        return [{"id" : page.id, "URLFish" : page.URLFish} for page in self.notebook.all()]

    def excursionList(self):
        return [{"id" : excursion.id, "excursionTitle" : excursion.excursionTitle} for excursion in self.fishingExcursionsList.all()]

    def bookingList(self):
        return [{"id" : booking.id, "date" : booking.date} for booking in self.bookingsList.all()]


class Notebook(models.Model):

    URLFish = models.CharField(max_length=255)
    comment = models.CharField(max_length=1023)
    size = models.DecimalField(max_digits=9, decimal_places=1)
    weight = models.DecimalField(max_digits=9, decimal_places=3)
    place = models.CharField(max_length=255)
    date = models.DateTimeField()
    released = models.BooleanField()

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='notebook')


class Boat(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    URLBoat = models.CharField(max_length=255)
    boatLicenseType = models.CharField(max_length=255)
    boatType = models.CharField(max_length=255)
    equipments = models.CharField(max_length=255)
    deposit = models.IntegerField()
    capacity = models.IntegerField()
    bedsNumber = models.IntegerField()
    harbor = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    motor = models.CharField(max_length=255)
    horsepower = models.IntegerField()

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='boatsList')


class DateTimeExcursion(models.Model):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    excursion = models.ForeignKey("fishingdate.Excursion", on_delete=models.CASCADE, related_name='dateTimeList')


class Excursion(models.Model):
    excursionTitle = models.CharField(max_length=255)
    information = models.CharField(max_length=1023)
    excursionType = models.CharField(max_length=255)
    tariff = models.CharField(max_length=255)

    def dateList(self):
        return [{"startDate" : datetime_excursion.startDate, "endDate" : datetime_excursion.endDate} for datetime_excursion in
                self.dateTimeList.all()]

    numberOfPassengers = models.IntegerField()
    excursionPrice = models.DecimalField(max_digits=9, decimal_places=2)
    idBoat = models.IntegerField()

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='fishingExcursionsList')


class Booking(models.Model):
    idExcursion = models.IntegerField()
    date = models.DateTimeField()
    nbBookedSeats = models.IntegerField()
    totalPrice = models.DecimalField(max_digits=9, decimal_places=2)

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='bookingsList')

