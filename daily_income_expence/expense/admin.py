from django.contrib import admin

# Register your models here.
from expense.models import Expense,expenseForm

class Expadmin(admin.ModelAdmin):
    list_display = ['id','expense','expense_type','expense_date','description','user']


admin.site.register(Expense,Expadmin)
