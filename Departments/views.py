from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def response (request):
    return HttpResponse("Departments is activated")