from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied 
from ..serializers.control import ControlSerializer
from ..models.control import Control

class ControlsView(APIView):
    def post(self, request):
        # Add the user id as owner
        request.data['owner'] = request.user.id
        control = ControlSerializer(data=request.data)
        if control.is_valid():
            control.save()
            return Response(control.data, status=status.HTTP_201_CREATED)
        else:
            return Response(control.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        # filter for mangos with our user id
        controls = Control.objects.filter(owner=request.user.id)
        data = ControlSerializer(controls, many=True).data
        return Response(data)

class ControlView(APIView):
    def delete(self, request, pk):
        control = get_object_or_404(Control, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != control.owner:
            raise PermissionDenied('Unauthorized, you do not own this control')
        control.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        control = get_object_or_404(Control, pk=pk)
        if request.user != control.owner:
            raise PermissionDenied('Unauthorized, you do not own this control')
        data = ControlSerializer(control).data
        return Response(data)
    
    def patch(self, request, pk):
        control = get_object_or_404(Control, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != control.owner:
            raise PermissionDenied('Unauthorized, you do not own this control')
        # Ensure the owner field is set to the current user's ID
        request.data['owner'] = request.user.id
        updated_control = ControlSerializer(control, data=request.data, partial=True)
        if updated_control.is_valid():
            updated_control.save()
            return Response(updated_control.data)
        return Response(updated_control.errors, status=status.HTTP_400_BAD_REQUEST)