from rest_framework import serializers
from products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='name', max_length=50)
    price = serializers.IntegerField(source='price')
    count = serializers.IntegerField(source='count')
    class Meta:
        model = Products
        fields = '__all__'