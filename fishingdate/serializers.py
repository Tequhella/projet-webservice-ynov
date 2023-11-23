from rest_framework.serializers import ModelSerializer

from fishingdate.models import User, Notebook, Boat, Excursion, Booking


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'lastname',
            'firstname',
            'birthday',
            'email',
            'phone',
            'address',
            'zipcode',
            'city',
            'languages',
            'URLAvatar',
            'boatLicenseNumber',
            'insuranceNumber',
            'status',
            'companyName',
            'activity',
            'siretNumber',
            'tradeRegisterNumber'
        ]


class NotebookSerializer(ModelSerializer):

    class Meta:
        model = Notebook
        fields = [
            'id',
            'URLFish',
            'comment',
            'size',
            'weight',
            'place',
            'date',
            'released',
            'user'
        ]


class BoatSerializer(ModelSerializer):

    class Meta:
        model = Boat
        fields = [
            'id',
            'name',
            'description',
            'brand',
            'year',
            'URLBoat',
            'boatLicenseType',
            'boatType',
            'equipments',
            'deposit',
            'capacity',
            'bedsNumber',
            'harbor',
            'longitude',
            'latitude',
            'motor',
            'horsepower',
            'user'
        ]


class ExcursionSerializer(ModelSerializer):

    class Meta:
        model = Excursion
        fields = [
            'id',
            'excursionTitle',
            'information',
            'excursionType',
            'tariff',
            'date_time_list',
            'numberOfPassengers',
            'excursionPrice',
            'idOwner',
            'idBoat',
            'user'
        ]


class BookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = [
            'idBooking',
            'idExcursion',
            'date',
            'nbBookedSeats',
            'totalPrice',
            'idBooker',
            'user'
        ]
