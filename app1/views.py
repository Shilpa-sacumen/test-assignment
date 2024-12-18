"""Views file"""
from datetime import datetime

from django.shortcuts import render


from .models import Book, Employee


# Create your views here.
def page1(request):
    """page1

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
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
    """book_info

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    book = Book.objects.all() #pylint: disable=no-member
    return render(request, "index.html", {"book": book})


def employee_info(request):
    """employee_info

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    emp = Employee.objects.all() #pylint: disable=no-member
    return render(request, "employee.html", {"emp": emp})


def forms_info(request):
    """forms_info

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, "forms.html")
