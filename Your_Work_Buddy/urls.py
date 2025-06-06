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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', s_views.login_view, name='login'),
    path('', s_views.home, name='home'),
    path('about_us/', s_views.about_us, name='about_us'),
    path('contact_us/', s_views.contact_us, name='contact_us'),
    path('help/', s_views.get_help, name='help'),
    path('service/', s_views.service, name='service'),
    path('register/', s_views.register_view, name='register'),
    path('logout/', s_views.logout_view, name='logout'),
    path('provider/',s_views.provider, name= 'provider'),

    path('profile/', s_views.profile_view, name='profile'),
    path('service/<int:id>', s_views.service_detail, name='service_detail'),
    path('job_status/', s_views.job_status, name='job_status'),
    path('add_service_history/<int:service_id>/', s_views.add_service_history, name='add_service_history'),
    path('active_schedule/', s_views.active_schedule, name='active_schedule'),

    path('post-job/', s_views.post_job, name='post_job'),
    path('requests/', s_views.requests_view, name='requests'),
    path('approve_provider/<int:service_id>/<int:provider_id>/', s_views.approve_provider, name='approve_provider'),
    path('scheduled_services/', s_views.scheduled_services, name='scheduled_services'),

    path('rate/<int:provider_id>/<int:service_id>/', s_views.rate_provider, name='rate_provider'),

    path('provider/<int:id>/', s_views.provider_detail, name='provider_detail'),
    path('receiver/<int:id>/', s_views.receiver_detail, name='receiver_detail'),
    path('receiver/', s_views.receiver, name='receiver'),

    path('signup/provider/', s_views.AddNewProvider, name='new_provider'),
    path('signup/receiver/', s_views.AddNewReceiver, name='new_receiver'),

<<<<<<< HEAD
    path('cancel-service/<int:service_id>/<int:provider_id>/', s_views.cancel_service, name='cancel_service'),
    # path('make-payment/<int:service_id>/<int:provider_id>/', views.make_payment, name='make_payment'),  # placeholder
    path('make-payment/<int:service_id>/<int:provider_id>/', s_views.make_payment, name='make_payment'),
    path('wallet/', s_views.wallet_view, name='wallet'),


=======
>>>>>>> 4126b94b043fda0ca389497191cff73936285a0f
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
