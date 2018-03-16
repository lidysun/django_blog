# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog import models
# Create your views here.

def index(request):
	# return HttpResponse('hello django')
	if request.method=='POST':
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		models.UserInfo.objects.create(user = username,pwd = password)

	user_list = models.UserInfo.objects.all()
	return render(request,'index.html',{'data':user_list})

def movie(request):
	movies = models.DoubanMovie.objects.all()
	return render(request,'movie.html',{'movies':movies})


