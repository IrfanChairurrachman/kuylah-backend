from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import pandas as pd
from inventory.model import *
# Create your views here.

metadata = pd.read_csv('inventory/dataset.csv', low_memory=False)

@api_view(['GET', 'POST'])
def destination_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    # data = {'ini': 1, 'itu': 2}
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        test = get_popular(metadata, 12)

        print(type(test))

        print("CLIENT MINTA GET")

        return JsonResponse(test, safe=False)

    elif request.method == 'POST':
        
        