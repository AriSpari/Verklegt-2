from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/',  LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'),name='logout'),
    path('register/', views.register,name='register'),
    path('profile/',  views.profile,name='profile'),
]
