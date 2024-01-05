from django.shortcuts import render, redirect
from back_office.products.models import Product
from .custom_widgets import CartAmountForm

# Create your views here.

def pdp(request, pk):
    product = Product.objects.get(id=pk)
    #form = CartAmountForm
    return render(request, "pdp.html", 
    {'product': product})
    #{'form': form})
    

