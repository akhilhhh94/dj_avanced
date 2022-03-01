from django.urls import path
from django.views.generic import TemplateView
from .views import getDateTime

urlpatterns = [
    path('/about', TemplateView.as_view(template_name="about_us.html"), name='get_date'),
    path('/', getDateTime, name='get_date')
]