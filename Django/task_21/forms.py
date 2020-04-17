from django import forms


class UserForm(forms.Form):
    firstname = forms.CharField(max_length=25)
    lastname = forms.CharField(max_length=25)
    age = forms.IntegerField(min_value=1, max_value=100)
    profession = forms.CharField(max_length=255)
