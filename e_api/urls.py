from django.urls import path

from e_api import views

urlpatterns = [
    path('^$', views.ListCategory.as_view(), name="index"),
]