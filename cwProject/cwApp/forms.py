from .models import ContactModel
from django import forms


# model bound form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
