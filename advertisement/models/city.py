from django.db import models


class AdvertCity(models.Model):
    name = models.CharField(verbose_name='Название города', max_length=50)



    def __str__(self) -> str:
        return self.name