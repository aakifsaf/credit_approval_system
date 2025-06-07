# utils.py
from decimal import Decimal
from datetime import datetime
from .models import CustomerModel, LoanModel
from django.db.models import Sum

def check_loan_eligibility(customer_id, loan_amount, interest_rate, tenure):
    try:
        customer = CustomerModel.objects.get(customer_id=customer_id)
        loan_amount = Decimal(str(loan_amount))
        interest_rate = Decimal(str(interest_rate))
        tenure = int(tenure)
        approved_limit = Decimal(str(customer.approved_limit))
        monthly_salary = Decimal(str(customer.monthly_salary))

        customer_loans = LoanModel.objects.filter(customer_id=customer_id)
        today = datetime.now()
        current_loans = customer_loans.filter(end_date__gt=today)

        total_current_debt = current_loans.aggregate(total=Sum('loan_amount'))['total'] or Decimal('0')
        if total_current_debt > approved_limit:
            return {
                "customer_id": customer_id,
                "approval": False,
                "interest_rate": float(interest_rate),
                "corrected_interest_rate": None,
                "tenure": tenure,
                "monthly_payment": None,
            }

        paid_on_time = customer_loans.aggregate(paid_on_time=Sum('emis_paid_on_time'))['paid_on_time'] or 0
        loan_count = customer_loans.count()
        paid_on_time_ratio = paid_on_time / loan_count if loan_count else 0

        current_year = today.year
        activity_this_year = customer_loans.filter(end_date__year=current_year).count()
        total_loan_volume = customer_loans.aggregate(total=Sum('loan_amount'))['total'] or Decimal('0')

        credit_score = 0
        credit_score += paid_on_time_ratio * 30
        credit_score += max(0, 10 - 0.5 * loan_count)
        credit_score += max(0, 10 - 2 * activity_this_year)
        credit_score += max(0, 20 - float(total_loan_volume / Decimal('100000')))

        monthly_interest_rate = interest_rate / Decimal('1200')
        if monthly_interest_rate == 0:
            emi = loan_amount / tenure
        else:
            emi = loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** tenure) / (((1 + monthly_interest_rate) ** tenure) - 1)
        emi = emi.quantize(Decimal("0.01"))

        existing_emi = current_loans.aggregate(total=Sum('monthly_repayment'))['total'] or Decimal('0')
        total_emi_burden = existing_emi + emi

        if total_emi_burden > monthly_salary * Decimal('0.5'):
            return {
                "customer_id": customer_id,
                "approval": False,
                "interest_rate": float(interest_rate),
                "corrected_interest_rate": None,
                "tenure": tenure,
                "monthly_payment": None,
            }

        approved = False
        corrected_interest_rate = None

        if credit_score > 50:
            approved = True
        elif 30 < credit_score <= 50:
            approved = interest_rate >= Decimal('12')
        elif 10 < credit_score <= 30:
            approved = interest_rate >= Decimal('16')
        else:
            approved = False

        return {
            "customer_id": customer_id,
            "approval": approved,
            "interest_rate": float(interest_rate),
            "corrected_interest_rate": corrected_interest_rate,
            "tenure": tenure,
            "monthly_payment": float(emi)
        }

    except CustomerModel.DoesNotExist:
        raise Exception("Customer not found")
