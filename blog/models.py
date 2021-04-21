from django.db import models

#for Time Zone
from django.utils import timezone

#user table django
from django.contrib.auth.models import User

#post korle POST er jagay niye jabe & bole dibe j url shoobo
from django.urls import reverse

# Create your models here.

class Post(models.Model):      #class dile auto shob data dibe
    title = models.CharField(max_length=100)
    text = models.TextField() 
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    #def get_absolute_url(self):
		#return reverse ('blog-detail', kwargs={'pk':self.pk})