from django import forms

from .models import *


class LandingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LandingForm, self).__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(
            max_length=40,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bruce Wayne'
            })
        )

        self.fields['email'] = forms.EmailField(
            widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '123@xyz.com'
            })
        )

        self.fields['suburb'] = forms.CharField(
            max_length=40,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Brisbane CBD'
            })
        )

        self.fields['price'] = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '$15'
            })
        )

        self.fields['role'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(attrs={
                'type': 'hidden',
            })
        )

    def clean_email(self):
        try:
            Landed.objects.get(email=self.cleaned_data['email'])
            raise forms.ValidationError('Email has already been signed up')
        except Landed.DoesNotExist:
            pass
        return self.cleaned_data['email']

    def clean_price(self):
        price = self.cleaned_data['price']
        try:
            price = float(price.replace('$', ''))
        except ValueError:
            raise forms.ValidationError('Please fix price format')
        return price

    def clean_role(self):
        role = self.cleaned_data['role']
        if role != 'parker' and role != 'parkee':
            raise forms.ValidationError('Incorrect role input')
        return role

    def save(self):
        sub = Landed(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            suburb=self.cleaned_data['suburb'],
            price=self.cleaned_data['price'],
            role=self.cleaned_data['role'],
        )
        sub.save()
