from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from books.serializers import BookSerializer
from books.models import Book
from rest_framework.decorators import api_view

# Create your views here.
# @api_view(['GET', 'POST'])
# def books_list(request):
#     if request.method == 'GET':
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class BookList(ListAPIView):
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, fotmat=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, namy =True)
        return Response(serializer.data)