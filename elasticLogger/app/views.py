# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer


logger = logging.getLogger(__name__)


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        logger.info('List all snippets')
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Create a new snippet')
            return JsonResponse(serializer.data, status=201)
        logger.error('Something went wrong!')
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        logger.error('Snippet with id {} doesn\'t exist'.format(pk))
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        logger.info('Get snippet with id of {}'.format(pk))
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Update snippet with id of {}'.format(pk))
            return JsonResponse(serializer.data)
        logger.error('Some thing wrong in updating snippet with id of {}'.format(pk))
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        logger.info('Delete snippet with id of {}'.format(pk))
        return HttpResponse(status=204)