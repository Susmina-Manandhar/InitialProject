from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def response(request):
    return HttpResponse("Hi! You've successfully created Digital Library App Component!")
   
