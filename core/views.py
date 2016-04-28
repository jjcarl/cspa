from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import ProductForm, TreatmentForm
from .models import Product, Treatment


def index(request):
    return render(request, 'home.html', {})


def manage_treatments(request):
    context = dict()
    context['treatments'] = Treatment.objects.filter(active=True)
    context['form'] = TreatmentForm()
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'treatments.html', context)
        context['form'] = form
        context['errors'] = form.errors
        return render(request, 'treatments.html', context)
    else:
        return render(request, 'treatments.html', context)


def manage_products(request):
    context = dict()
    context['products'] = Product.objects.filter(active=True)
    context['form'] = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'products.html', context)
        context['form'] = form
        context['errors'] = form.errors
        return render(request, 'products.html', context)
    else:
        return render(request, 'products.html', context)


def account_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                render(request, 'login.html', {'errors': 'Your account has been disabled, please contact the CSpa'})
        else:
            return render(request, 'login.html', {'errors': 'Your account has been disabled, please contact the CSpa'})
    else:
        return render(request, 'login.html', {})


def account_logout(request):
    logout(request)
    return redirect('/')
