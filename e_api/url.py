from django.urls import path

from e_api import views

urlpatterns = [
    path('^$', views.index, name="index"),
]