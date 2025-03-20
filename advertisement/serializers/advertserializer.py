from rest_framework import serializers
from advertisement.models.advert import Advert




class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = '__all__'