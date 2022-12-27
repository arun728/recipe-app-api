"""
URL mappings for the User API.
"""
from user import views
from django.urls import path


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]