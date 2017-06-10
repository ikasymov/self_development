# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

import random
from decimal import Decimal

from django.shortcuts import render
from django.db.models import F
from django.db import transaction
from django.conf import settings
from django.conf.urls.static import static

from practice.models import Topping, Pizza


def base_page(request):
	context = {}
 	context['anymore'] = 's'
	context['old'] = Pizza.objects.all()
	return render(request, 'base.html', context)