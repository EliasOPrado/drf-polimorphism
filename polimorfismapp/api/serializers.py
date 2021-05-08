import json
from rest_framework import serializers
from polimorfismapp.models import CarModel, Sony, Pioneer




class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = [
            'name',
            'object_id',
            'content_object',
            'content_type'
        ]

class CarModelObjectRelatedField(serializers.RelatedField):
    """
    Serialize bookmark instances using a bookmark serializer.
    """

    def to_representation(self, value):
        if isinstance(value, CarModel):
            serializer =CarModelSerializer(value)
            print('SERIALIZER ==>', serializer.data)
        # elif isinstance(value, Pioneer):
        #     serializer = PioneerSerializer(value)
            return serializer.data

class SonySerializer(serializers.HyperlinkedModelSerializer):

    carmodels = CarModelObjectRelatedField(read_only=True)

    class Meta:
        model = Sony
        fields = [
            'name',
            'carmodels'
            ]

class PioneerSerializer(serializers.HyperlinkedModelSerializer):

    carmodels = CarModelObjectRelatedField(read_only=True)

    class Meta:
        model = Pioneer
        fields = [
            'name',
            'carmodels'
            ]
