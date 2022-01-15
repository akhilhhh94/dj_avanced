from django.urls import path
from .views import list_all,list_one, add_one, update_one, delete_one

urlpatterns = [
    path('list-all/', list_all, name='list-all'),
    path('list/<int:id>/', list_one, name='list-a-single'),
    path('add/', add_one, name='add-a-single'),
    path('update/<int:id>/', update_one, name='update-a-single'),
    path('delete/<int:id>/', delete_one, name='delete-a-single'),
]
