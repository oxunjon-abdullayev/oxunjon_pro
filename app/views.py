from django.shortcuts import render
from django.views.generic import TemplateView


def IndexView(request):
    return render(request=request,
                  template_name='app/index.html')

def addproduct(request):
    return render(request=request,
                  template_name='app/add_product.html')