from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import *
from .forms import *



# Create
def logoutt(request):
    logout(request)
    return redirect(dashboard)
def login(request):

   if request.method == 'POST':
      print(request.POST)
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
         if user.is_active:
            auth.login(request, user)

         return redirect(dashboard)
      else:
         error="username or password is incorrect"
         return render(request,'pages-login-2.html',{'error':error})
   else:
      return render(request, 'pages-login-2.html')

def signup(request):
   if request.method == "POST":
      password = request.POST['password']
      confirm_password = request.POST['confirm_password']
      user_name = request.POST['username']
      print(request.POST['name'])
      first_name,last_name = request.POST['name'].split(" ")
      email = request.POST['email']
      if password == confirm_password:
         if User.objects.create_user(user_name, email, password):
            return redirect(company_create)
         else:
            context = {
               'error': 'Could not create user account - please try again.'
            }
            return render(request, 'signup.html',context)
      else:
         context = {
            'error': 'Passwords did not match. Please try again.'
         }
         return render(request, 'signup.html',context)
   else:
      return render(request, 'signup.html')

@csrf_exempt
def company_create(request):

   if request.method == 'POST':
      company_name = request.POST['company_name']
      currency = request.POST['currency']
      currency,created=Currency.objects.get_or_create(name=currency)
      company= Company(name=company_name,default_currency=currency)
      company.save()

      zip_code=request.POST['zip_code']
      city = request.POST['city']
      state= request.POST['state']
      address = request.POST['address']
      email = request.POST['email']
      phone_number = request.POST['phone_number']


      company_details=CompanyDetail(email=email,phone=phone_number,address=address,
                                    zip=zip_code,city=city,state=state,company=company)
      company_details.save()
      return redirect(dashboard)

   return render(request, 'company_create.html')

@csrf_exempt
def dashboard(request):


    if request.user.is_authenticated:

        return render(request,'dashboards-crm-analytics.html')
    else:
        return render(request, 'pages-login-2.html')