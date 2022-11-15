from django.shortcuts import render

# Create your views here.

def pventa(request):
    return render(request, "afterselling/pventa.html")