from django.urls import path
from manage_it_service.APIs import currencyAPI as views

urlpatterns = [
    path('setCurrency/', views.setCurrency.as_view()),
    path('getCurrencyes/', views.getCurrencyes.as_view()),
    path('getActiveCurrencyes/', views.getActiveCurrencies.as_view()),
    path('getInactiveCurrencyes/', views.getInactiveCurrencies.as_view()),
    path('searchCurrency/', views.searchCurrency.as_view()),
    path('updateCurrency/', views.updateCurrency.as_view()),
    path('deleteCurrency/', views.deleteCurrency.as_view()),
    path('restoreCurrency/', views.restoreCurrency.as_view()),
    ]
