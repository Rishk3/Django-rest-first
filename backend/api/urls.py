# All urls will be declared here
from django.urls import path

from . import views

urlpatterns=[
    path('',views.api_home)
]
