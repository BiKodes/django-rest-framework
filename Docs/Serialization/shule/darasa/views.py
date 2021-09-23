from django.views.decorators.csrf import csrf_exempt
from darasa.models import Darasa
from darasa.serializers import DarasaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
@api_view(['GET', 'POST'])
def darasa_list(request, format=None):
    """
    List all darasa codes, or create a new darasa
    """
    if request.method == 'GET':
        darasas = Darasa.objects.all()
        serializer = DarasaSerializer(darasas, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DarasaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def darasa_detail(request, pk, format=None):
    """
    Retrieve, update or delete a darasa code.
    """

    try:
        darasa = Darasa.objects.get(pk=pk)
    except Darasa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DarasaSerializer(darasa)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = DarasaSerializer(darasa, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        darasa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

