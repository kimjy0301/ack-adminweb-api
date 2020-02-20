from rest_framework import authentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from user.models import User
from datetime import timedelta


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(
                jwt_token,
                settings.SECRET_KEY,
                leeway=timedelta(seconds=10),
                algorithms=["HS256"],
            )
            pk = decoded.get("pk")
            user = User.objects.get(pk=pk)
            return (user, None)
        except ValueError:
            return None
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed(detail="jwt 형식이 맞지 않습니다.")
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(detail="jwt 토큰이 만료되었습니다.")
