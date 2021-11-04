# A Basic Custom Field

class Color:
    """
    A color represented in the RGB colorspace.
    """

    def __init__(self, red, green, blue):
        assert(red >= 0 and green >= 0 and blue >= 0)
        assert(red < 256 and green < 256 and blue < 256)
        self.red, self.green, self.blue = red, green, blue

class ColorField(serializers.Field):
    """
    Color objects are serialized into 'rgb(#, #, #)' notation.
    """

    def to_representation(self, value):
        return "rgb(%d, %d, %d)" % (value.red, value.green, value.blue)

    def to_internal_value(self, data):
        data = data.strip('rgb(').rstrip(')')
        red, green, blue = [int(col) for col in data.split(',')]
        return Color(red, green, blue)


class ClassNameField(serializers.Field):

    def get_attribute(Self, instance):
        # We pass the object instance onto `to_representation`,
        # not just the field attribute.

        return instance

    def to_representation(self, value):
        """
        Serialize the value's class name.
        """
        return value.__class__.__name__

# Raising validation errors

class ColorField(serializers.Field):
    
    def to_internal_value(self, data):
        if not isinstance(data, str):
            msg = 'Incorrect type. Expected a string, but got %s'
            raise ValidationError(msg % type(data).__name__)

        if not re.match(r'^rgb\([0-9]+,[0-9]+,[0-9]+\)$', data):
            raise ValidationError('Incorrect format. Expected `rgb(#,#,#)`.')

        data = data.strip('rgb(').rstrip(')')
        red, green, blue = [int(col) for col in data.split(',')]

        if any([col > 255 or col < 0 for col in (red, green, blue)]):
            raise ValidationError('Value out of range. Must be between 0 and 255.')

        return Color(red, green, blue)

# The .fail() method is a shortcut for raising ValidationError that takes a message string 
# from the error_messages dictionary. 

class ColorField(serializers.Field):

    default_error_messages = {
        'incorrect_type': 'Incorrect type. Expected a string, but got {input_type}',
        'incorrect_format': 'Incorrect format. Expected `rgb(#,#,#)`.',
        'out_of_range': 'Value out of range. Must be between 0 and 255.'
    }

    def to_internal_value(self, data):
        if not isinstance(data, str):
            self.fail('incorrect_type', input_type=type(data).__name__)

        if not re.match(r'^rgb\([0-9]+,[0-9]+,[0-9]+\)$', data):
            self.fail('incorrect_format')

        data = data.strip('rgb(').rstrip(')')
        red, green, blue = [int(col) for col in data.split(',')]

        if any([col > 255 or col < 0 for col in (red, green, blue)]):
            self.fail('out_of_range')

        return Color(red, green, blue)


