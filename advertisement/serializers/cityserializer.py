from rest_framework import serializers
from advertisement.models.city import AdvertCity



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertCity
        fields = '__all__'