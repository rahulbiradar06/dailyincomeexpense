from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def adduser(request):
    if request.method == 'POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserCreationForm
        context={'form': f}
        return render(request, 'adduser.html')