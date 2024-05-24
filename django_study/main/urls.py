from . import views
from django.urls import path

urlpatterns =[
    path("",views.index),
    path("login/", views.log_reg),
    path("news/", views.news),
    path("about/",views.about),
    path("registration/",views.reg)
]