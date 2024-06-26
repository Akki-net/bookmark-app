from django.contrib.auth.models import User
from account.models import Profile
class EmailBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except DoesNotExist:
            return None
def create_profile(backend, user, *args, **kwargs):
    """
    Create user profile for social authentication
    """
    Profile.objects.get_or_create(user=user)