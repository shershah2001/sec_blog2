from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class Signup(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','pasword1','password2']
        labels = {"email":"Email"}
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
    
class Login(AuthenticationForm):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=250)
    
    label = ['username','password']
    widgets ={
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'})
    }

