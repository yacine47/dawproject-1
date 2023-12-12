from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .seriallizers import UserSerializer, UserLoginSerializer, UserMoreInfoSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from rest_framework import status


class signin(APIView):
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.check_user(data)
            login(request, user)

            return Response({"message": "access granted", }, status=status.HTTP_201_CREATED)

        return Response({"message": "Username or password invalid"}, status=status.HTTP_400_BAD_REQUEST)


class signup(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializerlogin = UserLoginSerializer(data=request)
        if serializer.is_valid():
            User.objects.create_user(username=request.data['username'],
                                     password=request.data['password'],
                                     email=request.data['email'],
                                     )
            user = serializerlogin.check_user(request.data)
            login(request, user)

            return Response(
                {"message": "User created successfully ,access granted"},
                status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class signout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class userinfo(APIView):
    def get(self, request):
        if request.session:
            user = UserSerializer(request.user)
            return Response({'user': user.data}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class moreinfo(APIView):
    def post(self, request):
        provided_id = request.data.get('id')  # Assuming the 'id' is provided in the request data
        try:
            user_instance = User.objects.get(id=provided_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        userinfoserializer = UserMoreInfoSerializer(user_instance,data=request.data,partial=True)
        if userinfoserializer.is_valid():
            userinfoserializer.save()
            return Response(userinfoserializer.data, status=status.HTTP_201_CREATED)
        return Response(userinfoserializer.errors, status=status.HTTP_400_BAD_REQUEST)

