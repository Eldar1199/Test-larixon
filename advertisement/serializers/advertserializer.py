from rest_framework import serializers
from advertisement.models.advert import Advert




class AdvertSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Advert
        fields = ['id', 'created', 'title', 'desc', 'city_name', 'category_name', 'views']