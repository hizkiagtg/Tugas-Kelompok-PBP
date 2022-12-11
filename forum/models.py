from django.db import models
from accounts.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default = "")
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    def get_responses(self):
        return self.responses.filter(parent=None)



class Answer(models.Model):
    author = models.ForeignKey(User, null=False, on_delete = models.CASCADE)
    username = models.CharField(max_length=100, default = "")
    parent = models.ForeignKey(Question, null=False, on_delete = models.CASCADE, related_name='responses')
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body    
    