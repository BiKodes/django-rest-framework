from rest_framework import mixins

class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.GenericViewSet):

    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    pass