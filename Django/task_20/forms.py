from django import forms


class AviaSales(forms.Form):
    name = forms.CharField(max_length=20)
    departure = forms.CharField(max_length=30)
    arrival = forms.CharField(max_length=30)
    amount = forms.IntegerField(min_value=0)
    date = forms.DateField(input_formats=('%d.%m.%Y',))

    date.widget.attrs.update({'placeholder': 'DD.MM.YYYY'})
