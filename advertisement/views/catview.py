from rest_framework.viewsets import ModelViewSet
from advertisement.models.category import AdvertCategory
from advertisement.serializers.catserializer import CategorySerializer



class CategoryViewSet(ModelViewSet):
    queryset = AdvertCategory.objects.all()
    serializer_class = CategorySerializer