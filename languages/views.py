

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from languages.models import Language
from rest_framework.decorators import api_view
from languages.serializers import LanguagesSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def language_list(request):
    if request.method == 'GET':
        languages = Language.objects.all()
        serializer = LanguagesSerializer(languages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LanguagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)