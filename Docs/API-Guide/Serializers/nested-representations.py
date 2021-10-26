#  writable nested representations you'll need to write .create() or .update() 
# methods that handle saving multiple objects.

class UserSerializer(serializers.Serializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'profile']

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user

    # use the new manager method.
    def create(self, validated_data):
        return User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            is_premium_member = validated_data['profile']['is_premium_member'],
            has_support_contract = validated_data['profile']['has_support_contract']
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')

        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.is_premium_member = profile_data.get(
            'is_premium_member',
            profile.is_premium_member
        )

        profile.has_support_contract = profile_data.get(
            'has_support_contract',
            profile.has_support_contract
        )
        profile.save()

        return instance


