from django.urls import path
from . import views

urlpatterns = [
    # path('login', views.loginView, name='loginView'),
    path('', views.loginView, name='loginView'),
    path('register', views.registerView, name='registerView'),
    path('logout', views.logoutView, name='logoutView'),
    path('api/login', views.apiLogin.as_view(), name='apiLogin'),
]
