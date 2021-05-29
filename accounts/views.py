from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):

	if request.method == 'POST':
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		username = request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]

		user = User.objects.create_user(username=username, first_name=first_name,
						last_name=last_name,email=email,password=password)
		user.save()
		print("User Created")
		return redirect('/')

	else: 
		return render(request,'register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,"Invalid bruh")
			return redirect('/') 
	else:
		return render(request,'login.html')


