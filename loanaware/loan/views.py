from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from loan.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def home(request):
    return render(request,"loan/index.html")

def Business(request):
    busines=loan.objects.filter(cat=1)
    return render(request,"loan/business.html",{"business":busines})
def edu(request):
    education=loan.objects.filter(cat=2)
    return render(request,"loan/education.html",{"education":education})
def other(request):
    others=loan.objects.filter(cat=3)
    return render(request,"loan/other.html",{"others":others})

def loan_search(request):
    query_amount = request.GET.get('amount')
    query_cat = request.GET.get('cat')

    results = loan.objects.all()

    if query_amount:
        results = results.filter(amount__icontains=query_amount)
    if query_cat:
        results = results.filter(category__icontains=query_cat)

    return render(request, 'loan/assistance.html', {'results': results})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out sucessfully ..!")
    return redirect('/')
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in sucessfully ..!")
                return redirect('/') 
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect('/login')  
        return render(request,"loan/login.html")

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()            
            messages.success(request, "Registered successfully. You can login now.")
            return redirect('/login')
    return render(request, "loan/signup.html", {'form': form})

def profile(request):
    pro=loan.objects.filter(age_eligibility__gt=19)
    return render(request,"loan/profile.html",{'pro':pro})