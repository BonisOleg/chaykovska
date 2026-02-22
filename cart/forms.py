from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phone', 'email', 'address')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('First Name'),
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Last Name'),
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('+380 XX XXX XXXX'),
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('your@email.com'),
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Delivery address'),
                'rows': 4,
            }),
        }
