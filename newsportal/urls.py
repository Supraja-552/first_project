"""
URL configuration for newsportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from testapp.views import home,movie_news,emp_info,comp_info,customer_form,


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    #path('',home,name='home'),
    path('movie_news/',movie_news,name='movie_news'),
    path('emp_info/',emp_info,name='emp_info'),
    path('com_info/',comp_info,name='comp_info');
path('customerform/',customer_form,name='customerform')
]
