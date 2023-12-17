from django.shortcuts import render

# Create your views here.

def pdp(request):
    return render(request, "pdp.html")
