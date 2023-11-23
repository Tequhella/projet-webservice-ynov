from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from fishingdate.views import NotebookViewSet, UserViewSet, BoatViewSet, ExcursionViewSet, BookingViewSet

router = routers.SimpleRouter()
router.register('notebook', NotebookViewSet, basename='notebook')
router.register('user', UserViewSet, basename='user')
router.register('boat', BoatViewSet, basename='boat')
router.register('excursion', ExcursionViewSet, basename='excursion')
router.register('booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
