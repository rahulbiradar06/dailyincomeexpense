"""
URL configuration for daily_income_expence project.

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
from. import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('income',v.addincome, name='inc'),
    path('income_list',v.income_list, name='list'),
    path('delete/<int:id>',v.delete_income, name='delete'),
    path('income_search',v.income_search, name='income_search'),
]
