# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from decimal import Decimal

class Topping(models.Model):
	name = models.CharField(max_length=50)
	balance = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0))


class Pizza(models.Model):
	name = models.CharField(max_length=50)
	toppings = models.ManyToManyField(Topping, related_name='pizzas')

	def __str__(self):
		return '%s, %s' % (self.name, ','.join([i.name for i in self.toppings.all()]))