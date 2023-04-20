from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun2(request):
	return HttpResponse('<h1>Iam a electrical engineer</h1>')