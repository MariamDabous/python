from email.policy import default
from django.db import models
from distutils.log import error
import email
import imp
from django.db import models
import re

from django.core.validators import validate_email

class userManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}
        if len(post_data['fname']) < 2:
            errors['fname']="First name should be at least 2 characters"
        if len(post_data['lname']) < 2:
            errors['lname']="Last name should be at least 2 characters"
        try:
            validate_email(post_data['email'])
        except:
            errors['lname']="email is not valid"
        if len(post_data['pass1']) < 8:
            errors['pass1']="Password should be at least 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if post_data['pass1'] != post_data['pass2']:
            errors['pass2']= "The passwords are not the same"
        if users.objects.filter(email=post_data['email']).exists():
            errors['email']= "Entered email is already exist"
        return(errors)



class users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=255)
    password= models. CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()
    #tree

class TreeManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}
        if len(post_data['spieces']) < 5:
            errors['lname']="species should be at least 5 characters"
        if len(post_data['location']) < 2:
            errors['desc']="Location should be at least 2 characters"
        return(errors)

class Tree(models.Model):
    species= models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    reason = models.TextField(default='i like it')
    user = models.ForeignKey(users, related_name="tree", on_delete = models.CASCADE)
    date_planted = models.DateTimeField()
    objects=TreeManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
