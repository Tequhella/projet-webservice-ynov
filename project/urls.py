# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fishingdate.views import NotebookViewSet

router = DefaultRouter()
router.register(r'notebooks', NotebookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]