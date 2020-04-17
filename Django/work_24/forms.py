from django import forms


class SendEmailForm(forms.Form):
    receiver = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField()
