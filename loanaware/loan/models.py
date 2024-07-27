from django.db import models
import datetime
from django.contrib.auth.models import User
class business(models.Model):
   name=models.CharField(max_length=150,null=False,blank=False)
   details=models.CharField(max_length=2000,null=False,blank=False)
   interest=models.IntegerField(null=False,blank=False,default=0)
   amount=models.FloatField(null=False,blank=False,default=1)
   benifit=models.CharField(max_length=2000,null=False,blank=False)
   eligible=models.CharField(max_length=2000,null=False,blank=False)
   application=models.CharField(max_length=2000,null=False,blank=False)
   documents=models.CharField(max_length=2000,null=False,blank=False)
   status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
   create_at=models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.name

class Education(models.Model):
   name=models.CharField(max_length=150,null=False,blank=False)
   details=models.CharField(max_length=2000,null=False,blank=False)
   interest=models.IntegerField(null=False,blank=False,default=0)
   amount=models.FloatField(null=False,blank=False,default=1)
   benifit=models.CharField(max_length=2000,null=False,blank=False)
   eligible=models.CharField(max_length=2000,null=False,blank=False)
   application=models.CharField(max_length=2000,null=False,blank=False)
   documents=models.CharField(max_length=2000,null=False,blank=False)
   status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
   create_at=models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.name
   
class others(models.Model):
   name=models.CharField(max_length=150,null=False,blank=False)
   details=models.CharField(max_length=2000,null=False,blank=False)
   interest=models.IntegerField(null=False,blank=False,default=0)
   amount=models.FloatField(null=False,blank=False,default=1)
   benifit=models.CharField(max_length=2000,null=False,blank=False)
   age_eligibility=models.IntegerField(null=False,blank=False,default=0)
   eligible=models.CharField(max_length=2000,null=False,blank=False)
   application=models.CharField(max_length=2000,null=False,blank=False)
   documents=models.CharField(max_length=2000,null=False,blank=False)
   status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
   create_at=models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.name
   


class loan(models.Model):
   name=models.CharField(max_length=150,null=False,blank=False)
   interest=models.IntegerField(null=False,blank=False,default=0)
   amount=models.FloatField(null=False,blank=False,default=1)
   details=models.CharField(max_length=2000,null=False,blank=False)
   benifit=models.CharField(max_length=2000,null=False,blank=False)
   age_eligibility=models.IntegerField(null=False,blank=False,default=0)
   eligible=models.CharField(max_length=2000,null=False,blank=False)
   application=models.CharField(max_length=2000,null=False,blank=False)
   documents=models.CharField(max_length=2000,null=False,blank=False)
   status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
   category=models.CharField(max_length=100,null=False,blank=False,default="-")
   cat=models.IntegerField(null=False,blank=False)
   create_at=models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.name
   
class AddToProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan = models.ForeignKey(loan, on_delete=models.CASCADE)  # Assuming you have a Loan model
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age_eligibility = models.IntegerField(null=True, blank=True)
   