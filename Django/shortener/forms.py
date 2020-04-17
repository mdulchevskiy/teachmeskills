from django import forms


CHOICES = [
    ('auto', 'Automatically'),
    ('manual', 'Manual'),
]


class ShortenerForm(forms.Form):
    long_url = forms.URLField(
        max_length=1000,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'https://www.youtube.com/',
            'size': '70',
        }),
        error_messages={
            'required': 'Link is required \u21b4',
            'invalid': 'Enter a valid URL \u21b4',
        },
    )
    shortening_method = forms.ChoiceField(
        widget=forms.Select,
        choices=CHOICES,
        initial='auto',
        error_messages={
            'required': 'Shortening method is required \u21b4',
        },
    )
    manual_shortening = forms.CharField(
        max_length=255,
        required=False,
    )

    def as_myp(self):
        return self._html_output(
            normal_row='<p style="margin-top: 5px; margin-bottom: 5px;">%(label)s %(field)s %(help_text)s</p>',
            error_row='<span style="color: red;">%s</span>',
            row_ender='',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)
