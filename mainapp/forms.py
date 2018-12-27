from django import forms
from .models import Order

class ContactForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('username', 'email', 'phone', 'text')
