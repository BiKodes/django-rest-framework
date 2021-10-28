# Customizing ListSerializer behavior

class CustomListSerializer(serializers.ListSerializer):
    pass

class CustomSerializer(serializers.Serializer):
    # ...
    class Meta:
        list_serializer_class = CustomListSerialize

# Customizing multiple create:

class BookListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)

class BookSerializer(serializers.Serializer):

    class Meta:
        list_serializer_class = BookListSerializer


# Customizing multiple update

class BookListSerializer(serializers.ListSerializer):

    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.

        book_mapping = {book.id: book for book in instance}
        data_mapping =  {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for book_id, data in data_mapping.items():
            book = book_mapping.get(book_id, None)

            if book is None:
                ret.append(self.child.create(data))

            else:
                ret.append(self.child.update(book, data))

        # Perform deletions.

        for book_id, book in book_mapping.items():
            if book_id not in data_mapping:
                book.delete()

        return ret


class BookSerializer(serializers.Serializer):
    # We need to identify elements in the list using their primary key,
    # so use a writable field here, rather than the default which would be read-only.

    id = serializers.IntegerField()

    class Meta:
        list_serializer_class = BookListSerializer

