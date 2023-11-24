from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from .seriallizers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status


class signin(APIView):
    def post(self, request):
        if authenticate(username=request.data['username'], email=request.data['email'],
                        password=request.data['password']) is not None:
            return Response({"message": "access granted"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Username or password invalid"}, status=status.HTTP_400_BAD_REQUEST)


class signup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=request.data['username'],
                                            password=request.data['password'],
                                            email=request.data['email'])
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        us = User.objects.all()
        data = UserSerializer(us, many=True).data
        return Response(data)
