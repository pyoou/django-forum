from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        register_serializer = RegisterUserSerializer(data=request.data)
        if register_serializer.is_valid():
            newuser = register_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
