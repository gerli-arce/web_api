from django.urls import path
from manage_it_service.APIs import servicesAPI as views

urlpatterns = [
    path('setService/', views.setService.as_view()),
    path('getServices/', views.getServices.as_view()),
]