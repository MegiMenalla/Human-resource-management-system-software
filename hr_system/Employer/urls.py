from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path(r'hr/', views.hr, name="hr"),
    path(r'logini/', views.logini, name="logini"),
    path(r'logoutUser/', views.logoutUser, name="logoutUser"),
    path(r'change_password/', views.change_password, name="change_password"),
    path(r'manage_departments/', views.manage_departments, name="manage_departments"),
    path(r'manage_employees/', views.manage_employees, name="manage_employees"),
    path(r'manage_holidays/', views.manage_holidays, name="manage_holidays"),
    path(r'emp_page/', views.emp_page, name="emp_page"),
    path(r'manager_page/', views.manager_page, name="manager_page"),
    path(r'see_answer_requests/', views.see_answer_requests, name="see_answer_requests"),
    path(r'manage_jobs/', views.manage_jobs, name="manage_jobs"),
    path(r'deleted_users/', views.deleted_users, name="deleted_users"),

    path(r'export_users_xls/', views.export_users_xls, name='export_users_xls'),
    path(r'export_departments_xls/', views.export_departments_xls, name='export_departments_xls'),
    path(r'export_offical_holidays_xls/', views.export_offical_holidays_xls, name='export_offical_holidays_xls'),
    path(r'export_absence_rate_xls/', views.export_absence_rate_xls, name='export_absence_rate_xls'),
    path(r'export_new_hires_xls/', views.export_new_hires_xls, name='export_new_hires_xls'),
    path(r'export_new_hires_year_xls/', views.export_new_hires_year_xls, name='export_new_hires_year_xls'),
    path(r'export_salary_xls/', views.export_salary_xls, name='export_salary_xls'),
    path(r'export_approvers_xls/', views.export_approvers_xls, name='export_approvers_xls'),
    path(r'export_deniers_xls/', views.export_deniers_xls, name='export_deniers_xls'),
    path(r'export_job_positions_xls/', views.export_job_positions_xls, name='export_job_positions_xls'),

    #  submit email form
    path('reset_password/',
         auth_view.PasswordResetView.as_view(template_name="registration/password_reset.html"),
         name="reset_password"),
    #  render the success msg
    path('reset_password_sent/',
         auth_view.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
         name="password_reset_done"),
    #  link password success form to email
    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    #  password successfully changed msg
    path('reset_password_complete/',
         auth_view.PasswordResetCompleteView.as_view(template_name="registration/password_reset_end.html"),
         name="password_reset_complete"),

]
