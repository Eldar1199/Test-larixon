from rest_framework.viewsets import ModelViewSet
from advertisement.models.advert import Advert
from advertisement.serializers.advertserializer import AdvertSerializer



class AdvertViewSet(ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


    def get_object(self):
        advert = super().get_object()
        advert.views += 1
        advert.save()
        return advert