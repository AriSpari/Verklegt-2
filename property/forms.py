# property/forms.py
from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'property_address', 'city', 'postalcode', 'property_price',
            'property_type', 'description', 'roomcount', 'bedroomcount',
            'bathroomcount', 'squaremeters', 'image_cover'
        ]
        widgets = {
            'property_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postalcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('Villa', 'Villa'),
                ('Cottage', 'Cottage'),
                ('Single-family', 'Single-family')
            ]),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'roomcount': forms.NumberInput(attrs={'class': 'form-control'}),
            'bedroomcount': forms.NumberInput(attrs={'class': 'form-control'}),
            'bathroomcount': forms.NumberInput(attrs={'class': 'form-control'}),
            'squaremeters': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_cover': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }