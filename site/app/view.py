from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact
from .serializers import ContactSerializer


def index(request):
    return render(request, 'index.html')


@api_view(('GET', 'POST'))
def action_index(request, format=None):
    if request.method == 'GET':
        fetchAllContacts = Contact.objects.all()
        serializer = ContactSerializer( fetchAllContacts, many=True )
        json = JSONRenderer().render(serializer.data)
        return HttpResponse( json )
    elif request.method == 'POST':
        return action_store(request)


def action_create(request):
    pass


@api_view(('POST', ))
def action_store(request):
    serializer = ContactSerializer( data=request.DATA )
    if serializer.is_valid():
        serializer.save()
        return Response( serializer.data,
                         status=status.HTTP_201_CREATED )
    else:
        return Response( serializer.errors,
                         status=status.HTTP_400_BAD_REQUEST )


@api_view(('GET', ))
def action_show(request, id):
    try:
        contact = Contact.objects.get( id=id )
    except Contact.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND )
    serializer = ContactSerializer( contact )
    return Response( serializer.data )

@api_view(('DELETE', 'PUT'))
def action_edit(request, id):
    if request.method == 'DELETE':
        return action_destroy( request, id )
    elif request.method == 'PUT':
        return action_update( request, id )
    else:
        return Response( status=status.HTTP_400_BAD_REQUEST )


@api_view(('PUT', ))
def action_update(request, id):
    try:
        contact = Contact.objects.get( id=id )
    except Contact.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND )
    serializer = ContactSerializer( contact, data=request.DATA )
    if serializer.is_valid():
        serializer.save()
        return Response( serializer.data )
    else:
        return Response( serializer.errors,
                  status=status.HTTP_400_BAD_REQUEST )

    
@api_view(('DELETE', ))
def action_destroy(request, id):
    try:
        contact = Contact.objects.get( id=id )
    except Contact.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND )
    contact.delete()
    return Response( status=status.HTTP_204_NO_CONTENT)
