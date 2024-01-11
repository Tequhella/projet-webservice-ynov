from multiprocessing.managers import BaseManager
import numbers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Notebook, Boat, Excursion, Booking, DateTimeExcursion
from .serializers import UserSerializer, NotebookSerializer, BoatSerializer, ExcursionSerializer, BookingSerializer, DateTimeExcursionSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        zipcode = self.request.GET.get('zipcode')
        if zipcode is not None:
            queryset = queryset.filter(zipcode=zipcode)
        return queryset

    #permission_classes = [IsAuthenticated]


class BoatViewSet(viewsets.ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer

    def get_queryset(self):
        queryset = Boat.objects.all()
        name = self.request.GET.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
    
    #permission_classes = [IsAuthenticated]


class ExcursionViewSet(viewsets.ModelViewSet):
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer

    def get_queryset(self):
        queryset = Excursion.objects.all()
        excursionType = self.request.GET.get('excursionType')
        if excursionType is not None:
            queryset = queryset.filter(excursionType=excursionType)
        return queryset
    
    #permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        idExcursion = self.request.GET.get('idExcursion')
        if idExcursion is not None:
            queryset = queryset.filter(idExcursion=idExcursion)
        return queryset
    
    #permission_classes = [IsAuthenticated]

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

    def get_queryset(self):
        queryset = Notebook.objects.all()
        weight = self.request.GET.get('weight')
        if weight is not None:
            queryset = queryset.filter(weight=weight)
        return queryset
    
    #permission_classes = [IsAuthenticated]

class DateTimeListViewSet(viewsets.ModelViewSet):
    queryset = DateTimeExcursion.objects.all()
    serializer_class = DateTimeExcursionSerializer
    #permission_classes = [IsAuthenticated]