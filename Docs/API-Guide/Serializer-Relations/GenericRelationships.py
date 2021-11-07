class TaggedItem(models.Model):
    """
    Tags arbitrary model instances using a generic relation.
    """

    tag_name = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    tagged_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag_name

class Bookmark(models.Model):
    """
    A bookmark consists of a URL, and 0 or more descriptive tags.
    """
    url = models.URLField()
    tags = GenericRelation(TaggedItem)

class Note(models.Model):
    """
    A note consists of some text and 0 or more descriptive tags
    """

    text = models.CharField(max_length=1000)
    tags = GenericRelation(TaggedItem)


class TaggedObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `tagged_object` generic relationship.
    """

    def to_reprsentation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """

        if isinstance(value, Bookmark):
            return 'Bookmark: ' + value.url

        elif isinstance(value, Note):
            return 'Note: ' + value.text

        raise Exception('Unexpected type of tagged object')

    # If you need the target of the relationship to have a nested representation, 
    # you can use the required serializers inside the .to_representation() method:

    def to_representation(self, value):
        """
        Serialize bookmark instances using a bookmark serializer,
        and note instances using a note serializer.
        """

        if isinstance(value, Bookmark):
            serializer = BookmarkSerializer(value)

        elif isinstance(value, Note):
            serializer = NoteSerialzier(value)

        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data

        


