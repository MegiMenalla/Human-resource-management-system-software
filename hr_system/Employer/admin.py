from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Users)
admin.site.register(Departments)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(AllowanceRequest)
admin.site.register(OfficalHolidays)
admin.site.register(Profile)
