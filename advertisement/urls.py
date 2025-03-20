from django.urls import path, include
from rest_framework.routers import DefaultRouter
from advertisement.views.advertview import AdvertViewSet


router = DefaultRouter()
router.register(r'advert', AdvertViewSet, basename='advert')



urlpatterns = [
    path('', include(router.urls)),
]