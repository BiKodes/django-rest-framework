from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from darasa.models import Darasa
from darasa.serializers import DarasaSerializer


@csrf_exempt
def darasa_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        darasas = Darasa.objects.all()
        serializer = DarasaSerializer(darasas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DarasaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def darasa_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        darasa = Darasa.objects.get(pk=pk)
    except Darasa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(darasa)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DarasaSerializer(darasa, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        darasa.delete()
        return HttpResponse(status=204)