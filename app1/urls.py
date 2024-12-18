from django.urls import path
from app1.views import page1, book_info, employee_info, forms_info


urlpatterns = [
    path("", page1),
    path("book_info", book_info),
    path("employee_info", employee_info),
    path("forms_info", forms_info),
]
