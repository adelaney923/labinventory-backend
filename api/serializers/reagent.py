from rest_framework import serializers
from ..models.reagent import Reagent

class ReagentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reagent
        fields = ('id', 'description', 'storage_temp', 'reference_num', 'part_number', 'unit_of_measure', 'quantity','lot_number', 'expiration_date', 'comments', 'owner')