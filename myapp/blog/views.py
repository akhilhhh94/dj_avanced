from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import PostModel

# Create your views here.
def page1(request):
    qs = PostModel.objects.all()
    template = 'list-blog.html'
    context_dict = {
        'object_list': qs
    }
    return render(request, template, context_dict)