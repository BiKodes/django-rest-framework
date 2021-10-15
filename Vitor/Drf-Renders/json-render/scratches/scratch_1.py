from rest_framework import serializers

from unittest.mock import Mock

class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(allow_blank=True)
    last_name = serializers.CharField(allow_blank=True)
    birthdate = serializers.DateField()
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        delta = date.today() - obj.birthdate
        return int(delta.days / 365)

    def validate_birthdate(self, value):
        if value > date.today():
            raise serializers.ValidationError("The birthdate must be a date before today.")
        return value

    def validate(self, data):
        if not data["first_name"] and not data["last_name"]:
            raise serializers.ValidationError("You must inform either the first name or last name.")
        return data
        


class Person:
    def __init__(self, first_name, birthdate):
        self.first_name = first_name
        self.birthdate = birthdate


Mock()