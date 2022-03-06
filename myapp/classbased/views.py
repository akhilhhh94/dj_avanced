from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, RedirectView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import datetime
from .models import ClassSample, ProxyClassSample
from .mixin import TitleMixin


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
