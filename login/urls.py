from django.contrib import admin
from django.urls import path,include

from .views import register_view, login_view,Profile_view,Logoutview
# home

urlpatterns = [
    path('Profile/', Profile_view, name='Profile_view'),
    path('register/', register_view, name='register'),
    path('', login_view, name='login'),
    path('logout/', Logoutview, name='logout'),
]