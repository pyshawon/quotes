# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


# Create your models here.

class Quote(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quoted_by = models.CharField(max_length=200, validators=[MinLengthValidator(3,message="More then 3 Charactor")])
	message = models.TextField(validators=[MinLengthValidator(10,message="More then 10 Charactor")])
	

	def __unicode__(self):
		return self.quoted_by

	class Meta:
		ordering = ["-id"]


class FavoriteQuote(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
	is_favorite = models.BooleanField(default=True)

	def __unicode__(self):
		return "%s"%(self.is_favorite)


	class Meta:
		ordering = ["-id"]
