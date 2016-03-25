from django import forms

from .models import *


class LandingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LandingForm, self).__init__(*args, **kwargs)

        self.fields['email'] = forms.EmailField(
            widget=forms.EmailInput(attrs={
                'class': 'form-control no-border-radius',
                'placeholder': '123@xyz.com',
            })
        )

        self.fields['city'] = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control no border-radius',
                'placeholder': 'Brisbane'
            })
        )

        self.fields['price'] = forms.FloatField(
            widget=forms.TextInput(attrs={
                'class': 'form-control no border-radius',
                'placeholder': '$3.50'
            })
        )

    def clean_email(self):
        try:
            Landed.objects.get(email=self.cleaned_data['email'])
            raise forms.ValidationError('Email has already been signed up')
        except Landed.DoesNotExist:
            pass
        return self.cleaned_data['email']

    # TODO check price float

    def save(self):
        sub = Landed(
            email=self.cleaned_data['email'],
            city=self.cleaned_data['city'],
            price=self.cleaned_data['price']
        )
        sub.save()
