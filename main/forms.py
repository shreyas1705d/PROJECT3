from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

class CustomerForm(forms.ModelForm):
    PRODUCT_CHOICES = [
        ('product1', 'Product 1'),
        ('product2', 'Product 2'),
        ('product3', 'Product 3'),
    ]
    product = forms.ChoiceField(choices=PRODUCT_CHOICES)

    class Meta:
        model = Customer
        fields = ['name', 'email', 'product', 'message']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'service_quality', 'product_quality', 'delivery_speed', 'overall_experience', 'additional_comments']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['name'].initial = user.username