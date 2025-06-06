from django.db import models
# Create your models here.

class CustomerModel(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    monthly_salary = models.IntegerField(null=True, blank=True)
    approved_limit = models.IntegerField(null=True, blank=True)
    current_debt = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.first_name    

class LoanModel(models.Model):
    customer_id = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    loan_id = models.AutoField(primary_key=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tenure = models.IntegerField(null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monthly_repayment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    emis_paid_on_time = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.customer_id