from django.forms import ModelForm
from store.models import contact
class ContactForm(ModelForm):
   class Meta:
        model= contact
        fields='__all__'
