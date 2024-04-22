from django.shortcuts import render,redirect
from .models import Income, IncomeForm
from django.contrib.auth.models import User


def addincome(request):
    uid=request.session.get('uid')
    if request.method == 'POST':
        # f=IncomeForm(request.POST)
        income=request.POST.get('income')
        income_type=request.POST.get('income_type')
        income_date=request.POST.get('income_date')
        description=request.POST.get('description')
        inc=Income()
        inc.income=income
        inc.income_type=income_type
        inc.income_date=income_date
        inc.description=description
        inc.user=User.objects.get(id=uid)
        inc.save()
        return redirect('/') 
    else:
        f = IncomeForm
        context = {'form': f}
        return render(request, 'addincome.html', context)
    
def income_list(request):
    uid=request.session.get('uid')
    inclist=Income.objects.filter(user=uid)
    context={'incl':inclist}
    return render(request, 'income_list.html', context)

def delete_income(request,id):
    inc=Income.objects.get(id=id)
    inc.delete()
    return redirect('/')

def income_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    incl=Income.objects.filter(user=uid,description__contains=srch)
    context={'incl':incl}
    return render(request, 'income_list.html', context)