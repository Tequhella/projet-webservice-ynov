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
    path('api/v1/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/v1/', include(router.urls)),
]

"""
Django URL Configuration
This file defines the URL patterns for the project.
It includes the necessary imports and sets up the router for API endpoints.
The urlpatterns list contains the paths for various URLs, including admin, authentication, and API endpoints.
Each path is associated with a specific view or viewset.

TokenObtainPairView:
This view is used to obtain a JSON Web Token (JWT) pair, consisting of an access token and a refresh token.
The access token is used for authenticating API requests, while the refresh token is used to obtain a new access token when the current one expires.

TokenRefreshView:
This view is used to refresh an expired access token by providing a valid refresh token.
Refreshing the token generates a new access token, allowing the user to continue making authenticated requests without having to re-authenticate.

These token functionalities provide a secure way to authenticate and authorize users in the API endpoints.

The router registers the viewsets for the API endpoints.
"""
