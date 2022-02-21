from . import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from . import serializers


def get_response(status, message, result={}):
    if status >200:
        success=False
    else:
        success=True
    return {
        "success": success,
        "status": status,
        "message": message,
        "result": result
    }
        
class manager_access(BasePermission):
    message = {
        "success":False,
        "message":'permission denied',
        "result":{"details":"you don't have permission to perform this action"}
        }
    def has_permission(self, request, view):
        if request.user.role=="Admin" or (
            request.user.role=="Manager"):
            return True
        return False


def authenticate(self, username, password):
        try:
            user = CustomUser.objects.get(
                email=username)
        except CustomUser.DoesNotExist:
            return None
        return user if user.check_password(password) else None

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    serializer=serializers.UserDetailsSerializer(user).data
    return {
        'token_type':'Bearer',
        'expiresIn': '3600',
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user_details':serializer
    }
   