from newapp.models import Food
from newapp.forms import FoodForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class FoodAdd(CreateView):
    model = FoodList
    fields = '__all__'
    success_url = 'http://127.0.0.1:8000/'

class FoodsList(ListView):
    model = FoodList

class FoodOrderView(DetailView):
    model = FoodList


def index(request):
    return render(request, 'newapp/index.html', {})

def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('userlogin')
    return render(request, 'newapp/signup_form.html', {'form':form})

def userlogin(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == 'POST':
        data = request.POST 
        u = data['username']
        p = data['password']
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('foodslist')
    return render(request, 'newapp/login_form.html', {'form':form})

def userlogout(request):
    logout(request)
    return redirect('userlogin')



def hotelslist(request):
    return render(request, 'newapp/hotels.html', {})