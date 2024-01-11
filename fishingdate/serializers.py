from rest_framework.serializers import ModelSerializer

from fishingdate.models import User, Notebook, Boat, Excursion, Booking, DateTimeExcursion


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
            'tradeRegisterNumber',
            'boatList',
            'notebookPageList',
            'excursionList',
            'bookingList'
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
            'dateList',
            'numberOfPassengers',
            'excursionPrice',
            'idBoat',
            'user'
        ]


class BookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = [
            'id',
            'idExcursion',
            'date',
            'nbBookedSeats',
            'totalPrice',
            'user'
        ]


class DateTimeExcursionSerializer(ModelSerializer):

    class Meta:
        model = DateTimeExcursion
        fields = [
            'startDate',
            'endDate'
        ]
