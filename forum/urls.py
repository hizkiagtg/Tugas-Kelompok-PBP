from django.urls import path
from forum.views import homePage
from forum.views import addQuestion
from forum.views import addFlutter
from forum.views import addFlutterRep
from forum.views import addAnswer
from forum.views import questionJson
from forum.views import answerJson

urlpatterns = [
    path('', homePage, name = 'forum'),
    path('addQuestion/', addQuestion, name='addQuestion'),
    path('json/', questionJson, name='json'),
    path('answerJson/', answerJson, name='answerJson'),
    path('addFlutter/', addFlutter, name='addFlutter'),
    path('addFlutterRep/', addFlutterRep, name='addFlutterRep'),
    path('addAnswer/', addAnswer, name='addAnswer'),
]
