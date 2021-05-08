
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

class CarModel(models.Model):
    name = models.CharField(max_length=255)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='content_types',)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name


class Sony(models.Model):
    name = models.CharField(max_length=255)
    carmodels = models.ForeignKey(CarModel, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Pioneer(models.Model):
    name = models.CharField(max_length=255)
    carmodels = models.ForeignKey(CarModel, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.name
