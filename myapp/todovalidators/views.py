from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import todo
from .forms import TodoForms

def add(request):

    form = TodoForms(request.POST or None)
    # We can avaid if else and pu like form = PostForms(request.POST or None)

    if form.is_valid():
        todo = form.save(commit=False)
        todo.save()
        return HttpResponse("Saved SuccessFully")


    template = 'add.html'
    context_dict = {
        "form": form
    }
    return render(request, template, context_dict)
    
# Create your views here.
