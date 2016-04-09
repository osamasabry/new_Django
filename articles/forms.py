from django.db import models
from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm
# from captcha.fields import CaptchaField 
# from .models import Article
# from .models import User_profile
from .models import * 

#class form to forgetPassword Form (osama)
class forgetPassForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True,placeholder="Enter Mail Here")))

class confirmPassForm(forms.Form):
	code = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=10,placeholder="Enter Code Here")))

class confirmUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=10,placeholder="Enter User Name Here")))

class resetForm(forms.Form):
    reset = forms.CharField(widget=forms.PasswordInput(attrs=dict(max_length=10,placeholder="Enter New Password")))
    resetconfirm=forms.CharField(widget=forms.PasswordInput(attrs=dict(max_length=10,placeholder="Enter Confirm Password")))

#-------------------------------------------------------------------

class ArticleForm(forms.ModelForm):
	
	class Meta:
		model = Article
		# fields = ['']
		exclude = ['art_number_views']
#-------------------------------------------------------------------

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    # user_img = forms.FileField(
    #     label='Select a file',
    # )
    class Meta:
        model = User_profile
        # fields = ('another field', '','')
        fields = ['user_img']

#-------------------------------------------------------------------        

# class CaptchaTestModelForm(forms.ModelForm):
#     captcha = CaptchaField()
#     class Meta:
#         model = CaptchaTestForm
