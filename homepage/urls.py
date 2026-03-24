#
# This file tells Django that you want to serve the index view from your service's root URL.

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]