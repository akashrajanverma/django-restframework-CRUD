from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import AuthorSerializer, BookSerializer, UpdateBookSerializer
from .models import Author, Book
from django.contrib.auth.models import User
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def welcome(request):
    data = {"message": "Welcome to the bookstore"}
    return Response(data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_author(request):
    serializer = AuthorSerializer(data=request.data)
    
    if serializer.is_valid():
        user = User.objects.get(username=request.user.username)
        author = Author(name=request.data['name'], added_by=user)
        author.save()
        return Response("Author added successfully", status=200)
    else:
        return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_book(request):
    #print(request.user)
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        user = request.user
        author = Author.objects.filter(name=request.data['author']).filter(added_by=user)
        print(author)
        for auth in author:
            book = Book(title=request.data['title'], description=request.data['description'], author=auth, added_by=user)
            book.save()
        return Response("book saved successfully", status=200)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_books(request):
    user = request.user
    book = Book.objects.filter(added_by=user)
    arr = []
    for b in book:
        res = {}
        res['title'] = b.title
        res['desc'] = b.description
        arr.append(res)
    return Response(data={"books": arr}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_book_title(request):
    serializer = UpdateBookSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        get_book = Book.objects.filter(title=request.data['title'], added_by=user)
        for book in get_book:
            book.title = request.data['new_title']
            book.save()
        return Response(status=200, data={"updated successfully"})

    else:
        return Response( serializer.errors, status=400)
