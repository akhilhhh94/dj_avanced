from django.http import HttpResponse
from django.views.generic import ListView, DetailView
import datetime
from .models import ClassSample


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


class ProxyTestListView(ListView):
    model = ClassSample
    template_name = "class_test_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['title'] = "Proxy test"
        return context
