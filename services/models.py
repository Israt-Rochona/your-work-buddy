from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class Provider(models.Model):
    provider_name = models.CharField(max_length=200)
    provider_id = models.IntegerField()
    skills = models.TextField(max_length=1000)
    certification = models.BooleanField(blank=True,null=True)
    employement_type = models.CharField(max_length=200)
    rating = models.FloatField(blank=True,null=True)
    total_work = models.IntegerField(blank=True,null=True)
    nid = models.IntegerField(blank=True,null=True)
    contact_info= models.IntegerField(blank=True,null=True)
    location = models.CharField(max_length=200,default="Default Location")
    # password = models.CharField(max_length=128,default="1234")

    # def set_password(self, raw_password):
    #     """Hashes the password and saves it to the model."""
    #     self.password = make_password(raw_password)
    #     self.save()
    #
    # def check_password(self, raw_password):
    #     """Checks the raw password against the hashed password."""
    #     return check_password(raw_password, self.password)

    def __str__(self):
        return self.provider_name

class consumer(models.Model):
    consumer_id = models.IntegerField()
    consumer_name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_info= models.IntegerField()
    location = models.CharField(max_length=200)
    nid = models.IntegerField()

    def __str__(self):
        return self.consumer_name


class Service(models.Model):
    consumer_id = models.ForeignKey(consumer,on_delete=models.CASCADE,blank=True,null=True)
    provider_id =  models.ForeignKey(Provider,on_delete=models.CASCADE,blank=True,null=True)
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    rate_per_hour = models.FloatField(max_length=300)
    duration = models.IntegerField()



