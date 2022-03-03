from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import getDateTime, TestListView, TestDetailed, ProxyTestListView

urlpatterns = [
    path('/proxy-tests', ProxyTestListView.as_view()),
    path('/tests', TestListView.as_view()),
    path('/test/<int:pk>/', TestDetailed.as_view()),
    path('/about', TemplateView.as_view(template_name="about_us.html"), name='get_date'),
    path('/about-us', RedirectView.as_view(url="/sample/about")),
    path('/', getDateTime, name='get_date')
]