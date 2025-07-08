from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('verify/<uidb64>/<token>/', views.verify_email, name='verify_email'),  # ✅ Correct
     path('register/', views.register_view, name='register'),
]
