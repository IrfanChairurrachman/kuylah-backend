from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.


@csrf_exempt
def destination_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = {'ini': 1, 'itu': 2}
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(data=data)
        # if serializer.is_valid():
            # serializer.save()
        
        return JsonResponse(data, safe=False, status=201)
        
        # return JsonResponse(serializer.errors, status=400)