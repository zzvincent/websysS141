from django.db import models

# Create your models here.
class User(models.Model):
	fb_id =  models.CharField(max_length=150,blank=True, null=True)
	fb_access_token = models.CharField(max_length=300,blank=True,null=True)