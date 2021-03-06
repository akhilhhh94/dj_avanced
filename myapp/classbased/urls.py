from django.urls import path
from django.views.generic import TemplateView, RedirectView

from .views import (
    getDateTime, TestListView, TestDetailed, ProxyTestListView, MultipleObjectListingExample, MyRedirectView, UserWithFormSample, TestDeleteView, TestUpdateView, FormTest
)

urlpatterns = [
    path('/sample-form-test', FormTest.as_view()),
    path('/proxy-tests', ProxyTestListView.as_view()),
    path('/form-use-test', UserWithFormSample.as_view()),
    path('/multi-tests', MultipleObjectListingExample.as_view()),
    path('/tests', TestListView.as_view()),
    path('/test/<int:pk>/', TestDetailed.as_view(), name='my-text'),
    path('/test/<int:pk>/update', TestUpdateView.as_view(), name='my-text-update'),
    path('/test/<int:pk>/delete', TestDeleteView.as_view(), name='my-text-delete'),
    path('/tt/<int:pk>/', MyRedirectView.as_view()),
    path('/about', TemplateView.as_view(template_name="about_us.html"), name='get_date'),
    path('/about-us', RedirectView.as_view(url="/sample/about")),
    path('/', getDateTime, name='get_date')
]