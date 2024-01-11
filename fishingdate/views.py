from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Notebook, Boat, Excursion, Booking, DateTimeExcursion
from .serializers import UserSerializer, NotebookSerializer, BoatSerializer, ExcursionSerializer, BookingSerializer, DateTimeExcursionSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class BoatViewSet(viewsets.ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer
    permission_classes = [IsAuthenticated]


class ExcursionViewSet(viewsets.ModelViewSet):
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    permission_classes = [IsAuthenticated]

class DateTimeListViewSet(viewsets.ModelViewSet):
    queryset = DateTimeExcursion.objects.all()
    serializer_class = DateTimeExcursionSerializer
    permission_classes = [IsAuthenticated]