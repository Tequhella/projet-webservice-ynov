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
        longitude1 = self.request.GET.get('longitude1')
        longitude2 = self.request.GET.get('longitude2')
        latitude1 = self.request.GET.get('latitude1')
        latitude2 = self.request.GET.get('latitude2')
        if longitude1 is not None and longitude2 is not None and latitude1 is not None and latitude2 is not None :
            queryset = queryset.filter(longitude__range=(longitude1, longitude2))
            queryset = queryset.filter(latitude__range=(latitude1, latitude2))
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