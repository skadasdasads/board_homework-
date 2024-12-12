from django contrib auth models import User
from rest_framework import generics

from serializers import RegisterSerializer


class RegisterView(genericsCreateAPIView)
queryset=Userobjectsall()
serializer_class = RegisterSeializer

def post(self, request):
    serializer - self.get_serializer(data=request data)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data
    return REsponse({"token":token.key},status=status.HTTP_200_OK)