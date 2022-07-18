import imghdr
import re
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from __init__ import *

@login_required(login_url='login')
def homePage(request):
    context = {}

    shops = Shop.objects.filter(creators=request.user)

    context['shops'] = shops
    return render(request, 'index.html', context)

def userAuth(request):

    if request.method == 'POST':
        if request.POST['firstName'] != 'error':
            phone = str(request.POST.get('phone-number')).strip()
            firstName = str(request.POST.get('firstName')).strip()
            lastName = str(request.POST.get('lastName')).strip()
            password = '@Qwerty11'
            username = str(firstName + phone + lastName)

            email = firstName + lastName + '1234@gmail.com'
            new_user = User.objects.create_user(
                username=username,
                first_name=firstName, 
                last_name=lastName,
                password=password, 
                email=email, 
                phone=phone)

            login(request, new_user)

            return redirect('homePage')
        else:
            phone = request.POST.get('phone-number')

        try:

            user = User.objects.get(phone=phone)
            
            login(request, user)

            return redirect('homePage')
        except User.DoesNotExist:
            context = {
                'phone' : phone
            }

            return render(request, 'register.html', context)

    return render(request, 'auth-page.html')


def createShop(request):
    if request.method == 'POST' and request.FILES['i']:
        name = request.POST['n']
        password = request.POST['p']
        description = request.POST['d']
        img = request.FILES['i']
        viloyat = Viloyat.objects.get(pk=request.POST['v'])
        tuman = Tuman.objects.get(pk=request.POST['t'])

        new_shop = Shop.objects.create(
            host=request.user,
            name=name,
            description=description,
            password=password,
            image=img,
            viloyat=viloyat,
            tuman=tuman,
        )

        new_shop.creators.add(request.user)
        
        return redirect('homePage')


    viloyatlar = Viloyat.objects.all()
    tumanlar = Tuman.objects.all()
    context = {
        'v' : viloyatlar,
        't' : tumanlar,
    }
    return render(request, 'createShop.html', context)
