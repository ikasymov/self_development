# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from practice.models import	 Topping, Pizza

# Register your models here.

admin.site.register(Topping)
admin.site.register(Pizza)