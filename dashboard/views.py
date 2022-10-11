from django.shortcuts import redirect, render

def index(request):
    return render(request,'admin/index.html')

def products(request):
    return render(request,'admin/products.html')
