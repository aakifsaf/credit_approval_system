from django.urls import path
from api.views import RegisterView, CheckEligibilityView, CreateLoanView, GetLoanView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("check-eligibility/", CheckEligibilityView.as_view()),
    path("create-loan/", CreateLoanView.as_view()),
    path("view-loan/<int:loan_id>", GetLoanView.as_view()),
]