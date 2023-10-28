# apps/users/views/authentication.py

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from ..models import User
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
import json

def custom_error_response(message, status=400):
    return JsonResponse({"status": "error", "message": message}, status=status)

@csrf_exempt
def register_admin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')

        # Validate email and password
        try:
            validate_email(email)
            validate_password(password)
        except ValidationError as e:
            return JsonResponse({"status": "Invalid data", "errors": list(e)}, status=400)

        # Check if a user with the given email already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({"status": "User already exists"}, status=400)

        user = User.objects.create_user(email=email, password=password, phone_number=phone_number)  # Pass phone_number to create_user
        if user:
            admin_group, created = Group.objects.get_or_create(name='Admin')
            user.groups.add(admin_group)
            return JsonResponse({"status": "Admin Registered"}, status=201)
        else:
            return JsonResponse({"status": "Registration Failed"}, status=400)
    else:
        return JsonResponse({"status": "Not a POST request"}, status=405)

@csrf_exempt
def register_regular(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')

        # Validate email and password
        try:
            validate_email(email)
            validate_password(password)
        except ValidationError as e:
            return JsonResponse({"status": "Invalid data", "errors": list(e)}, status=400)

        # Check if a user with the given email already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({"status": "User already exists"}, status=400)

        user = User.objects.create_user(email=email, password=password, phone_number=phone_number)  # Pass phone_number to create_user
        if user:
            regular_group, created = Group.objects.get_or_create(name='Regular')
            user.groups.add(regular_group)
            return JsonResponse({"status": "User Registered"}, status=201)
        else:
            return JsonResponse({"status": "Registration Failed"}, status=400)
    else:
        return JsonResponse({"status": "Not a POST request"}, status=405)

@csrf_exempt
def login_view(request):
    if request.method != 'POST':
        return custom_error_response("Method not allowed", status=405)

    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return custom_error_response("Email and password are required")

    user = authenticate(email=email, password=password)
    if user is None:
        return custom_error_response("Invalid credentials", status=401)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    # Get user's group
    group = user.groups.first()  # assuming each user belongs to only one group
    group_name = group.name if group else None

    return JsonResponse({"status": "success", "access_token": access_token, "group": group_name})


def logout_view(request):
    logout(request)
    return JsonResponse({"status": "User Logged Out"})
