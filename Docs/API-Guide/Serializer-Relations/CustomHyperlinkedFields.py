from rest_framework import serializers
from rest_framework.reverse import reverse


class CustomerHyperLink(serializers.HyperlinkedField):
    # We define these as class attributes, so we don't need to pass them as arguments.

    view_name = 'customer-detail'
    queryset = Customer.objects.all()
        
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'organizaation_slug': obj.organization.slug,
            'customer_pk': obj.pk
        }

        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'organization__slug': view_kwargs['organization_slug'],
            'pk': view_kwargs['customer_pk']
        }

        return self.get_queryset().get(**lookup_kwargs)