from rest_framework import viewsets


class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_class = [IsAccountAdminOrReadOnly]


# A ViewSet that dynamically determines the queryset it should operate on

class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """

    serializer_class = AccountSerializer
    permission_classes = [IsAccountAdminOrReadOnly]

    def get_queryset(self):
        return self.request.user.accounts.all()


# ReadOnlyModelViewSet:

class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
