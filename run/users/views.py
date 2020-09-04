from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import CustomUser
from .serializzers import CustomUserSerializzers
# Create your views here.
class CustomUserList(APIView):
    def get(self,request):
        user = CustomUser.objects.all()
        seriallizers = CustomUserSerializzers(user, many=True)
        return Response(seriallizers.data)
    def post(self,request):
        pass