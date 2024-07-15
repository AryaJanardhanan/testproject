from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

#Django form
class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='enter your email')


#Model form   
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Userr
        fields = ['name', 'password', 'email']


# user registrtn & login
class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class Itemsform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'des', 'image', 'document']








