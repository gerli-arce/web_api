from django.contrib import admin
from django.urls import path, include
from manage_it_service.PATHs import usersPATH
from manage_it_service.PATHs import servicesPATH
from manage_it_service.PATHs import currencyPATH

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(usersPATH)),
    path('services/', include(servicesPATH)),
    path('services/', include(currencyPATH)),
]
