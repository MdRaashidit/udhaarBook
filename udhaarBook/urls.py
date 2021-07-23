from udhaar.views import Transactions, udhari
from django.contrib import admin
from django.urls import path
from udhaar.views import udhari

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',udhari)
    
]
