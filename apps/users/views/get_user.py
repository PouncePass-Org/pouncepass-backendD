# File: users/views/get_user.py
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from apps.users.serializers import UserSerializer

class GetUser(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # No need to query the database again, as request.user is already populated by the authentication class
        return self.request.user
