from django import forms
#from authapp.models import UserProfileInfo
from django.contrib.auth.models import User
from .models import Content
class UserForm(forms.ModelForm):
    username=forms.CharField(label='username', required=True, widget=forms.TextInput(attrs={'placeholder': 'mysuperusername690'}))
    #email=forms.CharField(label='email', widget= forms.EmailInput(attrs={'placeholder':'mysupermail@mail.com'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder':'eg. X8df!90EO', 'id':'password', 'onkeyup':'check();','name':'password',}))
    confirmpassword = forms.CharField(label='confirm_password', widget=forms.PasswordInput(attrs={'placeholder':'eg. X8df!90EO', 'id':'confirm_password', 'onkeyup':'check();','name':'confirm_password',}))
    class Meta():
        model = User
        fields = ('username','password')
class URLForm(forms.ModelForm):
    url = forms.URLField(label='Enter URL', required=True, widget=forms.URLInput(attrs={'placeholder': 'https://www.mywebsite.com/'}))
    class Meta():
        model=Content
        fields=['url']

