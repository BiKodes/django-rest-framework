from rest_framework import serializers


class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    # Field-level validation

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value

class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    # Object-level validation
    
    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data ['finish']:
            raise serializers.ValidationError("Finish must occur after start")
        return data

