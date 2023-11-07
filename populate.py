import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelprojecct1.settings')
django.setup()
from testapp.models import*
from faker import Faker
from random import*
fake=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=fake.name()
        fesal=randint(10000,20000)
        feadder=fake.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esalary=fesal,eaddress=feadder)
    populate(30)
