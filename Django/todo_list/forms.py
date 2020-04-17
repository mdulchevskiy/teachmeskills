from django import forms


PRIORITY = [
    (1, 'High'),
    (2, 'Mid'),
    (3, 'low'),
]


class TodoForm(forms.Form):
    activity = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Your activity...',
            'size': '70',
        }),
        error_messages={
            'required': 'Activity is required!',
            'max_length': 'Your activity is too long!',
        },
    )
    priority = forms.CharField(
        widget=forms.Select(choices=PRIORITY),
        error_messages={
            'required': 'Selection is required!',
        },
    )

    def as_myp(self):
        return self._html_output(
            normal_row='<p style="margin-top: 5px; margin-bottom: 5px;">%(label)s %(field)s %(help_text)s</p>',
            error_row='<span style="color: red;">%s</span>',
            row_ender='',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)
