from django.contrib import admin
from testapp.models import Employee,Company
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','salary','eaddress']
admin.site.register(Employee,EmployeeAdmin)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['cname','clocation','cid','no_of_employees']
admin.site.register(Company,CompanyAdmin)
# Register your models here.
