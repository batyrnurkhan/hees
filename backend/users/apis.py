from rest_framework import views, response, exceptions, permissions
from . import serializer as user_serializer
from . import services, authentication
from django.contrib.auth import logout
class RegisterApi(views.APIView):
    def post(self, req):
        serializer = user_serializer.UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc = data)

        return response.Response(data=serializer.data)

class LoginApi(views.APIView):
    def post(self, req):
        email = req.data["email"]
        password = req.data["password"]

        user = services.user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid credentials")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid credentials")

        token = services.create_token(user_id=user.id)

        resp = response.Response()

        resp.set_cookie(key = "jwt", value=token, httponly=True)

        return resp

class UserApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, req):
        user = req.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)

class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "User Logged out successfully"}
        return resp