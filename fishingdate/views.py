from multiprocessing.managers import BaseManager
import numbers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User, Notebook, Boat, Excursion, Booking, DateTimeExcursion
from .serializers import UserSerializer, NotebookSerializer, BoatSerializer, ExcursionSerializer, BookingSerializer, DateTimeExcursionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing user data.

    This viewset provides CRUD operations for User objects.
    It also supports filtering by zipcode.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for User objects.
        permission_classes (list): The list of permission classes for this viewset.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Get the queryset of User objects.

        Returns:
            QuerySet: The queryset of User objects.
        """
        queryset = User.objects.all()
        zipcode = self.request.GET.get('zipcode')
        if zipcode is not None:
            queryset = queryset.filter(zipcode=zipcode)
        
        return queryset

    permission_classes = [IsAuthenticated]


class BoatViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing boats.

    This ViewSet provides CRUD operations for boats, including filtering by name, longitude, and latitude.
    Only authenticated users are allowed to access this ViewSet.

    Attributes:
        queryset (QuerySet): The queryset of all boats.
        serializer_class (Serializer): The serializer class for boats.

    Methods:
        get_queryset: Retrieves the queryset of boats, with optional filtering by name, longitude, and latitude.
        create: Creates a new boat, with validation to ensure the owner has a boat license number.

    """
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer

    def get_queryset(self):
        """
        Retrieves the queryset of boats, with optional filtering by name, longitude, and latitude.

        Returns:
            QuerySet: The filtered queryset of boats.

        """
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
    
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Creates a new boat, with validation to ensure the owner has a boat license number.

        Args:
            request (Request): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object.

        """
        owner_id = request.data.get('user')
        try:
            user = User.objects.get(pk=owner_id)
            if user.boatLicenseNumber is None:
                return Response(
                    {'error': 'User must have a boat License number to create an boat.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except User.DoesNotExist:
            return Response(
                {'error': 'User with provided ID does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)
    

class ExcursionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing excursions.

    This ViewSet provides CRUD operations for the Excursion model.
    It allows filtering excursions by excursionType and requires authentication for all operations.
    """

    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer

    def get_queryset(self):
        """
        Get the queryset of excursions.

        If the 'excursionType' parameter is provided in the request, filter the queryset by excursionType.

        Returns:
            queryset: The filtered queryset of excursions.
        """
        queryset = Excursion.objects.all()
        excursionType = self.request.GET.get('excursionType')
        if excursionType is not None:
            queryset = queryset.filter(excursionType=excursionType)
        return queryset
    
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Create a new excursion.

        Check if the user has at least one boat before creating the excursion.

        Args:
            request: The request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The response object.
        """
        boat_owner_id = request.data.get('user')
        try:
            user = User.objects.get(pk=boat_owner_id)
            if not user.boatsList.exists():
                return Response(
                    {'error': 'User must have at least one boat to create an excursion.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except User.DoesNotExist:
            return Response(
                {'error': 'User with provided ID does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)
    

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing bookings.

    Attributes:
        queryset (QuerySet): The queryset of all bookings.
        serializer_class (Serializer): The serializer class for bookings.
        permission_classes (list): The list of permission classes for accessing bookings.
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        """
        Get the filtered queryset of bookings.

        Returns:
            QuerySet: The filtered queryset of bookings.
        """
        queryset = Booking.objects.all()
        idExcursion = self.request.GET.get('idExcursion')
        if idExcursion is not None:
            queryset = queryset.filter(idExcursion=idExcursion)
        return queryset
    
    permission_classes = [IsAuthenticated]


class NotebookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Notebooks.

    This ViewSet provides CRUD operations for Notebooks.
    """

    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

    def get_queryset(self):
        """
        Get the queryset for Notebooks.

        This method filters the queryset based on the 'weight' parameter in the request.

        Returns:
            queryset (QuerySet): The filtered queryset of Notebooks.
        """
        queryset = Notebook.objects.all()
        weight = self.request.GET.get('weight')
        if weight is not None:
            queryset = queryset.filter(weight=weight)
        return queryset
    
    permission_classes = [IsAuthenticated]


class DateTimeListViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing date and time excursions.

    This viewset provides CRUD operations for the DateTimeExcursion model.
    Only authenticated users are allowed to access these endpoints.
    """
    queryset = DateTimeExcursion.objects.all()
    serializer_class = DateTimeExcursionSerializer
    permission_classes = [IsAuthenticated]
