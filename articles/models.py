from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField
# from . import AnyOtherField
from django import forms
# Create your models here.

class User_profile (models.Model):
	user_img=models.ImageField(upload_to='media/profile_images', blank=True)
	user=models.OneToOneField(User)

	# def __str__(self):
	# 	return user.username
#-------------------------------------------------------------------
class Article(models.Model):
	art_title=models.CharField(max_length=255)
	art_content=models.TextField()
	art_img=models.ImageField(max_length=255)
	is_published=models.BooleanField(default=False)
	art_publish_date=models.DateTimeField(auto_now_add=True)
	art_number_views=models.IntegerField(default=0)
	art_user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		 return self.art_title
#-------------------------------------------------------------------

class keywords(models.Model):
	keyword_name=models.CharField(max_length=255)
	keyword_art_id=models.ForeignKey(Article,on_delete=models.CASCADE)
	def __str__(self):
		 return self.keyword_name
#-------------------------------------------------------------------		 

class Comment(models.Model):
	Comment_content=models.TextField()
	is_approved=models.BooleanField(default=0)
	Comment_parent_id=models.ForeignKey('self',on_delete=models.CASCADE,default=-1)
	Comment_user_like=models.ManyToManyField(User)
	Comment_art_id=models.ForeignKey(Article,on_delete=models.CASCADE)
	def __str__(self):
		 return self.Comment_content
#-------------------------------------------------------------------		 

class  Banwords(models.Model):
	banword_name=models.CharField(max_length=255)
	def __str__(self):
		 return self.banword_name

#-------------------------------------------------------------------

class Emotions(models.Model):
	emotion_letter=models.CharField(max_length=255)
	emotion_img=models.CharField(max_length=255)
	def __str__(self):
		 return self.emotion_letter
#-------------------------------------------------------------------
# class CaptchaTestForm(forms.Form):
#     myfield = AnyOtherField()
#     captcha =CaptchaField()

#-------------------------------------------------------------------

# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)