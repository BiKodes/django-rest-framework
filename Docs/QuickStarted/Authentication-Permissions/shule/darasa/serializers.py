from rest_framework import serializers
from .models import Darasa, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class DarasaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = Darasa
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.ModelSerializer):
    darasas = serializers.PrimaryKeyRelatedField(many = True, queryset = Darasa.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'darasas']
