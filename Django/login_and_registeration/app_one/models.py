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
        if len(post_data['pass1']) < 2:
            errors['pass1']="Password should be at least 8 characters"
        if post_data['pass1'] != post_data['pass2']:
            errors['pass2']= "The passwords are not the same"
        return(errors)



class users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=255)
    password= models. CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

