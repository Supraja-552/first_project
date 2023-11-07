from django.test import TestCase

from faker import Faker
fake=Faker()
for i in range(100):
    print('Employee Name:',fake.name())
    print('Employee Name:',fake.first_name())
    print('Employee Name:',fake.last_name())
    print('Employee DOB:',fake.date())
    print('Employee ID:',fake.random_number(5))
    print('Employee Mail ID',fake.email())
    print('Employee number:',fake.random_int(min=0,max=9999))
    print(fake.city())
    print('Employee role:',fake.random_element(elements=('software Engineer','Team Lead','Project Lead','project Manager')))
print()