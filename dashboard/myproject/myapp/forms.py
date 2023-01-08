from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):


    password1 = forms.CharField(label='Enter Your Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:

        model = User
        
        fields = ['username','first_name','last_name','email']

        widgets = {

            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),

        }

class LogInForm(AuthenticationForm):

    username = forms.CharField(label='Enter Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:

        model=User

        fields = ['username','password'] 



