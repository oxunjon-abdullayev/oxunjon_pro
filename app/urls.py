from django.urls import path

from app.views import IndexView, addproduct, deleteproduct

urlpatterns = [
    path('', IndexView, name='index'),
    path('addproduct/', addproduct, name='add-product'),
    path('delete-product/<int:product_id>', deleteproduct, name='delete-product')
]