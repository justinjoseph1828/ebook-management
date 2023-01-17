from django.shortcuts import render
from django.http import JsonResponse
from .models import ebook
from .serializers import bookserializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def booklist(request):

    if request.method == 'GET':
        books=ebook.objects.all()
        serializer=bookserializer(books,many=True)
        return JsonResponse({"books":serializer.data})

    if request.method == 'POST':
        serializer=bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"books":serializer.data})

@api_view(['GET','PUT','DELETE'])
def book_detail(request, id):
    try:
        book=ebook.objects.get(pk=id)
    except ebook.DoesNotExist:
        return Response("NOT FOUND",status=404)
    if request.method=='GET':
      serializer=  bookserializer(book)
      return Response(serializer.data)
    elif request.method=='PUT':
        serializer= bookserializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=404)
    elif request.method=='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



