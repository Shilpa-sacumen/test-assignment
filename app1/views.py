from datetime import datetime

from django.shortcuts import render
from requests import ReadTimeout, Response

from .models import Book, Employee


# Create your views here.
def page1(request):
    date = datetime.now()
    h = int(date.strftime("%H"))

    if h < 12:
        msg = "Morning"
    elif h < 16:
        msg = "Afternoon"
    elif h < 21:
        msg = "Evening"
    else:
        msg = "Night"

    return render(request, "base.html", {"msg": msg, "h": h, "date": date})


def book_info(request):
    """book info

    Args:
        request (_type_): _description_

    Returns:
        html: returns html page
    """
    book = Book.objects.all()
    return render(request, "index.html", {"book": book})


def employee_info(request):
    emp = Employee.objects.all()
    return render(request, "employee.html", {"emp": emp})


def forms_info(request):
    return render(request, "forms.html")
