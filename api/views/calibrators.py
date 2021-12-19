from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied 
from ..serializers.calibrator import CalibratorSerializer
from ..models.calibrator import Calibrator

class CalibratorsView(APIView):
    def post(self, request):
        # Add the user id as owner
        request.data['owner'] = request.user.id
        calibrator = CalibratorSerializer(data=request.data)
        if calibrator.is_valid():
            calibrator.save()
            return Response(calibrator.data, status=status.HTTP_201_CREATED)
        else:
            return Response(calibrator.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        # filter for mangos with our user id
        calibrators = Calibrator.objects.filter(owner=request.user.id)
        data = CalibratorSerializer(calibrators, many=True).data
        return Response(data)

class CalibratorView(APIView):
    def delete(self, request, pk):
        calibrator = get_object_or_404(Calibrator, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != calibrator.owner:
            raise PermissionDenied('Unauthorized, you do not own this calibrator')
        calibrator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        calibrator = get_object_or_404(Calibrator, pk=pk)
        if request.user != calibrator.owner:
            raise PermissionDenied('Unauthorized, you do not own this calibrator')
        data = CalibratorSerializer(calibrator).data
        return Response(data)
    
    def patch(self, request, pk):
        calibrator = get_object_or_404(Calibrator, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != calibrator.owner:
            raise PermissionDenied('Unauthorized, you do not own this calibrator')
        # Ensure the owner field is set to the current user's ID
        request.data['owner'] = request.user.id
        updated_calibrator = CalibratorSerializer(calibrator, data=request.data, partial=True)
        if updated_calibrator.is_valid():
            updated_calibrator.save()
            return Response(updated_calibrator.data)
        return Response(updated_calibrator.errors, status=status.HTTP_400_BAD_REQUEST)