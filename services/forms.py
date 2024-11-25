from django.forms import ModelForm
from .models import *
class ProviderForm(ModelForm):
    class Meta :
        model = Provider
        fields = '__all__'


class ConsumerForm(ModelForm):
    class Meta:
        model = consumer
        fields = '__all__'


