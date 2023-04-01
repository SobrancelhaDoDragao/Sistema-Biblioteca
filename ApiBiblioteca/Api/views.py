from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .models import CustomUser as User

@api_view(['GET'])
def getRoutes(request):

    routes = [
        'api/createuser',
        'api/token',
        'api/token/refresh',
        'api/VerifyAuthenticated',
    ]

    return Response(routes)


class VerifyAuthenticated(APIView):
    """
    Verificando se o usuario está logado
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        
        response = {
            'Authenticated':True
        }
        #request.user
        return Response(response)


class UserList(APIView):
    """
    List all user, or create a new user.
    """
    def get(self, request, format=None):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
          
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create
        """
        serializer =  UserSerializer(data=request.data)
              
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_Detail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self,request):

        try:
            return User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """
        Retrieve
        """
  
        user = self.get_object(request)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request, format=None):
        """
        Update 
        """

        user = self.get_object(request)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """
        Delete
        """
        user = self.get_object(request)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



    
