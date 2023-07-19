from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from app.forms import ProductForms


def IndexView(request):
    return render(request=request,
                  template_name='app/index.html')

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



