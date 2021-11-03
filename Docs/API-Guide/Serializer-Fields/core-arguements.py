# If the callable has a requires_context = True attribute, then the serializer field will 
# be passed as an argument.

class CurrentUserDefault:
    """
    May be applied as a `default=...` value on a serializer field.
    Returns the current user.
    """

    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user

    # style

    password = serializers.CharField(
        style = {
            'input_type': 'password'
        }
    )
    
    color_channel = serializers.ChoiceField(
        choices = ['red', 'green', 'blue'],
        style = {
            'base_template': 'radio.html'
        }
    )
