from django.db import models


class User(models.Model):
    """
    Represents a user.

    Attributes:
        lastname (str): The user's last name.
        firstname (str): The user's first name.
        birthday (DateTimeField): The user's birthday.
        email (str): The user's email address.
        phone (str): The user's phone number.
        address (str): The user's address.
        zipcode (str): The user's zipcode.
        city (str): The user's city.
        languages (str): The user's spoken languages.
        URLAvatar (str): The URL of the user's avatar.
        boatLicenseNumber (str): The user's boat license number.
        insuranceNumber (str): The user's insurance number.
        status (str): The user's status.
        companyName (str): The user's company name.
        activity (str): The user's activity.
        siretNumber (int): The user's SIRET number.
        tradeRegisterNumber (str): The user's trade register number.
    """
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    URLAvatar = models.CharField(max_length=255)
    boatLicenseNumber = models.CharField(max_length=255, null=True)
    insuranceNumber = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    activity = models.CharField(max_length=1023)
    siretNumber = models.IntegerField(null=True)
    tradeRegisterNumber = models.CharField(max_length=255)

    def boatList(self):
        """
        Returns a list of dictionaries representing the boats owned by the user.
        Each dictionary contains the boat's ID and name.
        """
        return [{"id" : boat.id, "name" : boat.name} for boat in self.boatsList.all()] # type: ignore

    def notebookPageList(self):
        """
        Returns a list of dictionaries representing the notebook pages of the user.
        Each dictionary contains the page's ID and URLFish.
        """
        return [{"id" : page.id, "URLFish" : page.URLFish} for page in self.notebook.all()] # type: ignore

    def excursionList(self):
        """
        Returns a list of dictionaries representing the fishing excursions of the user.
        Each dictionary contains the excursion's ID and excursionTitle.
        """
        return [{"id" : excursion.id, "excursionTitle" : excursion.excursionTitle} for excursion in self.fishingExcursionsList.all()] # type: ignore

    def bookingList(self):
        """
        Returns a list of dictionaries representing the bookings made by the user.
        Each dictionary contains the booking's ID and date.
        """
        return [{"id" : booking.id, "date" : booking.date} for booking in self.bookingsList.all()] # type: ignore


class Notebook(models.Model):
    """
    Represents a notebook entry for fishing data.

    Attributes:
        URLFish (str): The URL of the fish.
        comment (str): A comment about the fishing entry.
        size (Decimal): The size of the fish.
        weight (Decimal): The weight of the fish.
        place (str): The place where the fishing took place.
        date (DateTime): The date and time of the fishing entry.
    """
    URLFish = models.CharField(max_length=255)
    comment = models.CharField(max_length=1023)
    size = models.DecimalField(max_digits=9, decimal_places=1)
    weight = models.DecimalField(max_digits=9, decimal_places=3)
    place = models.CharField(max_length=255)
    date = models.DateTimeField(null=True)
    released = models.BooleanField(null=True)

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='notebook')


class Boat(models.Model):
    """
    Represents a boat.

    Attributes:
        name (str): The name of the boat.
        description (str): The description of the boat.
        brand (str): The brand of the boat.
        year (int): The year the boat was manufactured.
        URLBoat (str): The URL of the boat.
        boatLicenseType (str): The type of boat license required.
        boatType (str): The type of boat.
        equipments (str): The equipment available on the boat.
        deposit (int): The deposit amount for renting the boat.
        capacity (int): The maximum capacity of the boat.
        bedsNumber (int): The number of beds on the boat.
        harbor (str): The harbor where the boat is located.
        longitude (decimal): The longitude coordinate of the boat's location.
        latitude (decimal): The latitude coordinate of the boat's location.
        motor (str): The type of motor on the boat.
        horsepower (int): The horsepower of the boat's motor.
        user (User): The user who owns the boat.
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    brand = models.CharField(max_length=255)
    year = models.IntegerField(null=True)
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
    horsepower = models.IntegerField(null=True)

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='boatsList')


class DateTimeExcursion(models.Model):
    """
    Represents a DateTimeExcursion object that stores the start and end dates of an excursion.
    """

    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    excursion = models.ForeignKey("fishingdate.Excursion", on_delete=models.CASCADE, related_name='dateTimeList')


class Excursion(models.Model):
    """
    Represents an excursion.

    Attributes:
        excursionTitle (str): The title of the excursion.
        information (str): Additional information about the excursion.
        excursionType (str): The type of the excursion.
        tariff (str): The tariff of the excursion.
        numberOfPassengers (int): The number of passengers allowed on the excursion.
        excursionPrice (Decimal): The price of the excursion.
        idBoat (int): The ID of the boat associated with the excursion.
        user (ForeignKey): The user who created the excursion.
    """

    excursionTitle = models.CharField(max_length=255)
    information = models.CharField(max_length=1023)
    excursionType = models.CharField(max_length=255)
    tariff = models.CharField(max_length=255)

    def dateList(self):
        return [{"startDate" : datetime_excursion.startDate, "endDate" : datetime_excursion.endDate} for datetime_excursion in
                self.dateTimeList.all()] # type: ignore

    numberOfPassengers = models.IntegerField()
    excursionPrice = models.DecimalField(max_digits=9, decimal_places=2)
    idBoat = models.IntegerField()

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='fishingExcursionsList')


class Booking(models.Model):
    """
    Represents a booking for an excursion.

    Attributes:
        idExcursion (int): The ID of the excursion.
        date (DateTimeField): The date and time of the booking.
        nbBookedSeats (int): The number of seats booked.
        totalPrice (DecimalField): The total price of the booking.
        user (ForeignKey): The user who made the booking.
    """
    idExcursion = models.IntegerField()
    date = models.DateTimeField()
    nbBookedSeats = models.IntegerField()
    totalPrice = models.DecimalField(max_digits=9, decimal_places=2)

    user = models.ForeignKey('fishingdate.User', on_delete=models.CASCADE, related_name='bookingsList')

