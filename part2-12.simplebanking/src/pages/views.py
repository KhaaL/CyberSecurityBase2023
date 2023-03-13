from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



@login_required
def addView(request):
	return redirect('/')


@login_required
def homePageView(request):
	return render(request, 'pages/index.html')
