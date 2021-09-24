from darasa.models import Darasa
from darasa.serializers import DarasaSerializer
from rest_framework import generics


class DarasaList(generics.ListCreateAPIView):
    queryset = Darasa.objects.all()
    serializer_class = DarasaSerializer


class DarasaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Darasa.objects.all()
    serializer_class = DarasaSerializer