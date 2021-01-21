from datetime import datetime
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
@is_human_resources
def manage_holidays(request):
    data = {}
    return render(request, 'manage_holidays.html', data)


@login_required(login_url='logini')
@is_human_resources
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
def deleted_users(request):
    data = {}
    return render(request, 'deletedUsers.html', data)


@login_required(login_url='logini')
@is_human_resources
def hr(request):
    data = {}
    return render(request, 'hr_homepage.html', data)


def logini(request):
    data = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                us = Users.objects.get(id=user.id)
                if us.active:
                    login(request, user)
                    request.session['id'] = user.id
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


import xlwt


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['first_name', 'last_name', 'salary', 'phone_no', 'department_id', 'email', 'active']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Users.objects.all().values_list('first_name', 'last_name', 'salary', 'phone_no',
                                           'department_id__department_name', 'email', 'active')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_departments_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="departments.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Departments')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['department_name', 'name', 'surname', 'parent_department']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Departments.objects.all().values_list('department_name', 'manager__first_name', 'manager__last_name',
                                                 'parent_dep__department_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_offical_holidays_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="offical_holidays.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Offical_holidays')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['holiday_name', 'active', 'day']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = OfficalHolidays.objects.all().values_list('holiday_name', 'active_flag', 'day')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# absence rate per user
def export_absence_rate_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="absence_rate.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Absence_rate')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['us', 'us_name', 'us_last_name', 'absence rate in %']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = UserHoliday.objects.all().values_list('us', 'us__first_name', 'us__last_name', 'days_left')
    rows1 = []
    days = 0
    for i in rows:
        u, x, y, z = i
        role = UserRole.objects.filter(user=u)
        ids = [i.role.id for i in role]
        id = min(ids)
        print(id)
        days = Role.objects.get(id=id)
        days = days.max_allowance_no
        print(z)
        print(days)
        z = (days - z) / days * 100
        i = (u, x, y, z)
        rows1.append(i)
    rows = rows1
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# new hires -- this month
def export_new_hires_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="new_hires.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('new_hires')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['first_name', 'last_name', 'department_id', 'email']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Users.objects.all().values_list('first_name', 'last_name', 'department_id', 'email')
    rows1 = []
    for i in rows:
        f, l, h, d, e = i
        if h.month == datetime.now().month and h.year == datetime.now().year:
            i = (f, l, h, d, e)
            rows1.append(i)
    rows = rows1
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# new hires -- this year
def export_new_hires_year_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="new_hires_year.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('new_hires_year')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['first_name', 'last_name', 'department_id', 'email']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Users.objects.all().values_list('first_name', 'last_name', 'department_id', 'email')
    rows1 = []
    for i in rows:
        f, l, h, d, e = i
        if h.year == datetime.now().year:
            i = (f, l, h, d, e)
            rows1.append(i)
    rows = rows1
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# salaries highest to lowest
def export_salary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="salary.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('salary')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['first_name', 'last_name', 'salary']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Users.objects.all().values_list('first_name', 'last_name', 'salary').order_by('-salary')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


from collections import Counter


# reuqest approvers -- who approves the most/least
def export_approvers_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="approvers.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('approvers')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['first_name', 'last_name', 'department', 'approved requests']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    requests = AllowanceRequest.objects.filter(approval_flag=True)
    approvers_list = [i.approver for i in requests]
    c = Counter(approvers_list)
    print(c)
    row1 = []
    rows = Users.objects.all().values_list('id', 'first_name', 'last_name', 'department_id__department_name')
    for i in rows:
        id, f, l, d = i
        x = Users.objects.get(id=id)
        app = list(c.keys())
        if x in app:
            row1.append((f, l, d, c[x]))
    rows = row1
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# reuqest deniers -- who denies the most/least
def export_deniers_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="deniers.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('deniers')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['first_name', 'last_name', 'department', 'denied requests']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    requests = AllowanceRequest.objects.filter(approval_flag=False, checked=True)
    approvers_list = [i.approver for i in requests]
    c = Counter(approvers_list)
    row1 = []
    rows = Users.objects.all().values_list('id', 'first_name', 'last_name', 'department_id__department_name')
    for i in rows:
        id, f, l, d = i
        x = Users.objects.get(id=id)
        app = list(c.keys())
        if x in app:
            row1.append((f, l, d, c[x]))
    rows = row1
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# job positions
def export_job_positions_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="job_positions.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('job_positions')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'surname', 'role']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = UserRole.objects.all().values_list('user__first_name', 'user__last_name', 'role__role')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
