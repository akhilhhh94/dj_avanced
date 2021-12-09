from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404
from .models import PostModel

# Create your views here.
def list_all(request):
    qs = PostModel.objects.all()
    template = 'list-all-blogs.html'
    context_dict = {
        'object_list': qs
    }
    return render(request, template, context_dict)

def list_one(request, id=None):
    qs = get_object_or_404(PostModel, id=id)
    template = 'get-single.html'
    context_dict = {
      'data': qs
    }
    return render(request, template, context_dict)