from django import forms
from .models import Product, Profile
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude = ['user', 'slug']

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
			"password": forms.PasswordInput()
		}

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']


class PasswordUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['password']
		widgets = {
			"password": forms.PasswordInput()
		}

class EmailUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email']


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio', 'birthday', 'image']
		widgets = {
			"birthday": forms.DateInput(attrs={"type":"date"})
		}