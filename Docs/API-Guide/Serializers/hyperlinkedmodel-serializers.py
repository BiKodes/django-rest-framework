#  explicitly include the primary key by adding it to the fields option,
class AccountSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['url', 'id', 'account_name', 'users', 'created']

# How hyperlinked views are determined

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['account_url', 'account_name', 'users', 'created']

        extra_kwargs = {
            'url': {'view_name': 'accounts', 'lookup_field': 'account_name'},
            'users': {'lookup_field': 'username'}
        }

# Alternatively you can set the fields on the serializer explicitly
class AccountSerializer(serializers.HyperLinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='accounts',
        lookup_field = 'slug'
    )

    users = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field = 'username',
        many = True,
        read_only = True
    )

    class Meta:
        model = Account
        fields = ['url', 'account_name', 'users', 'created']