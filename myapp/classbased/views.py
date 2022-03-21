import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, View, RedirectView, CreateView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import DeleteView, UpdateView

from .mixin import TitleMixin
from .models import ClassSample, ProxyClassSample
from .forms import ClassAndUserTestForm, FormTestForm


def getDateTime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class TestListView(ListView):
    # Important
    # app_name = classbased
    # model = ClassSample
    # view_name = ListView
    # default name = <app_name>/<model>_<view_name>.html (classbased/classsample_list.html)
    model = ClassSample
    template_name = "class_test_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = " test"
        print(context)
        return context


class TestDetailed(DetailView):
    model = ClassSample

    # Just override the core get_context_data() to print it // no need it actually
    def get_context_data(self, **kwargs):
        contect = super(TestDetailed, self).get_context_data(**kwargs)
        print(contect)
        return contect


# login requred decorator is here with mixin example
class ProxyTestListView(LoginRequiredMixin, TitleMixin, ListView):
    login_url = '/index/'
    redirect_field_name = 'index'
    title = "this titles"

    # one methord of login requred decorator is here
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProxyTestListView, self).dispatch(*args, **kwargs)

    model = ProxyClassSample
    template_name = "class_test_list.html"


class MultipleObjectListingExample(MultipleObjectMixin, View):
    queryset = ClassSample.objects.filter(pk__gte=2)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        template_name = "class_test_list.html"
        return render(request, template_name=template_name, context=context)


class MyRedirectView(RedirectView):
    pattern_name = 'my-text'

    def get_redirect_url(self, *args, **kwargs):
        data = get_object_or_404(ClassSample, pk=kwargs['pk'])
        # data.updateCounter Or something like
        return super().get_redirect_url(*args, **kwargs)


class UserWithFormSample(LoginRequiredMixin, CreateView):
    form_class = ClassAndUserTestForm
    template_name = 'user-with-form.html'
    # Or put absolute URL in the model
    success_url = "/akhil"

    def form_valid(self, form):
        # form.cleaned_data
        temp = form.save(commit=False)
        temp.user = self.request.user
        temp.save()
        return super().form_valid(form)


class TestUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    success_url = "/sample/tests"
    form_class = ClassAndUserTestForm
    template_name = "update.html"
    success_message = "%(name)s was updated successfully"
    model = ClassSample


class TestDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    success_url = "/sample/tests"
    model = ClassSample
    success_message = "%(name)s was created successfully"
    template_name = "deelete.html"


class FormTest(CreateView):
    form_class = FormTestForm
    template_name = 'form-sample.html'
    success_url = "/sample/sample-form-test"

