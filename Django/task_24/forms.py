from django import forms


class ImageResolutionForm(forms.Form):
    width = forms.IntegerField(required=True)
    height = forms.IntegerField(required=True)


class ContactForm(forms.Form):
    receiver = forms.EmailField(required=True)
    image = forms.URLField()
    subject = forms.CharField(required=True)
