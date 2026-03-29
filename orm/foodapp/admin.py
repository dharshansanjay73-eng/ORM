from django.contrib import admin
from .models import CustomerDB

@admin.register(CustomerDB)
class CustomerDBAdmin(admin.ModelAdmin):
    list_display = ['PhoneNo','Address','OrderNo','Amount','Items','CustomerName','AdditionalNo']