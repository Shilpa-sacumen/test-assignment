from django.urls import path
from .views import *


urlpatterns=[
    path('',page1),
    path('book_info',book_info),
    path('employee_info',employee_info),
    path('forms_info',forms_info),
]