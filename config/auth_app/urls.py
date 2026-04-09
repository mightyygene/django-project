from django.urls import path
from .views import landing, login_view, register_view, home

urlpatterns = [
    path('', landing, name='landing'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home, name='home'),
]