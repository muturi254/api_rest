from django.urls import path

from e_api import views

urlpatterns = [
    path('', views.ListCategory.as_view(), name="index"),
    path('<pk>/', views.DetailCategory.as_view(), name="category-details"),
    path('books', views.ListBook.as_view(), name="list-books"),
    path('books/<pk>/', views.DetailBook.as_view(), name="book-details"),
    path('product', views.ListProduct.as_view(), name="list-product"),
    path('product/<pk>/', views.DetailProduct.as_view(), name="product-details"),
]