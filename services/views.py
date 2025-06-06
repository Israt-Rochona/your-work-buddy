from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate , logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.db.models import QuerySet
from django.contrib.auth.decorators import login_required
from django.db.models import Avg


from django.core.mail import send_mail
from django.conf import settings

def about_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"""
        New contact form submission:

        Name: {name}
        Email: {email}
        Message:
        {message}
        """

        send_mail(
            subject="New Contact Form Submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,                   # Sender
            recipient_list=['yourworkbuddyofficial@gmail.com'],       # Receiver
            fail_silently=False,
        )

        return render(request, 'services/About_us.html', {'success': True})

    return render(request, 'services/About_us.html' ,{ 'success': False})


# Create your views here.
def home(request):
    return render (request,template_name='services/home.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"""
        Contact form message from:

        Name: {name}
        Email: {email}
        Message:
        {message}
        """

        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['yourworkbuddyofficial@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'services/contact_us.html', {'success': True})

    return render(request, 'services/contact_us.html', {'success': False})


def get_help(request):
    return render (request,template_name='services/help.html')


def service(request):
    # Fetch all services initially
    services = Service.objects.all()

    # Check if it's a POST request with a search query
    if request.method == 'POST':
        search_query = request.POST.get('search', '').lower()  # Get the search term
        services = services.filter(service_name__icontains=search_query)  # Filter services based on search term

    # Pass the filtered or unfiltered services to the template
    context = {
        'service': services,
    }
    return render(request, template_name='services/service.html', context=context)

def provider(request):
    pro= Provider.objects.all()
    c = {
        'provider':pro,
    }
    return render(request, template_name='services/provider.html',context=c)

@login_required
def provider_detail(request , id):
    pro= Provider.objects.get(pk=id)
    reviews = Review.objects.filter(provider=pro)
    c = {
        'provider':pro,
        'reviews': reviews,
    }
    return render(request, template_name='services/provider_details.html',context=c)

@login_required
def receiver(request):
    pro= consumer.objects.all()
    c = {
        'consumer':pro,
    }
    return render(request, template_name='services/service_receiver.html',context=c)

@login_required
def receiver_detail(request, id):

    try:
        cons = consumer.objects.get(user__id=id)  # Using the related User model's ID
        c = {
            'consumer': cons,
        }
        return render(request, template_name='services/consumer_detail.html', context=c)
    
    except consumer.DoesNotExist:
        # Handle the case where the consumer does not exist
        messages.error(request, "Consumer not found.")
        return redirect('home')  # Redirect to home or an appropriate page


@login_required
def AddNewProvider(request) :
    form = ProviderForm()
    if request.method == 'POST' :
        form = ProviderForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render (request,template_name='services/provider_form.html' , context= context)

@login_required
def AddNewReceiver(request) :
    form = ConsumerForm()
    if request.method == 'POST':
        form =ConsumerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render (request,template_name='services/consumer_form.html' , context= context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a dashboard or home page after successful login
            return redirect('profile')  # Replace 'dashboard' with your desired URL name
        else: 
            messages.error(request, "Invalid username or password")
    return render(request, 'services/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type = request.POST['user_type']  # For CustomUser field

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        User = get_user_model()  # Get the custom user model dynamically
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(
            username=username,
            password=password,
            user_type=user_type,
        )
        user.save()

        if user_type == 'provider':
            provider = Provider(
                user=user,  # Required field
                provider_name=None,
                provider_id=None,
                skills=None,
                certification=None,
                employement_type=None,
                rating=None,
                total_work=None,
                nid=None,
                contact_info=None,
                location=None
            )
            provider.save() # Save the provider instance after linking to user
            
        elif user_type == 'customer':
            cons = consumer(
            user=user,  # Required field
            consumer_id=None,
            consumer_name=None,
            email=None,
            contact_info=None,
            location=None,
            nid=None
            )
            cons.save()  # Save the consumer instance after linking to user
            try:
                saved_consumer = consumer.objects.get(user=user)  # Fetch the consumer instance from the database
                print("Consumer saved: ", saved_consumer)
            except consumer.DoesNotExist:
                print("Consumer does not exist in the database!")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            messages.error(request, "Invalid user type!")
            return redirect('register')

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'services/register.html')


def logout_view(request):
    logout(request)  # This will log out the user
    return redirect('home')


@login_required
def profile_view(request):
    # Check if the logged-in user is a provider or a consumer
    user_type = request.user.user_type

    if user_type == 'provider':
        # Fetch the provider object for the logged-in user
        provider = Provider.objects.get(user=request.user)

        if request.method == 'POST':
            try:
                # Update the provider profile
                provider.provider_name = request.POST['provider_name']
                provider.provider_id = request.POST['provider_id']
                provider.skills = request.POST['skills']
                provider.certification = 'certification' in request.POST
                provider.employement_type = request.POST['employement_type']
                provider.rating = 0
                provider.total_work = 0
                provider.nid = request.POST['nid']
                provider.contact_info = request.POST['contact_info']
                provider.location = request.POST['location']
                
                # Handle picture upload
                if 'picture' in request.FILES:
                    new_picture = request.FILES['picture']
                    if provider.picture:  # Delete the old image if exists
                        provider.picture.delete(save=False)
                    provider.picture = request.FILES['picture']
                
                provider.save()
                messages.success(request, "Provider profile updated successfully!")
                return redirect('profile')  # Redirect to profile page to show updated data
            except Exception as e:
                # Print the exception
                print(f"An error occurred: {e}")

        return render(request, 'services/provider_profile.html', {'provider': provider})

    elif user_type == 'customer':
        # Fetch the consumer object for the logged-in user
        cons = consumer.objects.get(user=request.user)

        if request.method == 'POST':
            # Update the consumer profile
            cons.consumer_name = request.POST['consumer_name']
            cons.consumer_id = request.POST['consumer_id']
            cons.email = request.POST['email']
            cons.contact_info = request.POST['contact_info']
            cons.location = request.POST['location']
            cons.nid = request.POST['nid']
            
            # Handle picture upload
            if 'picture' in request.FILES:
                new_picture = request.FILES['picture']
                if cons.picture:  # Delete the old image if exists
                    cons.picture.delete(save=False)
                cons.picture = request.FILES['picture']
            
            cons.save()
            messages.success(request, "Consumer profile updated successfully!")
            return redirect('profile')  # Redirect to profile page to show updated data

        return render(request, 'services/consumer_profile.html', {'consumer': cons})


@login_required
def service_detail(request , id) :
    pro= Service.objects.get(pk=id)
    c = {
        'service':pro,
    }
    try:
        return render(request, template_name='services/service_detail.html',context=c)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error rendering service detail: {e}")
        return render(request, template_name='services/home.html')



@login_required
def job_status(request):
    # Fetch the service history for the logged-in user

    service_history = ServiceHistory.objects.filter(user=request.user)
    if not isinstance(service_history, QuerySet):
        service_history = ServiceHistory.objects.none()
    
    return render(request, 'services/job_status.html', {'service_history': service_history})


@login_required
def add_service_history(request, service_id):
    # Get the service object
    service = get_object_or_404(Service, id=service_id)

    # Create a new ServiceHistory entry
    ServiceHistory.objects.create(user=request.user, service=service, status='waiting')

    return redirect('job_status')


@login_required
def active_schedule(request):
    # Fetch all approved services from the ServiceHistory model
    active_services = ServiceHistory.objects.filter(user=request.user,status="approved").select_related('service')
    
    context = {
        'active_services': active_services,
    }
    return render(request, 'services/active_schedule.html', context)


@login_required
def post_job(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        description = request.POST.get('description')
        rate_per_hour = request.POST.get('rate_per_hour')
        duration = request.POST.get('duration')
        service_date = request.POST.get('service_date')
        location = request.POST.get('location')

        # Create a new Service instance
        try:
            Service.objects.create(
                service_name=service_name,
                description=description,
                rate_per_hour=float(rate_per_hour),
                duration=int(duration),
                service_date=service_date,
                location=location,
                posted_by=request.user  # Associate with the logged-in user
            )
        except Exception as e:
            print(f"Error while creating service: {e}")
            return render(request, 'services/post_job.html', {'error': str(e)})

        return redirect('service')  # Redirect to the homepage or another page after posting

    return render(request, 'services/post_job.html')


@login_required
def requests_view(request):
    # Get all services posted by the current consumer
    posted_services = Service.objects.filter(posted_by=request.user, hide=False)
    
    # Prepare context data with the services and their applied providers
    services_with_applications = []
    
    for service in posted_services:
        # Get all the providers who have applied for this service
        applied_providers = ServiceHistory.objects.filter(service=service, status='waiting')
        
        # Collect the provider user details (i.e., the providers who applied)
        provider_list = [Provider.objects.get(user=application.user) for application in applied_providers]
        
        
        # Add service and the list of applied providers to context
        services_with_applications.append({
            'service': service,
            'applied_providers': provider_list,
        })
    
    context = {
        'services_with_applications': services_with_applications,
    }
    
    return render(request, 'services/requests.html', context)



def approve_provider(request, service_id, provider_id):
    try:
        # Fetch the service and provider
        service = get_object_or_404(Service, id=service_id)
        provider = get_object_or_404(Provider, id=provider_id)

        # Find the ServiceHistory entry for the provider's application
        service_history = ServiceHistory.objects.get(service=service, user=provider.user)

        # Update the status to 'approved'
        service_history.status = 'approved'
        service_history.save()

        # Increase the provider's total_work by 1
        provider.total_work += 1
        provider.save()

        # Remove the service from the Service table (since it's been approved)
        service.hide = True
        service.save()

        # Redirect to the Scheduled Services page
        return redirect('scheduled_services')

    except ServiceHistory.DoesNotExist:
        messages.error(request, "Service history not found for this provider.")
        return redirect('requests')
    except Exception as e:
        messages.error(request, f"Error approving provider: {e}")
        return redirect('requests')
    

@login_required
def scheduled_services(request):
    try:
        # Fetch all approved ServiceHistory entries for services posted by the current user
        service_history = ServiceHistory.objects.filter(
            status='approved', 
            service__posted_by=request.user
        ).select_related('service', 'user__provider')

        services = [
            {
                'service': entry.service,
                'provider': entry.user.provider,
            }
            for entry in service_history
        ]

        context = {'services': services}
        return render(request, 'services/scheduled_services.html', context)

    except Exception as e:
        messages.error(request, f"Error fetching scheduled services: {e}")
        return render(request, 'services/error.html', {'error_message': str(e)})
    

@login_required
def rate_provider(request, provider_id, service_id):
    provider = get_object_or_404(Provider, id=provider_id)
    service = get_object_or_404(Service, id=service_id)
    cons = get_object_or_404(consumer, user=request.user)

    if request.method == "POST":
        try:
            rating = float(request.POST['rating'])
            remarks = request.POST.get('remarks', '')
            review_text = request.POST.get('review', '')

            # Prevent duplicate rating
            existing_review = Review.objects.filter(
                provider=provider,
                service=service,
                consumer=cons
            ).first()

            if existing_review:
                messages.warning(request, "You have already submitted a review for this service.")
                return redirect('scheduled_services')

            # Create new review
            Review.objects.create(
                provider=provider,
                service=service,
                consumer=cons,
                rating=rating,
                remarks=remarks,
                review=review_text,
            )

            # Recalculate provider's average rating
            avg_rating = Review.objects.filter(provider=provider).aggregate(avg=Avg('rating'))['avg'] or 0
            provider.rating = round(avg_rating, 2)
            provider.save()

            # Update service history status to 'rated'
            service_history = ServiceHistory.objects.get(service=service, user=provider.user)
            service_history.status = 'rated'
            service_history.save()

            messages.success(request, "Rating submitted successfully!")
            return redirect('make_payment', service_id=service.id, provider_id=provider.id)

        except Exception as e:
            messages.error(request, f"Error submitting rating: {e}")
            return redirect('rate_provider', provider_id=provider_id, service_id=service_id)


    return render(request, 'services/rate_provider.html', {'provider': provider, 'service': service})


@login_required
def cancel_service(request, service_id, provider_id):
    try:
        service = get_object_or_404(Service, id=service_id)
        provider = get_object_or_404(Provider, id=provider_id)

        service_history = ServiceHistory.objects.get(service=service, user=provider.user)

        # Reverse approval
        if service_history.status == 'approved':
            service_history.status = 'cancelled'
            service_history.save()

            provider.total_work = max(0, provider.total_work - 1)  # avoid negative
            provider.save()

            service.hide = False
            service.save()

            messages.success(request, "Service has been cancelled successfully.")
        else:
            messages.warning(request, "Service was not in approved state.")

        return redirect('scheduled_services')

    except ServiceHistory.DoesNotExist:
        messages.error(request, "Service history not found.")
        return redirect('scheduled_services')
    except Exception as e:
        messages.error(request, f"Error cancelling service: {e}")
        return redirect('scheduled_services')


@login_required
def make_payment(request, service_id, provider_id):
    service = get_object_or_404(Service, id=service_id)
    provider = get_object_or_404(Provider, id=provider_id)

    total_payment = round(service.rate_per_hour * service.duration, 2)
    provider_share = round(total_payment * 0.9, 2)
    company_cut = round(total_payment * 0.1, 2)

    if request.method == "POST":
        # Transfer funds
        provider.wallet_balance += provider_share
        provider.save()

        ServiceHistory.objects.filter(service=service, user=provider.user).update(
            status='completed',
            earned_amount=provider_share
        )

        messages.success(request, f"Payment successful. ${provider_share} added to provider's wallet.")
        return redirect('scheduled_services')

    return render(request, 'services/make_payment.html', {
        'service': service,
        'provider': provider,
        'total_payment': total_payment,
        'provider_share': provider_share,
        'company_cut': company_cut,
    })



@login_required
def wallet_view(request):
    provider = get_object_or_404(Provider, user=request.user)

    history = ServiceHistory.objects.filter(
        user=request.user,
        status='completed'
    ).select_related('service').order_by('-created_at')

    total = provider.wallet_balance

    return render(request, 'services/wallet.html', {
        'provider': provider,
        'history': history,
        'total_balance': total
    })
