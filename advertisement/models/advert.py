from django.db import models
from .category import AdvertCategory
from .city import AdvertCity

class Advert(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Идентификатор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    desc = models.TextField(verbose_name='Описание', max_length=255)
    city = models.ForeignKey(AdvertCity, on_delete=models.CASCADE, verbose_name='Город')
    category = models.ForeignKey(AdvertCategory, on_delete=models.CASCADE, verbose_name='Категория')
    views = models.PositiveIntegerField(default=0, verbose_name='Счетчик просмотров')


    def __str__(self) -> str:
        return self.title