from accounts.models import UserProfile


class EmailAuthBackend(object):
    def authenticate(self, req, email=None, password=None):
        try:
            user = UserProfile.objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except UserProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None
