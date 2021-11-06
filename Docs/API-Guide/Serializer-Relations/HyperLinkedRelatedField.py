class AlbumSerializer(serializers.ModelSerialzier):
    tracks = serializers.HyperLinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

        