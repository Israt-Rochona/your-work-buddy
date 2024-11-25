"""
URL configuration for Your_Work_Buddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import urlpatterns
from django.contrib import admin
from django.urls import path
from services import views as s_views
from.import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', s_views.home, name='home'),
    path('about_us/', s_views.about_us, name='about_us'),
    path('help/', s_views.get_help, name='help'),
    path('service/', s_views.service, name='service'),
    path('signup/', s_views.signup, name='signup'),
    path('provider/',s_views.provider, name= 'provider'),

    path('login/', s_views.provider, name='login'),
    path('provider/<int:id>/', s_views.provider_detail, name='provider_detail'),
    path('receiver/<int:id>/', s_views.receiver_detail, name='receiver_detail'),
    path('receiver/', s_views.receiver, name='receiver'),

    path('signup/provider/', s_views.AddNewProvider, name='new_provider'),
    path('signup/receiver/', s_views.AddNewReceiver, name='new_receiver'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
