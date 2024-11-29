from django.forms import ModelForm
from .models import *
class ProviderForm(ModelForm):
    class Meta :
        model = Provider
        # fields = ['provider_name', 'skills', 'employement_type', 'location']
        fields = '__all__'


class ConsumerForm(ModelForm):
    class Meta:
        model = consumer
        fields = '__all__'


