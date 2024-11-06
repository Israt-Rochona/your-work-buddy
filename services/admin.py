from django.contrib import admin
from .models import Service_provider,consumer,Service
# Register your models here.
admin.site.register([Service_provider,consumer,Service])