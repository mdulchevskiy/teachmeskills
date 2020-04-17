from django import forms


SPECIES_CHOICES = (
    ("1", "Cat"),
    ("2", "Dog"),
)
TYPES_CHOICES = (
    ("1", "JPG"),
    ("2", "GIF"),
    ("3", "PNG"),
)


class SearchForm(forms.Form):
    species = forms.ChoiceField(choices=SPECIES_CHOICES)
    type = forms.ChoiceField(choices=TYPES_CHOICES)


class SendEmailForm(forms.Form):
    sender = forms.EmailField()
    receiver = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField()
