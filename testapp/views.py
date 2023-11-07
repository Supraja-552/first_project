from django.shortcuts import render
from testapp.models import Employee,Company
from testapp.forms import Customerform


# from django.http import HttpResponse
def home(request):
    return render(request,'homa.html')
def movie_news(request):
    news1='In Telugu Devadas movie is not Good'
    news2 = 'In Telugu Devadas movie is not Good'
    news3 = 'In Telugu Devadas movie is not Good'
    news4 = 'In Telugu Devadas movie is not Good'
    news5='In Telugu Devadas movie is not Good'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}

    return render(request,'about.html',my_dict)
def  emp_info(request):
    employees=Employee.objects.all()
    return render(request,'results.html',{'employees':employees})
def comp_info(request):
    companys=Company.objects.all()
    return render(request,'results.html',{'companys':companys})
def customer_form(request):
    customer=Customerform()
    return render(request,'index.html',{'customer':customer})
