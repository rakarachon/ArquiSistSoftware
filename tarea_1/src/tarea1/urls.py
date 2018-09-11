from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_comment', views.new_comment, name='new_comment'),
]
