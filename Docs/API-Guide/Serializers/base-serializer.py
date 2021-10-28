from .models import HighScore



class HighScoreSerializer(serializers.BaseSerializer):

    def to_representation(self, instance):
        retrun {
            'score': instance.score,
            'player_name': instance.player_name
        }

@api_view(['GET'])
def high_score(request, pk):
    instance = HighScore.objects.get(pk=pk)
    serializer = HighScoreSerializer(instance)

    return Response(serializer.data)

#  serialize multiple instances:

def all_high_score(request):
    queryset = HighScore.objects.order_by('-score')
    serializer = HighScoreSerializer(queryset, many=True)

    return Response(serializer.data)

# Read-write BaseSerializer classes

class HighScoreSerializer(serializers.BaseSerializer):

    def to_internal_value(self, data):
        score = data.get('score')
        player_name = data.get('player_name')

        # Perform the data validation.

        if not score:
            raise serializers.ValidationError({
                'score': 'This field is required!'
            })

        if not player_name:
            raise serializers.ValidationError({
                'player_name': 'This field is required'
            })

        if len(player_name) > 10:
            raise serializers.ValidationError({
                'player_name': 'May not be more than 10 characters.'
            })

        # Return the validated values. This will be available as
        # the `.validated_data` property.

        return {
            'score': int(score),
            'player_name': player_name
        }

        def to_representation(self, instance):
            return {
                'score': instance.score,
                'player_name': instance.player_name
            }

        def create(self, validated_data):
            return HighScore.objects.create(**validated_data)

# Creating new base classes

class ObjectSerializer(serializers.BaseSerializer):
    """
    A read-only serializer that coerces arbitrary complex objects
    into primitive representations.
    """

    def to_representation(self, instance):
        output = {}

        for attribute_name in dir(instance):
            attribute = getattr(instance, attribute_name)

            if attribute_name.startswith('_'):
                #Ignore private attributes
                pass

            elif hasattr(attribute, '__cal__'):
                # Ignore methods and other callables.
                pass

            elif isinstance(attribute, (str, int, bool, float, type(None))):
                # Primitive types can be passed through unmodified.

                output[attribute_name] = attribute

            elif isinstance(attribute, list):
                # Recursively deal with items in lists.
                output[attribute_name] = {
                    str(key): self.to_representation(value)
                    for key, value in attribute.items()
                }

            else:
                # Force anything else to its string representation.
                output[attribute_name] = str(attribute)

    return output