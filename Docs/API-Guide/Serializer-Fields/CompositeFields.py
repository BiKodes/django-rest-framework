# ListField to validate a list of integers 
scores = serializers.ListField(
    child = serializers.IntegerField(min_value=0, max_value=100)
)

# The ListField class also supports a declarative style that allows you to write reusable 
# list field classes.


class StringListField(serializers.ListField):
    child = serializers.CharField()


# DictField a field that validates a mapping of strings to strings,

document = DictField(child=CharField())

class DocumentField(DictField):
    child = CharField()
