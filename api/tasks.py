from django.db import IntegrityError
import pandas as pd
from celery import shared_task
from .models import CustomerModel, LoanModel

@shared_task
def ingest_customer_data(file_path):
    try:
        df = pd.read_excel(file_path)

        df = df.drop_duplicates(subset='Customer ID', keep='first')

        for _, row in df.iterrows():
            try:
                CustomerModel.objects.update_or_create(
                    customer_id=int(row['Customer ID']),
                    defaults={
                        'first_name': row['First Name'],
                        'last_name': row['Last Name'],
                        'age': row['Age'],
                        'phone_number': str(row['Phone Number']),
                        'monthly_salary': row['Monthly Salary'],
                        'approved_limit': row['Approved Limit'],
                    }
                )
            except IntegrityError as e:
                print(f"⚠️ Skipped conflicting row: {row['Customer ID']} - {e}")
        print("Data ingestion complete.")
    except Exception as e:
        print(f"Error loading file: {e}")

@shared_task
def ingest_loan_data(file_path):
    try:
        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            try:
                LoanModel.objects.create(
                    loan_id=int(row['Loan ID']),
                    customer_id=CustomerModel.objects.get(customer_id=int(row['Customer ID'])),
                    loan_amount=row['Loan Amount'],
                    tenure=row['Tenure'],
                    interest_rate=row['Interest Rate'],
                    monthly_repayment=row['Monthly payment'],
                    emis_paid_on_time=row['EMIs paid on Time'],
                    start_date=row['Date of Approval'],
                    end_date=row['End Date'],
                )
            except IntegrityError as e:
                print(f"⚠️ Skipped conflicting row: {row['Loan ID']} - {e}")
        print("Data ingestion complete.")
    except Exception as e:
        print(f"Error loading file: {e}")