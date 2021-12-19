from rest_framework import serializers
from ..models.consumable import Consumable

class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumable
        fields = ('id', 'description', 'storage_temp', 'reference_num', 'part_number', 'unit_of_measure', 'quantity','lot_number', 'expiration_date', 'comments', 'owner')