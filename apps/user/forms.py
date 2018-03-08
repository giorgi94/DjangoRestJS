from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Account

class LoginForm(forms.Form):

	email = forms.CharField(widget = forms.EmailInput(attrs={
		'class':"form-control",
		}), label=_('Email'))

	password = forms.CharField(widget = forms.PasswordInput(attrs={
		'class':"form-control",
		# 'maxlength' : ,
		# 'minlength' : 6,
		}), label=_('Password'))
	
	remember_me = forms.BooleanField(widget=forms.CheckboxInput(),
			label=_('Remember me'), required=False)


	def add_prefix(self, field_name):
		field_name = 'login-%s' % field_name 
		return super().add_prefix(field_name)

	# def clean_email(self):
	# 	email = self.cleaned_data['email']
	# 	user = Account.objects.filter(email=email)
	# 	if not user.count():
	# 		raise forms.ValidationError(_('Incorrect email address or password.'))
	# 	return user[0]

class ProfileUpdateForm(forms.ModelForm):


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

	class Meta:
		model = Account
		fields = [
			'first_name',
			'last_name',
		]


	
