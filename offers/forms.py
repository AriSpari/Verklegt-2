from django import forms
from .models import Offers
from django.utils import timezone
from datetime import timedelta


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ['offer_price', 'expire_date']
        widgets = {
            'expire_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default expire date to 7 days from now, with time included
        self.fields['expire_date'].initial = timezone.now() + timedelta(days=7)
