from django.urls import path
from .views import list_all,list_one, add_one

urlpatterns = [
    path('list-all/', list_all, name='list-all'),
    path('list/<int:id>/', list_one, name='list-a-single'),
    path('add/', add_one, name='add-a-single'),
]
