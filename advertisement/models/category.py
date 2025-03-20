from django.db import models




class AdvertCategory(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length = 50)



    def __str__(self) -> str:
        return self.name