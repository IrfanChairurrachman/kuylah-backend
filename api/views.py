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
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        test = get_popular(metadata, 12)

        print(type(test))

        print("CLIENT MINTA GET")

        return JsonResponse(test, safe=False)

    elif request.method == 'POST':

        try:
            # change request.data['day'] from user to int type
            day = int(request.data['day'])
            # get itinerary data
            test = get_popular(metadata, day)

            # assign data structure for json in dict type
            response_data = {
                "title": request.data['title'],
                "day": request.data['day'],
                "budget": request.data['budget'],
                "destination": test,
            }
            # print(test)
            # test = request.data
            # change response_data to JSON format
            return JsonResponse(response_data, safe=False, status=201)
        except:
            # If try block error, API will respon this message below
            data = {'response': 'Error atau Data tidak lengkap, harus ada title, day, budget dan category',
                    'code':'400 bad request'}

            # print(type(request.data))

            # change data to JSON format
            response = JsonResponse(data, safe=False, status=400)
            # return response in JSON format
            return response