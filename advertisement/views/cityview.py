from rest_framework.viewsets import ModelViewSet
from advertisement.models.city import AdvertCity
from advertisement.serializers.cityserializer import CitySerializer


class CityViewSet(ModelViewSet):
    queryset = AdvertCity.objects.all()
    serializer_class = CitySerializer