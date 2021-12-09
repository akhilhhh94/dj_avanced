from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def page1(request):
    return HttpResponse("Here's the text of the Web page.")