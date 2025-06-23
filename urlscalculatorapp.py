from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculatorappsubmitquery', views.submitquery, name='submitquery'),
]
