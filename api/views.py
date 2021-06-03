from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import pandas as pd
from inventory.model import *
#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel
# Create your views here.

metadata = pd.read_csv('inventory/dataset.csv', low_memory=False)

#Define a TF-IDF Vectorizer Object.
tfidf = TfidfVectorizer()

#Replace NaN with an empty string
metadata['description'] = metadata['description'].fillna('')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(metadata['description'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


@api_view(['GET', 'POST'])
def destination_list(request, format=None):
    if request.method == 'GET':

        data = {'response': 'This GET method dont do anything, try POST method'}

        print("CLIENT MINTA GET")

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':

        try:
            # change request.data['day'] from user to int type
            day = int(request.data['day'])
            budget = int(request.data['budget'])
            
            # Print category and it's type in terminal output
            print(request.data['category'])
            print(type(request.data['category']))

            # check input type, if not list just generate random without category
            if type(request.data['category']) is list:
                category = request.data['category']
                # Call get_recommendations in model by users input
                test, htm_total = get_recommendations(metadata, cosine_sim, day, category, budget)
            else:
                test, htm_total = get_recommendations(metadata, cosine_sim, day, budget=budget)

            # assign data structure for json in dict type
            response_data = {
                "title": request.data['title'],
                "category": request.data['category'],
                "day": request.data['day'],
                "budget": request.data['budget'],
                "htm_total": htm_total,
                "destination": test,
            }
            # change response_data to JSON format
            return JsonResponse(response_data, safe=False, status=201)
        except:
            # If try block error, API will respon this message below
            data = {'response': 'Error atau Data tidak lengkap, harus ada title, day, budget dan category',
                    'code':'400 bad request'}

            # change data to JSON format
            response = JsonResponse(data, safe=False, status=400)
            # return response in JSON format
            return response