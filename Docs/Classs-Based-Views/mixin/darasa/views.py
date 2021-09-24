from darasa.models import Darasa
from darasa.serializers import DarasaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DarasaList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        darasas = Darasa.objects.all()
        serializer = DarasaSerializer(darasas, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DarasaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DarasaDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Darasa.objects.get(pk=pk)
        except Darasa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        darasa = self.get_object(pk)
        serializer = DarasaSerializer(darasa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        darasa = self.get_object(pk)
        serializer = DarasaSerializer(darasa, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        darasa = self.get_object(pk)
        darasa.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)