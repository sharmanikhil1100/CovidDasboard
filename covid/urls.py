from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.home),
    path('get-all', views.get_data),
    path('insert', csrf_exempt(views.insert)),
]