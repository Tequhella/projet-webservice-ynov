from rest_framework.serializers import ModelSerializer

from fishingdate.models import User, Notebook, Boat, Excursion, Booking


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'lastname', 'firstname', 'birthday', 'email', 'phone', 'address', 'zipcode', 'city', 'languages', 'url',
                  'boatLicenseNumber', 'insuranceNumber', 'status', 'companyName', 'activity', 'siretNumber', 'tradeRegisterNumber']

class NotebookSerializer(ModelSerializer):

    class Meta:
        model = Notebook
        fields = ['id', 'url', 'comment', 'size', 'weight', 'place', 'date', 'released', 'user']

class BoatSerializer(ModelSerializer):

    class Meta:
        model = Boat
        fields = ['id', 'name', 'description', 'brand', 'fabrication_year', 'url_boat_photo', 'boat_license_type', 'boatType', 'equipments',
                  'deposit', 'capacity', 'bedsNumber', 'harbor', 'longitude', 'latitude', 'motor', 'horsepower', 'user']

class ExcursionSerializer(ModelSerializer):

    class Meta:
        model = Excursion
        fields = ['id', 'title', 'information', 'excursion_yype', 'tariff', 'date_time_list', 'number_of_passengers', 'excursion_price',
                  'id_owner', 'id_boat', 'user']

class BookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id', 'id_excursion', 'date', 'nb_booked_seats', 'total_price', 'id_booker', 'user']