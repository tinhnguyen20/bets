from authlib.integrations.django_oauth2 import ResourceProtector
from django.http import JsonResponse
from functools import wraps
from rest_framework.decorators import api_view, permission_classes
import jwt
from . import validators
require_auth = ResourceProtector()
validator = validators.Auth0JWTBearerTokenValidator(
    "dev-wlelmdzz.us.auth0.com",
    "bets"
)
require_auth.register_token_validator(validator)


def public(request):
    """No access token required to access this route
    """
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return JsonResponse(dict(message=response))


@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})


@require_auth("read:messages")
def private_scoped(request):
    """A valid access token and an appropriate scope are required to access this route
    """
    response = "Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this."
    return JsonResponse(dict(message=response))

def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope