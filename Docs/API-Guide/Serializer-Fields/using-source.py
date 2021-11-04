class DataPoint(models.Model):
    label = models.CharField(max_length=50)
    x_coordinate = models.SmallIntegerField()
    y_coordinate = models.SmallIntegerField()

# Using a custom field and source='*' we can provide a nested representation of the coordinate pair:

class CoordinateField(serializers.Field):

    def to_representation(self, value):
        ret = {
            "x": value.x_coordinate,
            "y": value.y_coordinate
        }

        return ret

    def to_internal_value(self, data):

        ret = {
            "x_coordinate": data["x"],
            "y_coordiante": data["y"],
        }
        return ret

class DataPointSerializer(serializers.ModelSerializer):
    coordinates = CoordinateField(source='*')

    class Meta:
        model = DataPoint
        fields = ['label', 'coordinates']


# The same thing again with the nested serializer approach suggested above:

class NestedCoordinateSerializer(serializers.Serializer):
    x = serializers.IntegerField(source='x_coordinate')
    y = serializers.IntegerField(source='y_coordinate')


class DataPointSerilaizer(serializers.ModelSerializer):
    coordinates = NestedCoordinateSerializer(source='*')

    class Meta:
        model = DataPoint
        fields = ['label', 'coordinates']
