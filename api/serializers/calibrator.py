from rest_framework import serializers
from ..models.calibrator import Calibrator

class CalibratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibrator
        fields = ('id', 'description', 'storage_temp', 'reference_num', 'part_number', 'unit_of_measure', 'quantity','lot_number', 'expiration_date', 'comments', 'owner')