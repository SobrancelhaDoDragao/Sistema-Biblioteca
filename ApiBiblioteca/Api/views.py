from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser as User

@api_view(['GET'])
def getRoutes(request):

    routes = [
        '/createuser',
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


class RegisterView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

   
    

    
