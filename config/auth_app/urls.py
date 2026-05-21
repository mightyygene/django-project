from django.urls import path
from auth_app.views import home, login_view, register_view, dashboard, landing, logout_view

urlpatterns = [
    path('', landing, name='landing'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]