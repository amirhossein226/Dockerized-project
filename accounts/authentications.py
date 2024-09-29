from django.core.files.base import ContentFile

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile
import requests

UserModel = get_user_model()


class EmailBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserModel.objects.get(email=username)
            print(user)
            if user.check_password(password):
                return user
            return None
        except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except User.DoesNotExists:
            return None


def create_profile(backend, user, response, *args, **kwargs):
    """
    This will create a Profile instance for users whom registered using google authentication link.
    """
    if backend.name == "google-oauth2":
        # creating instance of Profile objec
        user_profile, created = Profile.objects.get_or_create(user=user)
        # getting the url of user's profile photo
        if not created:
            image_url = response.get('picture')
            if image_url:
                # download the the user's google profile photo
                user_photo = requests.get(image_url)
                if user_photo.status_code == 200:
                    # creating unique name for each photo
                    image_name = f"{user.username}_{user.id}_profile.jpg"
                    user_profile.photo.save(
                        image_name,
                        ContentFile(user_photo.content),
                        save=True,

                    )
