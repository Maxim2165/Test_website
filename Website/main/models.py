from django.db import models


class recipes(models.Model):
    name_category = models.CharField(max_length=25, blank=False)
    name_pecipe = models.CharField(max_length=150, blank=True)
    description_recept = models.CharField(max_length=1500, blank=True)
    cooking_time = models.IntegerField(default=0, blank=True)
    cooking_process = models.CharField(max_length=3500, blank=True)
    ingredients = models.CharField(max_length=1500, blank=True)
    image = models.BinaryField()
