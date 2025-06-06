from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

def provider_directory_path(instance, filename):
    return f'provider_pictures/{instance.user.id}/{filename}'

def consumer_directory_path(instance, filename):
    return f'consumer_pictures/{instance.user.id}/{filename}'

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('provider', 'Provider'),
        ('customer', 'Customer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='customer')

    def __str__(self):
        return self.username

class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='provider')
    provider_name = models.CharField(max_length=200, blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    skills = models.TextField(max_length=1000, blank=True, null=True)
    certification = models.BooleanField(blank=True, null=True)
    employement_type = models.CharField(max_length=200, blank=True, null=True)
    rating = models.FloatField(default=0)
    total_work = models.IntegerField(default=0)
    nid = models.IntegerField(blank=True, null=True)
    contact_info = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=200, default="Default Location", blank=True, null=True)
    picture = models.ImageField(upload_to=provider_directory_path, blank=True, null=True)
    wallet_balance = models.FloatField(default=0.0)


    def __str__(self):
        return self.provider_name if self.provider_name else "Unnamed Provider"

class consumer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='consumer')
    consumer_id = models.IntegerField(blank=True, null=True)
    consumer_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    contact_info = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    nid = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(upload_to=consumer_directory_path, blank=True, null=True)

    def __str__(self):
        return self.consumer_name if self.consumer_name else "Unnamed Consumer"

class Service(models.Model):
    service_id = models.IntegerField(blank=True, null=True)
    service_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rate_per_hour = models.FloatField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    service_date = models.DateField(default="2024-01-01", blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_services', blank=True, null=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.service_name or "Unnamed Service"

class ServiceHistory(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('rated', 'Rated'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='service_history')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_history')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)
    earned_amount = models.FloatField(default=0.0)


    def __str__(self):
        return f"{self.user.username} - {self.service.service_name} - {self.status}"

class Review(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='reviews')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    consumer = models.ForeignKey(consumer, on_delete=models.CASCADE)
    rating = models.FloatField()
    remarks = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.provider.provider_name} - {self.rating} stars"
