from django.shortcuts import render
import json

# Create your views here.

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse


###################### api views
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.middleware.csrf import get_token
from .parsers import PlainTextParser



def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') # replace 'home' with the name of your home page view
        else:
             # handle invalid login credentials
            # return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
            return redirect(reverse('registerView'))
    else:
        return render(request, 'login.html')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(reverse('loginView')) # replace 'login' with the name of your login view
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logoutView(request):
    if request.method=='POST':
        # jsonbody = json.loads(request.body)
        logout(request)
        return redirect(reverse('loginView'))

###################### api views
class apiLogin(APIView):
    print("apiLogin")
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   
    parser_classes = [PlainTextParser]
    def post(self, request, format=None):
        jsondata = json.loads(request.data)
        print(jsondata)
        keyList = jsondata.keys()
        if( 'email' in keyList and 'password' in keyList) :
            email = jsondata['email']
            password = jsondata['password']
        else:
            return Response({'error': 'Invalid params format'})
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)