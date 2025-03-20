from django.contrib import admin
from .models.advert import Advert
from .models.category import AdvertCategory
from .models.city import AdvertCity

admin.site.register([Advert, AdvertCity, AdvertCategory])