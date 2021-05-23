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
        
        try:
            day = int(request.data['day'])

            test = get_popular(metadata, day)

            response_data = {
                "title": request.data['title'],
                "day": request.data['day'],
                "budget": request.data['budget'],
                "destination": test,
            }
            # print(test)
            # test = request.data
            return JsonResponse(response_data, safe=False, status=201)
        except:
            data = {'response': 'Error atau Data tidak lengkap, harus ada `title`, `day`, `budget` dan `category`',
                    'code':'400 bad request'}

            # print(type(request.data))

            response = JsonResponse(data, safe=False, status=400)
            return response