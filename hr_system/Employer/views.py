from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .decorators import is_human_resources, is_manager, is_employee
from .models import *


# Create your views here.

@login_required(login_url='logini')
@is_employee
def emp_page(request):
    data = {}
    return render(request, 'emp_page.html', data)


@login_required(login_url='logini')
@is_manager
def manager_page(request):
    data = {}
    return render(request, 'manager_page.html', data)


@login_required(login_url='logini')
def see_answer_requests(request):
    data = {}
    return render(request, 'components/see_answer_requests.html', data)


@login_required(login_url='logini')
def manage_holidays(request):
    data = {}
    return render(request, 'manage_holidays.html', data)


@login_required(login_url='logini')
def manage_employees(request):
    data = {}
    return render(request, 'manage_employees.html', data)


@login_required(login_url='logini')
def manage_departments(request):
    data = {}
    return render(request, 'manage_departments.html', data)


@login_required(login_url='logini')
def manage_jobs(request):
    data = {}
    return render(request, 'manage_jobs.html', data)


@login_required(login_url='logini')
@is_human_resources
def hr(request):
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
            if user.is_active:
                login(request, user)
                request.session['id'] = user.id
                print(request.user.id)
                role = UserRole.objects.filter(user=request.user.id)
                ids = [i.role.id for i in role]
                id = min(ids)
                print(id)
                if id == 1:
                    return redirect('hr')
                elif id == 2:
                    return redirect('manager_page')
                elif id == 3:
                    return redirect('emp_page')
            else:
                return HttpResponse('not active')
        else:
            return render(request, 'registration/login.html', data)
    else:
        return render(request, 'registration/login.html', data)


@login_required(login_url='logini')
def logoutUser(request):
    del request.session['id']
    logout(request)
    return redirect('logini')


@login_required(login_url='logini')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    update_session_auth_hash(request, form.user)  # <-- keep the user loged after password change
    return render(request, 'registration/change_password.html', {
        'form': form
    })
