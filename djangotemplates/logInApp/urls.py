from django.urls import path
from . import views

urlpatterns = [
    # path('login', views.loginView, name='loginView'),
    path('', views.loginView, name='loginView'),
    path('register', views.registerView, name='registerView'),
]
