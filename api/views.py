from .utils import random_string
from rest_framework.views import APIView
from .models import LoginModel
from rest_framework.response import Response
from rest_framework import status


class LoginAPIView(APIView):

    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        user_name = request.data.get('user_name')
        try:
            token = random_string(50)
            new_login = LoginModel.objects.create(user_id=user_id, user_name=user_name, token=token)
            new_login.save()
            response_msg = "SUCCESS"
        except:
            response_msg = "FAILURE"
            token = None
        response = {
            "request_id": random_string(20),
            "response_msg": response_msg,
            "data": {
                "token": token,
                "user_info": {
                    "user_id": user_id,
                    "user_name": user_name
                }
            }
        }
        return Response(response)


class AuthenticationAPIView(APIView):

    def post(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION', '')
        login = LoginModel.objects.filter(token=token).first()
        if login is None:
            return Response({"Authorization": token}, status=status.HTTP_400_BAD_REQUEST)
        response = {
            "data": {
                "user_id": login.user_id,
                "user_name": login.user_name
            }
        }
        return Response(response, status=status.HTTP_200_OK)
