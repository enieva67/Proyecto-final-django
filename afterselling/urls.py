from django.urls import path

from . import views

urlpatterns = [

    path('pventa', views.pventa, name="pventa"),

]