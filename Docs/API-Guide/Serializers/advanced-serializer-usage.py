# Overriding serialization and deserialization behavior

def to_representation(self, instance):
    """Convert `username` to lowercase."""

    ret = super().to_representation(instance)
    ret['username'] = ret['username'].lower()
    return ret

# Serializer Inheritance

class MyBaseSerializer(Serializer):
    my_field = serializers.CharField()

    def validate_my_field(self, value):
        pass

class MySerializer(MyBaseSerializer):
    pass

# Meta class to inherit from a parent class 

class AccountSerializer(MyBaseSerializer):
    class Meta(MyBaseSerializer.Meta):
        model = Account

# Dynamically modifying fields
# setting which fields should be used by a serializer at the point of initializing it

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)

            for field_name in existing - allowed:
                self.fields.pop(field_name)