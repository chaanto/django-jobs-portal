from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class RegisterAPIView(APIView) :
    def post(self, request) :
        return Response('Hello LOL')