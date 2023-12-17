from django import forms

from slider.models import Picture


class PictureForm(forms.ModelForm):
    author = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Picture
        fields = ["file", "author"]
