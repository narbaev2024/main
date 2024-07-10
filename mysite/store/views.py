from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
    product = Product.objects.all()
    return render(request, 'product_list.html', {'product': product})


def product_detail(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('product_list')

    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})


def product_update(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect('product_list')

    else:
        form = ProductForm()
    return render(request, 'product_update.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})