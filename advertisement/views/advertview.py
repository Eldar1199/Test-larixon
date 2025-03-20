from rest_framework.viewsets import ModelViewSet
from advertisement.models.advert import Advert
from advertisement.serializers.advertserializer import AdvertSerializer



class AdvertViewSet(ModelViewSet):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer


    def get_object(self):
        advert = super().get_object()
        print('hello')
        Advert.objects.filter(id=advert.id).update(views=advert.views + 1)
        print('hello1')
        return advert