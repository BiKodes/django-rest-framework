class AlbumSerializer(serializers.HyperLinkedModelSerializer):
    track_listing = serializers.HyperlinkedIdentityField(
        view_name='track-list'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'track_listing']
        