from django.contrib import admin
from .models import Provider,consumer,Service
# Register your models here.
admin.site.register([Provider,consumer,Service])