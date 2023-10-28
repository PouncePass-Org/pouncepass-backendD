# apps/users/views/authentication.py

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from ..models import Payment
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
import json

def makePayment(request):
    # logic to make payment
    return JsonResponse({"status": "Payment Made"})

def refundPayment(request, payment_id):
    # logic to refund payment
    return JsonResponse({"status": "Payment Refunded"})
