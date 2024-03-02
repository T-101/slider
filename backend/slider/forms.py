from django import forms
from django.contrib.auth.forms import AuthenticationForm as DjangoAuthenticationForm, UsernameField

from slider.models import Picture


class PictureForm(forms.ModelForm):
    author = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Picture
        fields = ["file", "author"]


class AuthenticationForm(DjangoAuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username:', "class": "form-control"}))
