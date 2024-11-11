from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Service_provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    provider_name = models.CharField(max_length=200)
    provider_id = models.IntegerField()
    skills = models.TextField(max_length=1000)
    certification = models.BooleanField(blank=True,null=True)
    employement_type = models.CharField(max_length=200)

    def __str__(self):
        return self.provider_name

class consumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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
    provider_id =  models.ForeignKey(Service_provider,on_delete=models.CASCADE,blank=True,null=True)
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    rate_per_hour = models.FloatField(max_length=300)
    duration = models.IntegerField()



