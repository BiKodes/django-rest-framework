from darasa.models import Darasa
from darasa.serializers import DarasaSerializer, UserSerializer
from django.contrib.auth.models import User
from darasa.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import generics


class DarasaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,`update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Darasa.objects.all()
    serializer_class = DarasaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        darasa = self.get_object()

        return Response(darasa.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DarasaHighlight(generics.GenericAPIView):
    queryset = Darasa.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        darasa = self.get_object()
        return Response(darasa.highlighted)


