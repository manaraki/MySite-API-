from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import UserRegisterSerializer, UserSerializer


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            validated_data = ser_data.validated_data
            UserRegisterSerializer.create(ser_data, validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    """
        A viewset for viewing and editing user instances.
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = Student.objects.all()

    def list(self, request):
        ser_data = self.serializer_class(instance=self.queryset, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = self.serializer_class(instance=user)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = self.serializer_class(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        # deactivating user
        user.is_active = False
        user.save()
        return Response({'message': 'user deactivated'}, status=status.HTTP_200_OK)
