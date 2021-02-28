from django import forms
from django.contrib.auth.models import User
from doctor.models import DrProfileInfo

class DrForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')

class DrProfileForm(forms.ModelForm):
    class Meta():
        model = DrProfileInfo
        fields = ('specialisation','description','profile_pic')
