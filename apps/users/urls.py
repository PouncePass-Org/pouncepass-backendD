# users/urls.py
from django.urls import path
from .views.authentication import register_admin, register_regular, login_view
from .views.delete_user import delete_user
from .views.get_user import GetUser
from .views.update_user import update_user

urlpatterns = [
    path('register/admin/', register_admin, name='register_admin'),
    path('register/', register_regular, name='register_regular'),
    path('login/', login_view, name='login'),
    path('user/', GetUser.as_view(), name='get_user'),
    path('users/<int:user_id>/delete/', delete_user, name='delete_user'),
    path('users/<int:user_id>/update/', update_user, name='update_user'),

]
