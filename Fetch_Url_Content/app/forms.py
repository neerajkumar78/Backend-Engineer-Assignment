from django import forms
#from authapp.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    username=forms.CharField(label='username', required=True, widget=forms.TextInput(attrs={'placeholder': 'mysuperusername690'}))
    #email=forms.CharField(label='email', widget= forms.EmailInput(attrs={'placeholder':'mysupermail@mail.com'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder':'eg. X8df!90EO'}))
    confirmpassword = forms.CharField(label='confirm_password', widget=forms.PasswordInput(attrs={'placeholder':'eg. X8df!90EO'}))
    class Meta():
        model = User
        fields = ('username','password')