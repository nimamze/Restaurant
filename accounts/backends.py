from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class PhoneAuthenticate(ModelBackend):

    def authenticate(self, request, username = None , password = None , **kwargs):

        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(phone = username)
        except UserModel.DoesNotExist:
            return None
        if user and user.check_password(password) and self.user_can_authenticate(user): # type: ignore
            return user
        return None
