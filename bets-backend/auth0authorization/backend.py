from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, exceptions


class ColligoUserBackend(RemoteUserBackend):
    """
    Remote user backend for auth0
    """

    def get_user(self, user_id):
        return super().get_user(user_id)

    def authenticate(self, request, username=None, password=None, **kwargs):
        # Deal w/ Auth0 JWT
        remote_user = kwargs.get('remote_user', '')
        user = None
        if remote_user:
            _source, user_id = tuple(remote_user.split('|'))
            try:
                user = User.objects.get(pk=int(user_id))
                return user
            except User.DoesNotExist:
                raise Exception('Could not find a Django User for this auth0 user. Auto sign ups not enabled')
            except Exception:
                user = super().authenticate(request, user_id)

        # User not auto created, must be created before
        return user
