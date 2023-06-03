app_name = 'users'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]