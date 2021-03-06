from django.urls import path
from . import views

urlpatterns = [
    # read
    path('', views.index, name='index'),
    # create
    path('add/', views.add, name='add'),
    # update
    path('edit/<int:id>/', views.edit, name='edit'),
    # delete
    path('delete/<int:id>/', views.delete, name='delete'),
]
