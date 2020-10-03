from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User



class UserUpdateForm(ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','first_name','email']
