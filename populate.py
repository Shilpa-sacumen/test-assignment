import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')
django.setup()


from app1.models import *
from faker import Faker
from random import *



fake=Faker()
def populate(n):
    for i in range(n):
        fempno=randint(1001,9999)
        fename=fake.name()
        fsal=randint(100000,200000)
        fjob=fake.city()
        emp_record=Employee.objects.get_or_create(Empno=fempno,Ename=fename,sal=fsal,job=fjob)

populate(40)