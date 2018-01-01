# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import QuoteForm
from .models import Quote, FavoriteQuote
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


from ..accounts.forms import SignUpForm, UserLoginForm

# Create your views here.

def Home(request):
	if request.user.is_authenticated:
		return redirect('quotes')
	context = {
	"login": UserLoginForm(),
	"reg": SignUpForm(),
	"title":"Login/Registration"
	}
	return render(request, "quotes/home.html", context)


class QuotesCreate(CreateView):
	form_class = QuoteForm
	template_name = 'quotes/quotes.html'
	success_url = "/quotes/"

	def form_valid(self, form, *args, **kwargs):
		form.instance.user = self.request.user
		return super(QuotesCreate, self).form_valid(form, *args, **kwargs)


	def get_context_data(self, *args, **kwargs):
		context = super(QuotesCreate, self).get_context_data(*args, **kwargs)
		fev_item = []
		quotes_fev = FavoriteQuote.objects.filter(user=self.request.user, is_favorite=True)
		for item in quotes_fev:
			fev_item.append(item.quote.id)
		quotes = Quote.objects.exclude(id__in=fev_item)
		context['title'] = "Quotes"
		context['quotes'] = quotes
		context['quotes_fev'] = quotes_fev

		
		return context


def AddToFavorite(request, id=None):
	quote = Quote.objects.get(id=id)
	FavoriteQuote.objects.create(user=request.user, quote=quote, is_favorite=True)
	return HttpResponseRedirect(reverse("quotes"))


def RemoveToFavorite(request, id=None):
	quote = FavoriteQuote.objects.get(quote__id=id, is_favorite=True)
	quote.is_favorite=False
	quote.save()
	return HttpResponseRedirect(reverse("quotes"))


class UserDetails(DetailView):
	model = User
	template_name = 'quotes/user-details.html'

	def get_context_data(self, *args, **kwargs):
		context = super(UserDetails, self).get_context_data(*args, **kwargs)
		context['user_quotes'] = Quote.objects.filter(user__id=self.kwargs['pk'])
		context['userinfo'] = User.objects.get(id=self.kwargs['pk'])
		return context



