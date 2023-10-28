# apps/users/views/authentication.py

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from ..models import Order
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
import json
def createOrder(request):
    # logic to create order
    return JsonResponse({"status": "Order Created"})