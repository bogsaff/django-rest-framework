from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    year = serializers.IntegerField()
    pages = serializers.IntegerField(required=True)

    class Meta:
        model = Book
        fields = '__all__'