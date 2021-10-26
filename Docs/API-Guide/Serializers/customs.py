class UserManager(models.Manager):
    
    def create(self, username, email, is_premium_member=False, has_support_contract=False):
        user = User(username=username, email=email)
        user.save()
        profile = Profile(
            user=user,
            is_premium_member = is_premium_member,
            has_support_contract = has_support_contract

        )
        profile.save()
        return user