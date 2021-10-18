from django.urls import path
from darasa import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('darasa/', views.DarasaList.as_view()),
    path('darasa/<int:pk>/', views.DarasaDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)