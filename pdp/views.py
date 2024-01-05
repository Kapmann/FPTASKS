from django.shortcuts import render
from back_office.products.models import Product
from .custom_widgets import CartAmountForm

# Create your views here.

def pdp(request):
    product_list = Product.objects.all()
    #form = CartAmountForm
    return render(request, "pdp.html", 
    {'product_list': product_list})
    #{'form': form})
    

