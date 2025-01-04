from django.contrib import admin
from .models import Provider,consumer,Service,CustomUser,ServiceHistory
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register([Provider,consumer,Service,ServiceHistory])