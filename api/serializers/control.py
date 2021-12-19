from rest_framework import serializers
from ..models.control import Control

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('id', 'description', 'storage_temp', 'reference_num', 'part_number', 'unit_of_measure', 'quantity','lot_number', 'expiration_date', 'comments', 'owner')