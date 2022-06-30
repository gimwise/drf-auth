from rest_framework.response import Response
from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def user_list(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)