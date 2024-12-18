from django.contrib import admin
from .models import Employee,Book

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('Empno','Ename','sal','job')
class BookAdmin(admin.ModelAdmin):
    list_display=('number','title','author','published_date')




admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Book,BookAdmin)
