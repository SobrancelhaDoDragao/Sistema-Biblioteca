from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import CustomUser as User

@api_view(['GET'])
def getRoutes(request):

    routes = [
        '/createuser',
        '/api/token',
        '/api/token/refresh',
        'api/VerifyAuthenticated',
    ]

    return Response(routes)


class RegisterView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class VerifyAuthenticated(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        
        response = {
            'Authenticated':True
        }

        return Response(response)

    

    
