from rest_framework import serializers
from languages.models import Language
class LanguagesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = Language
        fields = '__all__'