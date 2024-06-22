from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


class HelloAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data='Hello', status=status.HTTP_200_OK)