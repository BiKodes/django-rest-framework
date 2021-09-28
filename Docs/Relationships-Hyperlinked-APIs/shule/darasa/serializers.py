from rest_framework import serializers
from .models import Darasa, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class DarasaSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serialiazers.HyperlinkedIdentityField(view_name='darasa-highlight', format='html')

    class Meta:
        model = Darasa
        fields = ['url','id', 'highlight','title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    darasas = serializers.HyperlinkedRelatedField(many = True, view_name='darasa-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url','id', 'username', 'darasas']
