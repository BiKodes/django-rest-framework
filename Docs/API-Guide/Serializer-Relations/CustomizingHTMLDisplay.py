class TrackPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return 'Track: %s' % (instance.title)

        