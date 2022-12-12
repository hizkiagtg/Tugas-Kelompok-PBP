from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from .forms import *
from accounts.models import User
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

@login_required
def show_profile(request):
    return render(request, 'show_profile.html')

@login_required
def edit_profile(request):
    user = request.user
    form_edit = None
    if user.is_regular:
        if request.method == 'POST':
            form_edit = EditProfileFormReg(request.POST, instance=request.user)
            email_exists = User.objects.filter(email=request.POST.get("email")).exists()
            username_exists = User.objects.filter(username=request.POST.get("username")).exists()

            # if '@' in request.POST.get("username"):
            #     messages.error(request, "Username can't contain @")
            if email_exists:
                messages.error(request, "Email is already used! Use other email.")
            elif username_exists:
                messages.error(request, "Username is already used! Choose other username.")
            elif form_edit.is_valid():
                form_edit.save()
                messages.success(request, "Succesfully Updated Profile!")
                return redirect('for_profile:show_profile')
            else:
                form_edit = EditProfileFormReg(request.POST, instance=request.user,
                initial = {
                "username": form_edit.username,
                "email": form_edit.email,
                "name": form_edit.name,
                "age": form_edit.age,
                "gender": form_edit.gender,
                "city": form_edit.city,
                })

    elif user.is_bank:
        if request.method == 'POST':
            form_edit = EditProfileFormBank(request.POST, instance=request.user)
            email_exists = User.objects.filter(email=request.POST.get("email")).exists()

            if email_exists:
                messages.error(request, "Email is already used! Use other email.")
            elif form_edit.is_valid():
                form_edit.save()
                messages.success(request, "Succesfully Updated Profile!")
                return redirect('for_profile:show_profile')
            else:
                form_edit = EditProfileFormBank(request.POST, instance=request.user,
                initial = {
                "name": form_edit.name,
                "email": form_edit.email,
                "city": form_edit.city,
                "address": form_edit.address,
            })
    return render(request, 'update_profile.html', {'form_edit':form_edit})



# def show_profile_flutter(request):
#     data = User.objects.get(pk=id)
#     return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

@csrf_exempt
def user_json_flutter(request, id_user):
    user = User.objects.get(id=id_user)

    context = {
				"email": user.email, 
				"username": user.username, 
				"name": user.name, 
				"age": user.age, 
				"gender": user.gender, 
				"city": user.city, 
				"address": user.address, 
				"id" : user.id,
                "weight" : user.weight,
                "score" : user.score,
				"is_regular" : user.is_regular, 
				"is_bank" : user.is_bank, 
				"is_superuser": user.is_superuser }

    return JsonResponse({'data': {'data':context}}, status=200)


@csrf_exempt
def edit_reg_flutter(request, id):
    try :
        user = get_object_or_404(User,id=id)
    except:
        print("error")

    context = {}

    if request.method == "POST" :
        
        # username_exists = User.objects.filter(username=request.POST.get("username")).exists()
        # email_exists = User.objects.filter(email=request.POST.get("email")).exists()
        
        # if '@' in request.POST.get("username"):
        #     context['success'] = False
        #     context['warning'] = "Username can not contain @."
        #     return JsonResponse({'data': context}, status=401)
            
        # elif username_exists:
        #     context['success'] = False
        #     context['warning'] = "Username has already been used."
        #     return JsonResponse({'data': context}, status=401)
                
        # elif email_exists:
        #     context['success'] = False
        #     context['warning'] = "Email has already been used."
        #     return JsonResponse({'data': context}, status=401)

        # else:
        newData = json.loads(request.body)
        user.name = newData['name']
        user.username = newData['username']
        user.email = newData['email']
        user.age = newData['age']
        user.gender = newData['gender']
        user.city = newData['city']
        user.save()
        return JsonResponse({"data":"Edit Successful", "status": 200}, status=200)
        
    context["data"] = {
        "name" : user.name,
        "username" : user.username,
        "email" : user.email,
        "age" : user.age,
        "gender" : user.gender,
        "city" : user.city
    }
    
    return JsonResponse({"data":context, "status": 200}, status=200)
    
@csrf_exempt
def edit_bank_flutter(request, id):
    try :
        user = get_object_or_404(User,id=id)
    except:
        print("error")
    context = {}
    if request.method == "POST" :
        # name_exists = User.objects.filter(is_bank=True, name=request.POST.get("name")).exists()
        # email_exists = User.objects.filter(email=request.POST.get("email")).exists()
        
        # if name_exists:
        #     context['success'] = False
        #     context['warning'] = "Institute name has already been registered."
        #     return JsonResponse({'data': context}, status=401)
        
        # elif email_exists:
        #     context['success'] = False
        #     context['warning'] =  "Email has already been used."
        #     return JsonResponse({'data': context}, status=401)

        # else:
        newData = json.loads(request.body)
        user.name = newData['name']
        user.email = newData['email']
        user.city = newData['city']
        user.address = newData['address']
        user.save()
        return JsonResponse({"data":"Edit Successful", "status": 200}, status=200)
    
    context["data"] = {
        "name" : user.name,
        "email" : user.email,
        "city" : user.city,
        "address" : user.address,
    }
    return JsonResponse({"data":context, "status": 200}, status=200)



    

