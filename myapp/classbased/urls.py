from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import getDateTime

urlpatterns = [
    path('/about', TemplateView.as_view(template_name="about_us.html"), name='get_date'),
    path('/about-us', RedirectView.as_view(url="/sample/about")),
    path('/', getDateTime, name='get_date')
]