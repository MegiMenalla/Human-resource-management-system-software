from django.http import HttpResponse
from Employer.models import UserRole


def is_human_resources(view_func):
    def wrapper_func1(request, *args, **kwargs):
        me = UserRole.objects.filter(user=request.user.id)
        ids = [i.role.id for i in me]
        id = min(ids)
        if id == 2 or id == 3:
            return HttpResponse('You are not a human resources user!')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func1


def is_manager(view_func):
    def wrapper_func2(request, *args, **kwargs):
        me = UserRole.objects.filter(user=request.user.id)
        ids = [i.role.id for i in me]
        id = min(ids)
        if id == 1 or id == 3:
            return HttpResponse('You are not a manager user!')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func2


def is_manager_or_hr(view_func):
    def wrapper_func2(request, *args, **kwargs):
        me = UserRole.objects.filter(user=request.user.id)
        ids = [i.role.id for i in me]
        id = min(ids)
        if id == 3:
            return HttpResponse('An employee user cannot acces this page!')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func2


def is_employee(view_func):
    def wrapper_func3(request, *args, **kwargs):
        me = UserRole.objects.filter(user=request.user.id)
        ids = [i.role.id for i in me]
        id = min(ids)
        if id == 1 or id == 2:
            return HttpResponse('You are not an employee user!')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func3
