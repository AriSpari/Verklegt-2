from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']  #
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput()
        }# add your fields
