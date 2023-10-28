# File: users/views/get_user.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import User
from ..serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)
