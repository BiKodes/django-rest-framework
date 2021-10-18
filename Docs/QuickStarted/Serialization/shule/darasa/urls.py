from django.urls import path
from darasa import views

urlpatterns = [
    path('darasa/', views.darasa_list),
    path('darasa/<int:pk>/', views.darasa_detail),
]
