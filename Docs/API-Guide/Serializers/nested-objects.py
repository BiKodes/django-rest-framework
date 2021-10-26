class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class CommentSerializer(serializers.Serializer):
    user = UserSerializer()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


class CommentSerializer(serializers.Serializer):
    # May be an anonymous user.
    user = UserSerializer(required=False)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()



class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    # A nested list of 'edit' items.
    edits = EditItemSerializer(many=True)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
