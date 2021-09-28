from django.urls import path
from darasa import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('darasa/', views.DarasaList.as_view(), name='darasa-list'),
    path('darasa/<int:pk>/', views.DarasaDetail.as_view(), name='darasa-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('darasas/<int:pk>/highlight/', views.DarasaHighlight.as_view(), name='darasa-highlight')
]


urlpatterns = format_suffix_patterns(urlpatterns)