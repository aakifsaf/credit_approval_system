from rest_framework import serializers
from api.models import CustomerModel, LoanModel
from api.utils import check_loan_eligibility
from datetime import datetime

class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    approved_limit = serializers.SerializerMethodField()
    
    def get_approved_limit(self, obj):
        return round(obj.monthly_salary * 36, 2)
    
    def get_name(self, obj):
        first = obj.first_name or ""
        last = obj.last_name or ""
        return f"{first.strip()} {last.strip()}".strip()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('first_name', None)
        data.pop('last_name', None)
        return data
    
    class Meta:
        model = CustomerModel
        exclude = ['current_debt']


class LoanSerializer(serializers.ModelSerializer):
    loan_approved = serializers.SerializerMethodField()
    monthly_payment = serializers.SerializerMethodField()

    def get_loan_approved(self, obj):
        result = check_loan_eligibility(
            customer_id=obj.customer_id.customer_id,
            loan_amount=obj.loan_amount,
            interest_rate=obj.interest_rate,
            tenure=obj.tenure
        )
        return result.get("approval")

    def get_monthly_payment(self, obj):
        result = check_loan_eligibility(
            customer_id=obj.customer_id.customer_id,
            loan_amount=obj.loan_amount,
            interest_rate=obj.interest_rate,
            tenure=obj.tenure
        )
        return result.get("monthly_payment")

    class Meta:
        model = LoanModel
        fields = '__all__'

class GetLoanSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    
    def get_customer(self, obj):
        return {
            "customer_id" : obj.customer_id.customer_id,
            "first_name" : obj.customer_id.first_name,
            "last_name" : obj.customer_id.last_name,
            "phone_number" : obj.customer_id.phone_number,
            "age" : obj.customer_id.age
        }
    
    class Meta:
        model = LoanModel
        fields = ['loan_id', 'customer', 'loan_amount', 'interest_rate', 'monthly_repayment', 'tenure']

class GetCustomerLoansSerializer(serializers.ModelSerializer):
    repayments_left = serializers.SerializerMethodField()
    
    def get_repayments_left(self, obj):
        today = datetime.now()
        return (obj.end_date - today).days // 30
    
    class Meta:
        model = LoanModel
        fields = ['loan_id', 'loan_amount', 'interest_rate', 'monthly_repayment', 'repayments_left']



    