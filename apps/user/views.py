from django.shortcuts import (
		render, redirect, reverse, 
		get_object_or_404
	)
from django.contrib.auth import (
		authenticate, login, logout
	)
from django.http import (
		Http404, HttpResponse, JsonResponse
	)
from django.utils.translation import ugettext_lazy as _

from django.views import generic
from django.conf import settings
from django.contrib import messages

from apps.user.models import User
from . import forms


# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')

class LogoutView(generic.RedirectView):
	url = settings.HOMEPAGE

	def get(self, request, *args, **kwargs):
		logout(request)
		return super().get(request, *args, **kwargs)

class LoginView(generic.TemplateView):
	template_name = 'user/login.html'
	form = forms.LoginForm

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['form'] = self.form
		context['name'] = _('Log in') 
		return context

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(settings.HOMEPAGE)
		return super().get(request, *args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		form = self.form(request.POST)

		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')

			user = authenticate(email = email, password = password)				

			if user:
				login(request, user)
				if form.cleaned_data.get('remember_me'):
					self.request.session.set_expiry(settings.REMEMBER_ME)
				return redirect('user:update')
				
		return self.hasError(request, form, *args, **kwargs)
	
	def hasError(self, request, form, *args, **kwargs):
		form.add_error('email', _('Incorrect email address or password.'))
		form.add_error('password', '')
		context = self.get_context_data(*args, **kwargs)
		context['form'] = form
		return render(request, self.template_name, context)


class ProfileUpdateView(generic.UpdateView):
	model = User
	form_class = forms.ProfileUpdateForm
	template_name = 'user/user_update.html'

	def get_object(self):
		return self.request.user
	
	def get_success_url(self):
		return reverse('user:update')
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['name'] = _('Update')
		context['initialized'] = True
		return context