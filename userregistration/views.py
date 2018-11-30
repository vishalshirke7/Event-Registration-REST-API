from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, views, generics, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import User


class UserRegistration(APIView):

    serializer_class = UserRegistrationSerializer

    def get(self, request, format=None):

        users = User.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):

    serializer_class = UserLoginSerializer

    def get(self, request, format=None):
        if 'user_id' in request.session:
            data = {"Logged-In": "Already Logged In"}
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            request.session['user_id'] = serializer.validated_data["user_id"]
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):

    def get(self, request, format=None):
        if 'user_id' in request.session:
            del request.session['user_id']
            data = {'Logout': 'logged out successfully'}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'Logout': 'Already logged out!'}
            return Response(data, status=status.HTTP_200_OK)

