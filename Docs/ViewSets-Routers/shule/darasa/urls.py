from django.urls import path, include
from darasa import views
from rest_framework.urlpatterns import format_suffix_patterns
from darasa.views import DarasaViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'darasas', views.DarasaViewSet)
router.register(r'users', views.UserViewSet)


# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('', include(router.urls)),
]


# darasa_list = DarasaViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# darasa_detail = DarasaViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# darasa_highlight = DarasaViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     path('', views.api_root),
#     path('darasa/', darasa_list, name='darasa-list'),
#     path('darasa/<int:pk>/', darasa_detail, name='darasa-detail'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
#     path('darasas/<int:pk>/highlight/', darasa_highlight, name='darasa-highlight')
# ]


# urlpatterns = format_suffix_patterns(urlpatterns)