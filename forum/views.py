from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from accounts.models import *
import datetime
import json

@login_required(login_url='accounts:login')
def addQuestion(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('description')
        newQuestion = Question(author=request.user, title=title, body = body, created_at= datetime.date.today())
        newQuestion.save()
        return HttpResponse(serializers.serialize("json",[newQuestion]), content_type="application/json")
    return HttpResponseNotFound()

@csrf_exempt
def addFlutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.get(id=data['user'])
        title = data['title']
        body = data['body']
        newQuestion = Question(author = user, title=title, body = body, created_at= datetime.date.today())
        newQuestion.save()
        return JsonResponse({"instance": "Forum Berhasil Dibuat!"}, status=200)
    
@login_required(login_url='accounts:login')
def addAnswer(request):
    if request.method == "POST":
        body = request.POST.get('body')
        newAnswer = Answer(user=request.user, body = body, created_at = datetime.now())
        newAnswer.save()
        return HttpResponse(serializers.serialize("json",[newAnswer]), content_type="application/json")
    return HttpResponseNotFound()

def questionJson(request):
    questions = Question.objects.all()
    return HttpResponse(serializers.serialize('json', questions), content_type='application/json')


def answerJson(request):
    answer = Answer.objects.all()

    return HttpResponse(serializers.serialize('json', answer), content_type='application/json')

def homePage(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request, 'forum.html', context)

