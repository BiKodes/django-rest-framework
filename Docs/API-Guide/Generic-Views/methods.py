def get_queryset(self):
    user = self.request.user
    return user.accounts.all()

def get_object(self):
    queryset = self.get_queryset()
    filter = {}

    for field in self.multiple_lookup_fields:
        filter[field] = self.kwargs[field]

    obj = get_object_or_404(queryset, **filter)
    self.check_object_permissions(self.request, obj)

    return obj

def filter_queryset(self, queryset):
    filter_backends = [CategoryFilter]

    if 'geo_route' in self.request.query_params:
        filter_backends = [GeoRouteFilter, CategoryFilter]
    elif 'geo_point' in self.request.query_params:
        filter_backends = [GeoPointFilter, CategoryFilter]

    for backend in list(filter_backends):
        queryset = backend().filter_queryset(self.request, queryset, view=self)

    return queryset

def get_serializer_class(self):
    if self.request.user.is_staff:
        return FullAccountSerializer
    return BasicAccountSerializer

def perform_create(self, serializer):
    serializer.save(user=self.request.user)

def perform_update(self, serializer):
    instance = serializer.save()
    send_email_confirmation(user=self.request.user, modified=instance)

def perform_create(self, serializer):
    queryset = SignupRequest.objects.filter(user=self.request.user)
    
    if queryset.exists():
        raise ValidationError('You have already signed up')
    serializer.save(user=self.request.user)


