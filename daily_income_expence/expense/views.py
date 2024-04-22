
from django.shortcuts import render,redirect

from account.views import get_balance

from .models import expenseForm,Expense
from django.contrib.auth.models import User


def addexpense(request):
    uid=request.session.get('uid')
    if request.method == 'POST':
        # f=expenseForm(request.POST)
        expense=request.POST.get('expense')
        if get_balance(request)>int(expense):
            expense_type=request.POST.get('expense_type')
            expense_date=request.POST.get('expense_date')
            description=request.POST.get('description')
            exp=Expense()
            exp.expense=expense
            exp.expense_type=expense_type
            exp.expense_date=expense_date
            exp.description=description
            exp.user=User.objects.get(id=uid)
            exp.save()
            return redirect('/') 
        else:
            f=expenseForm
            context={'form':f,'exp_msg':'Insufficient balance bhai paise kamale'}
            return render(request,'addexpense.html',context)
    else:
        f = expenseForm
        context = {'form': f}
        return render(request, 'addexpense.html', context)
    

def expense_list(request):
    uid=request.session.get('uid')
    explist=Expense.objects.filter(user=uid)
    expt=set()
    for i in explist:
        expt.add(i.expense_type)
    context={'expe':explist, 'expt':expt}
    return render(request, 'expense_list.html', context)

def delete_expense(request,id):
    exp=Expense.objects.get(id=id)
    exp.delete()
    return redirect('/')

def expense_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    expe=Expense.objects.filter(user=uid,description__contains=srch)
    context={'expe':expe}
    return render(request, 'expense_list.html', context)

def sort_by_expense_type(request,extc):
    uid=request.session.get('uid')
    explist=Expense.objects.filter(user=uid)
    expt=set()
    for i in explist:
        expt.add(i.expense_type)
    # for data based on category
    explist=Expense.objects.filter(user=uid,expense_type=extc)

    context={'expe':explist,'expt':expt}
    return render(request, 'expense_list.html', context)
