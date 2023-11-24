from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .seriallizers import UserSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status


class signin(APIView):
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.check_user(data)
            login(request, user)
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


class signout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
