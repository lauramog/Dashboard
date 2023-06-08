from django.urls import path
from . import views

urlpatterns = [

    path('year', views.create_accident)
]