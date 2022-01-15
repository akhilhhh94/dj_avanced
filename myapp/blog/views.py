from multiprocessing import context
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import PostModel
from .forms import PostForms

# Create your views here.
def list_all(request):
    query = request.GET.get("q", None)
    qs = PostModel.objects.all()
    if query is not None:
        # Complex lookups with Q objects
        qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query))
    template = 'list-all-blogs.html'
    context_dict = {
        'object_list': qs,
        'query': query
    }
    return render(request, template, context_dict)

def list_one(request, id=None):
    qs = get_object_or_404(PostModel, id=id)
    template = 'get-single.html'
    context_dict = {
      'data': qs
    }
    return render(request, template, context_dict)


def add_one(request, id=None):
    if request.POST:
        form = PostForms(request.POST)
        if form.is_valid():
            post_data = form.save(commit=False)
            #form.save() is allow to save by considering the forign key relation
            #form.save(commit=False) will return a cleanned model object (save seporately)
            post_data.save()
            messages.success(request, 'Addedd successfully')
            return HttpResponseRedirect('/test-model/list/{id}/'.format(id=post_data.id))
    else:
        form = PostForms()
    # We can avaid if else and pu like form = PostForms(request.POST or None)
    template = 'add-single.html'
    context_dict = {
        "form": form
    }
    return render(request, template, context_dict)


def update_one(request, id=None):
    qs = get_object_or_404(PostModel, id=id)
    form = PostForms(request.POST or None, instance=qs)
    if request.POST:
        if form.is_valid():
            post_data = form.save(commit=False)
            #form.save() is allow to save by considering the forign key relation
            #form.save(commit=False) will return a cleanned model object (save seporately)
            post_data.save()
            messages.success(request, 'Updateds successfully')
            return HttpResponseRedirect('/test-model/list/{id}/'.format(id=post_data.id))
    # We can avaid if else and pu like form = PostForms(request.POST or None)
    template = 'update-single.html'
    context_dict = {
        "form": form
    }
    return render(request, template, context_dict)


def delete_one(request, id=None):
    qs = get_object_or_404(PostModel, id=id)
    form = PostForms(request.POST or None, instance=qs)
    if request.POST:
        qs.delete()
        messages.success(request, 'Deleted successfully')
        return HttpResponseRedirect('/test-model/list-all/')
    # We can avaid if else and pu like form = PostForms(request.POST or None)
    template = 'delete-single.html'
    context_dict = {
        "form": form
    }
    return render(request, template, context_dict)