from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied 
from ..serializers.consumable import ConsumableSerializer
from ..models.consumable import Consumable

class ConsumablesView(APIView):
    def post(self, request):
        # Add the user id as owner
        request.data['owner'] = request.user.id
        consumable = ConsumableSerializer(data=request.data)
        if consumable.is_valid():
            consumable.save()
            return Response(consumable.data, status=status.HTTP_201_CREATED)
        else:
            return Response(consumable.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        # filter for mangos with our user id
        consumables = Consumable.objects.filter(owner=request.user.id)
        data = ConsumableSerializer(consumables, many=True).data
        return Response(data)

class ConsumableView(APIView):
    def delete(self, request, pk):
        consumable = get_object_or_404(Consumable, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != consumable.owner:
            raise PermissionDenied('Unauthorized, you do not own this consumable')
        consumable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        consumable = get_object_or_404(Consumable, pk=pk)
        if request.user != consumable.owner:
            raise PermissionDenied('Unauthorized, you do not own this consumable')
        data = ConsumableSerializer(consumable).data
        return Response(data)
    
    def patch(self, request, pk):
        consumable = get_object_or_404(Consumable, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != consumable.owner:
            raise PermissionDenied('Unauthorized, you do not own this consumable')
        # Ensure the owner field is set to the current user's ID
        request.data['owner'] = request.user.id
        updated_consumable = ConsumableSerializer(consumable, data=request.data, partial=True)
        if updated_consumable.is_valid():
            updated_consumable.save()
            return Response(updated_consumable.data)
        return Response(updated_consumable.errors, status=status.HTTP_400_BAD_REQUEST)