from django.urls import path, include
from .views import user_register, user_login, user_logout

urlpatterns = [
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('register', user_register, name='register'),
]
