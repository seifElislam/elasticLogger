# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer


# logger = logging.getlogging(__name__)


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        print('x')
        logging.info('List all snippets')
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logging.info('Create a new snippet')
            return JsonResponse(serializer.data, status=201)
        logging.error('Something went wrong!')
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        logging.error('Snippet with id {} doesn\'t exist'.format(pk))
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        logging.info('Get snippet with id of {}'.format(pk))
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            logging.info('Update snippet with id of {}'.format(pk))
            return JsonResponse(serializer.data)
        logging.error('Some thing wrong in updating snippet with id of {}'.format(pk))
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        logging.info('Delete snippet with id of {}'.format(pk))
        return HttpResponse(status=204)