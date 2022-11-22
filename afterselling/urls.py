from django.urls import path

from . import views

from .views import Encuesta
urlpatterns = [

    path('pventa', views.pventa, name="pventa"),
    path('encuesta', Encuesta.as_view(), name="encuesta"),
]