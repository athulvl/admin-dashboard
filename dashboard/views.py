from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login')
def index(request):
    return render(request,'admin/index.html')

@login_required(login_url='/admin/login')
def products(request):
    return render(request,'admin/products.html')

def login(request):
    return render(request,'admin/auth/login.html')

def login_user(request):
    if request.method == 'POST':
        next_data = request.POST.get('next',None)
        print(next_data)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('/admin/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/admin/login')

def logout_user(request):
    auth.logout(request)
    return redirect('/admin/login')
