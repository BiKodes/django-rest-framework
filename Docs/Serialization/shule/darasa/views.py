from django.views.decorators.csrf import csrf_exempt
from darasa.models import Darasa
from darasa.serializers import DarasaSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def darasa_list(request, format=None):
#     """
#     List all darasa codes, or create a new darasa
#     """
#     if request.method == 'GET':
#         darasas = Darasa.objects.all()
#         serializer = DarasaSerializer(darasas, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = DarasaSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def darasa_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a darasa code.
#     """

#     try:
#         darasa = Darasa.objects.get(pk=pk)
#     except Darasa.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DarasaSerializer(darasa)
#         return Response(serializer.data)


#     elif request.method == 'PUT':
#         serializer = DarasaSerializer(darasa, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         darasa.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class DarasaList(APIView):
    """
    List all darasas, or create a new darasa
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
    Retrieve, update or delete a darasa instance
    """
    def get_object(self, pk):
        try:
            return Darasa.objects.get(pk=pk)
        except Darasa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        darasa = slef.get_object(pk)
        serializer =  DarasaSerializer(darasa)

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
        



