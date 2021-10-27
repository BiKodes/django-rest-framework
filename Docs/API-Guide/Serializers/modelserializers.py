# Declaring a ModelSerializer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fileds = ['id', 'account_name', 'users', 'created'] 

# Specifying which fields to include

class AccountSerializer(serializer.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']

class AccountSerializer(serializer.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

# set the exclude attribute to a list of fields to be excluded from the serializer.
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['users']

# Specifying nested serialization
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
        depth = 1

# Specifying fields explicitly

class AccountSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    groups = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Account

# Specifying read only fields

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
        read_only_fields = ['account_name']

# Additional keyword arguments

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def ceate(self, validted_data):
            user = User(
                email = Validated_data['email'],
                username = validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user