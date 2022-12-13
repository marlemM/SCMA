from django.urls import path
from .views import list_item, create_item, update_item, delete_item

urlpatterns = [
    path('', list_item, name='list_item'),
    path('new', create_item, name='create_item'),
    path('update/<int:id>/', update_item, name='update_item'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
]


# CRUD - CREATE, READ, UPDATE, DELETE