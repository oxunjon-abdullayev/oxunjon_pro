from django.urls import path

from app.views import IndexView, addproduct

urlpatterns = [
    path('', IndexView, name='index'),
    path('addproduct/', addproduct, name='add-product')
]