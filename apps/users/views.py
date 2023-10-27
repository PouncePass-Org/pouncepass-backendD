from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import User
import json

@csrf_exempt  # Only for demonstration; in production, you should properly handle CSRF.
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = User.objects.create_user(email=email, password=password)
        if user:
            return JsonResponse({"status": "User Registered"})
        else:
            return JsonResponse({"status": "Registration Failed"})
    else:
        return JsonResponse({"status": "Not a POST request"})

@csrf_exempt  # Only for demonstration; in production, you should properly handle CSRF.
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "User Logged In"})
        else:
            return JsonResponse({"status": "Invalid Credentials"})
    else:
        return JsonResponse({"status": "Not a POST request"})

@login_required
def logout_view(request):
    logout(request)
    return JsonResponse({"status": "User Logged Out"})

@login_required
def updateProfile(request, user_id):
    if request.method == 'POST':
        # Assuming you're sending a JSON payload with fields to update
        data = json.loads(request.body)

        # Locate the user to update
        user = User.objects.get(pk=user_id)

        # Update fields
        user.email = data.get('email', user.email)

        # Save changes
        user.save()

        return JsonResponse({"status": "Profile Updated"})
    else:
        return JsonResponse({"status": "Not a POST request"})
