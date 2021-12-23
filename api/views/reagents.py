from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied 
from ..serializers.reagent import ReagentSerializer
from ..models.reagent import Reagent

class ReagentsView(APIView):
    def post(self, request):
        # Add the user id as owner
        request.data['owner'] = request.user.id
        reagent = ReagentSerializer(data=request.data)
        if reagent.is_valid():
            reagent.save()
            return Response(reagent.data, status=status.HTTP_201_CREATED)
        else:
            return Response(reagent.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        # filter for mangos with our user id
        reagents = Reagent.objects.filter(owner=request.user.id)
        data = ReagentSerializer(reagents, many=True).data
        return Response(data)

class ReagentView(APIView):
    def delete(self, request, pk):
        reagent = get_object_or_404(Reagent, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != reagent.owner:
            raise PermissionDenied('Unauthorized, you do not own this reagent')
        reagent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        reagent = get_object_or_404(Reagent, pk=pk)
        if request.user != reagent.owner:
            raise PermissionDenied('Unauthorized, you do not own this reagent')
        data = ReagentSerializer(reagent).data
        return Response(data)
    
    def put(self, request, pk):
        reagent = get_object_or_404(Reagent, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != reagent.owner:
            raise PermissionDenied('Unauthorized, you do not own this reagent')
        # Ensure the owner field is set to the current user's ID
        request.data['owner'] = request.user.id
        updated_reagent = ReagentSerializer(reagent, data=request.data)
        if updated_reagent.is_valid():
            updated_reagent.save()
            return Response(updated_reagent.data)
        return Response(updated_reagent.errors, status=status.HTTP_400_BAD_REQUEST)