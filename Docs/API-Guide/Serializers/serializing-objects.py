serializer = CommentSerializer(comment)
serializer.data

json = JSONRenderer().render(serializer.data)
json