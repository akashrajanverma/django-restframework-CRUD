from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import AuthorSerializer
from .models import Author
from django.contrib.auth.models import User
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def welcome(request):
    data = {"message": "Welcome to the bookstore"}
    return Response(data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user(request):
    serializer = AuthorSerializer(data=request.data)
    
    if serializer.is_valid():
        user = User(first_name="akash", last_name="rajan", username="vikas")
        user.save()
        author = Author(name=request.data['name'], added_by=user)
        author.save()
        return Response("Author added successfully", status=200)
    else:
        return Response(serializer.errors, status=400)
