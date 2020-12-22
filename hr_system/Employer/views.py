from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import CreateUserForm
from .models import Profil


# Create your views here.


# @api_view(['GET'])
def test(request):
    return HttpResponse('hi')


def home(request):
    data = {

    }
    return render(request, 'hr_homepage.html', data)


def logini(request):
    data = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Emri ose kodi eshte gabim!')
            return render(request, 'registration/login.html', data)
    else:
        return render(request, 'registration/login.html', data)


def logoutUser(request):
    logout(request)
    return redirect('logini')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Profil.objects.create(
                user=user,
            )
            messages.success(request, 'Profili u kijua: ')
            messages.success(request, username)
            return redirect('logini')

    data = {
        'form': form,

    }
    return render(request, 'registration/register.html', data)
