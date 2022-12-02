from django.http import request
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import datetime

from accounts.forms import *

# Create your views here.

User = get_user_model()

@csrf_exempt
def login_flutter(request):
	context = {}
	user = request.user
	
	if request.method == "POST":
		user_input = request.POST['email'] 
		try:
			email = User.objects.get(username=user_input).email
		except User.DoesNotExist:
			email = request.POST['email']

		password = request.POST['password']

		user = authenticate(request, email=email, password=password)

		if user is not None:
			login(request, user)
			# Redirect to a success page.
			context['login'] = "logged-in"
			context['user'] = {
				"email": user.email, 
				"username": user.username, 
				"name": user.name, 
				"age": user.age, 
				"gender": user.gender, 
				"city": user.city, 
				"address": user.address, 
				"id" : user.id, 
				"is_regular" : user.is_regular, 
				"is_bank" : user.is_bank, 
				"is_superuser": user.is_superuser,
				"is_admin": user.is_admin, 
				"is_staff": user.is_staff }
			
			return JsonResponse({'data': context}, status=200)
			# return JsonResponse({
			#   "status": True,
			#   "message": "Successfully Logged In!"
			# }, status=200)

		# else:
		# 	return JsonResponse({
		# 	"status": False,
		# 	"message": "Failed to Login, check your email/password."
		# 	}, status=401)
		else:
			context['login'] = 'unlogin'
			return JsonResponse({'data': context}, status=500)

	context['login'] = 'unlogin-not-POST-req'
	context['type'] = str(request)
	# context['GET'] = str(request.GET)
	return JsonResponse({'data': context}, status=401)

@csrf_exempt
def signup_reg_flutter(request):
	data = {}

	if request.method == 'POST':
		form = RegularSignUpForm(request.POST)
		
		username_exists = User.objects.filter(username=request.POST.get("username")).exists()
		email_exists = User.objects.filter(email=request.POST.get("email")).exists()

		if '@' in request.POST.get("username"):
			data['success'] = False
			data['warning'] = "Username can not contain @."
			return JsonResponse({'data': data}, status=401)
		
		elif username_exists:
			data['success'] = False
			data['warning'] = "Username has already been used."
			return JsonResponse({'data': data}, status=401)
			
		elif email_exists:
			data['success'] = False
			data['warning'] = "Email has already been used."
			return JsonResponse({'data': data}, status=401)
        
		# if name_exists:
		# 	data['success'] = False
		# 	data['warning'] = "Institute name has already been registered."
        
		# elif email_exists:
		# 	data['success'] = False
		# 	data['warning'] =  "Email has already been used."
        
		else:
			if form.is_valid():
				data['success'] = True
				user = form.save(commit=False)
				user.is_regular = True
				user.save()
				return JsonResponse({'data': data}, status=200)
			
			else:
				data['success'] = False
				req = False
				message = ""

				for msg in form.errors: 
					if (form.errors[msg] == "This field is required."): 
						req = True
					else: 
						message += (form.errors[msg] + "\n")

				if (req == True) :
					message = "All fields are required to be filled."
				else :
					message = str(message).replace(".", ".\n")
					message = str(message).replace('<ul class="errorlist">', "")
					message = str(message).replace('<li>', "")
					message = str(message).replace('</li>', "")
					message = str(message).replace('</ul>', "")
					# message = newMessage
                
				data['warning'] = message
				context = {"form": form}

			return JsonResponse({'data': data}, status=401)
		
        # response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
        # return response

	form = RegularSignUpForm()
	data['success'] = False
	data['warning'] = 'Please try again.'
	# return JsonResponse({"instance": "user Dibuat"}, status=200)
	return JsonResponse({'data': data}, status=401)

@csrf_exempt
def signup_bank_flutter(request):
	data = {}

	if request.method == 'POST':
		form = BankSignUpForm(request.POST)
		
		name_exists = User.objects.filter(is_bank=True, name=request.POST.get("name")).exists()
		email_exists = User.objects.filter(email=request.POST.get("email")).exists()
        
		if name_exists:
			data['success'] = False
			data['warning'] = "Institute name has already been registered."
			return JsonResponse({'data': data}, status=401)
        
		elif email_exists:
			data['success'] = False
			data['warning'] =  "Email has already been used."
			return JsonResponse({'data': data}, status=401)
        
		else:
			if form.is_valid():
				data['success'] = True
				user = form.save(commit=False)
				user.is_bank = True
				user.save()
				return JsonResponse({'data': data}, status=200)
			
			else:
				data['success'] = False
				req = False
				message = ""

				for msg in form.errors: 
					if (form.errors[msg] == "This field is required."): 
						req = True
					else: 
						message += (form.errors[msg] + "\n")

				if (req == True) :
					message = "All fields are required to be filled."
				else :
					message = str(message).replace(".", ".\n")
					message = str(message).replace('<ul class="errorlist">', "")
					message = str(message).replace('<li>', "")
					message = str(message).replace('</li>', "")
					message = str(message).replace('</ul>', "")
                
				data['warning'] = message
				context = {"form": form}

			return JsonResponse({'data': data}, status=401)
		
        # response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
        # return response

	form = BankSignUpForm()
	data['success'] = False
	data['warning'] = 'Please try again.'
	return JsonResponse({'data': data}, status=401)

@csrf_exempt
def logout_flutter(request):
	data = json.loads(request.body)
	if request.user.is_authenticated or data['loggedIn']:
		if request.user.is_authenticated:
			logout(request)
		return JsonResponse({"status" : "loggedOut"}, status=200)
	return JsonResponse({"status": "Not yet authenticated"}, status = 401)



