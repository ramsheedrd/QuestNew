from django import forms
from .models import Products
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class ProductForm(forms.Form):
    name = forms.CharField(label='Name of Product')
    price = forms.IntegerField(widget=forms.TextInput)
    image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('price should be a positive integer')
        return price


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'image', 'description', 'category']
        labels = {'name': 'Name of product'}
        widgets = {'price': forms.TextInput}

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password']
    