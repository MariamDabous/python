from django.db import models

class TVshowmanager(models.Manager):
    def basic_validator(self,data):
        errors= {}
        if len(data['title']) < 2:
            errors["title"]= 'Title Should be at least 2 characters.'
        if len(data['net']) < 3:
            errors["net"]='Network Should be at least 3 characters.'
        if len(data['desc']) <10:
            errors["desc"]= 'Description Should be at least 10 characters.'
        return(errors)

class TVshow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TVshowmanager()
# Create your models here.
