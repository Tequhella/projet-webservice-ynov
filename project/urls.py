from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from fishingdate.views import NotebookViewSet, UserViewSet, BoatViewSet, ExcursionViewSet, BookingViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('notebook', NotebookViewSet, basename='notebook')
router.register('user', UserViewSet, basename='user')
router.register('boat', BoatViewSet, basename='boat')
router.register('excursion', ExcursionViewSet, basename='excursion')
router.register('booking', BookingViewSet, basename='booking')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls)),
]