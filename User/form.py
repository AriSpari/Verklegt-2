from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user
