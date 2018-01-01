"""quotable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from apps.quotes.views import (
    Home, 
    QuotesCreate, 
    AddToFavorite, 
    RemoveToFavorite, 
    UserDetails,
    )

from apps.accounts.views import signup, login_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home, name='home'),
    url(r'^quotes/$', QuotesCreate.as_view(), name='quotes'),
    url(r'^addtofev/(?P<id>[-\w]+)/$', AddToFavorite, name='add-to-fev'),
    url(r'^remfromfev/(?P<id>[-\w]+)/$', RemoveToFavorite, name='remove-to-fev'),
    url(r'^users/(?P<pk>[-\w]+)/$', UserDetails.as_view(), name='users-details'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$',login_view, name='login'),
    url(r'^logout/$',logout_view, name='logout'),
]
