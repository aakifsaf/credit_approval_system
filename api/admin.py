from django.contrib import admin
from .models import CustomerModel, LoanModel
# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(LoanModel)
