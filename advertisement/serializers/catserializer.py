from rest_framework import serializers
from advertisement.models.category import AdvertCategory




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertCategory
        fields = '__all__'
        