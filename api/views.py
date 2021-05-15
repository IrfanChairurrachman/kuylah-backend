from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from inventory.model import *
# Create your views here.


@api_view(['GET', 'POST'])
def destination_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    # data = {'ini': 1, 'itu': 2}
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        test = get_popular()

        return JsonResponse(test, safe=False)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(data=data)
        # if serializer.is_valid():
            # serializer.save()
        print(type(request.data['day']))
        day = int(request.data['day'])
        print(type(day))
        test = get_popular(day)
        return JsonResponse(test, safe=False, status=201)
        
        # return JsonResponse(serializer.errors, status=400)