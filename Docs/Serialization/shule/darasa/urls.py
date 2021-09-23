from django.urls import path
from darasa import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('darasa/', views.darasa_list),
    path('darasa/<int:pk>/', views.darasa_detail)
]


urlpatterns = format_suffix_patterns(urlpatterns)
