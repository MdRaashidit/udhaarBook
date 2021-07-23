from django.contrib import admin
from udhaar.models import Party, Transactions
# Register your models here.

admin.site.register([Party,Transactions])
