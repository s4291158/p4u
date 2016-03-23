from django import forms

from .models import *


class SubForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SubForm, self).__init__(*args, **kwargs)

        self.fields['email'] = forms.EmailField(
            error_messages={
                'required': 'give us something to work with.'
            },
            widget=forms.EmailInput(attrs={
                'class': 'form-control no-border-radius',
                'placeholder': 'Notify me by email when it goes live',
            })
        )

    def clean_email(self):
        try:
            Subscribed.objects.get(email=self.cleaned_data['email'])
            raise forms.ValidationError('Email has already been signed up')
        except Subscribed.DoesNotExist:
            pass
        return self.cleaned_data['email']

    def save(self):
        sub = Subscribed(email=self.cleaned_data['email'])
        sub.save()
