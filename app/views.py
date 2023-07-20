from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from app.forms import ProductForms
from app.models import ProductModel


def IndexView(request):
    products = ProductModel.objects.all()
    product = request.GET.get("query", '')
    return render(request=request,
                  template_name='app/index.html',
                  context={"products":products,
                           "product":product})

def addproduct(request):
    if request.method == "POST":
        form = ProductForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = ProductForms()
    return render(request=request,
                  template_name='app/add_product.html',
                  context={"form":form})


def deleteproduct(request, product_id):
    product = ProductModel.objects.filter(id=product_id).first()
    if product:
        product.delete()
        return redirect('index')

