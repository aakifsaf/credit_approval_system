from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import RegisterSerializer, LoanSerializer, GetLoanSerializer, GetCustomerLoansSerializer
from api.models import CustomerModel, LoanModel
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal
from rest_framework import generics
from .utils import check_loan_eligibility
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class CheckEligibilityView(APIView):
    def post(self, request):
        try:
            data = request.data
            result = check_loan_eligibility(
                customer_id=data.get("customer_id"),
                loan_amount=data.get("loan_amount"),
                interest_rate=data.get("interest_rate"),
                tenure=data.get("tenure")
            )

            return Response({
                "customer_id": data.get("customer_id"),
                "approval": result.get("approval"),
                "interest_rate": float(data.get("interest_rate")),
                "corrected_interest_rate": result.get("corrected_interest_rate"),
                "tenure": data.get("tenure"),
                "monthly_payment": result.get("monthly_payment")
            })
        except Exception as e:
            return Response({"error": str(e)}, status=400)
            
class CreateLoanView(APIView):
    def post(self, request):
        try:
            serializer = LoanSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "loan_id" : serializer.data.get("loan_id"),
                        "customer_id" : serializer.data.get("customer_id"),
                        "loan_approved" : serializer.data.get("loan_approved"),
                        "message" : "Loan created successfully",
                        "monthly_payment" : serializer.data.get("monthly_payment")
                    }
                    , status=201)
            return Response(
                {   
                    "loan_id" : None,
                    "customer_id" : serializer.data.get("customer_id"),
                    "loan_approved" : False,
                    "message" : serializer.errors,
                    "monthly_payment" : None
                }
                , status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class GetLoanView(APIView):
    def get(self, request, loan_id):
        try:
            loan = LoanModel.objects.get(loan_id=loan_id)
            serializer = GetLoanSerializer(loan)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
class GetCustomerLoansView(APIView):
    def get(self, request, customer_id):
        try:
            loans = LoanModel.objects.filter(customer_id=customer_id)
            serializer = GetCustomerLoansSerializer(loans, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)