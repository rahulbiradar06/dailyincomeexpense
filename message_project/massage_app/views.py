from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def msg(request):
    if request.method == 'POST':
        Rname = request.POST.get('uname')
        passw = request.POST.get('passw')
        if(Rname=='rahul' and passw=='123'):
            lmsg = "login successful"
            fmsg = "UserName "+Rname+'  /'+"password "+passw
            context={'fmsg':fmsg, 'lmsg':lmsg}
            return render(request,'message.html',context)
        else:            
            lmsg = "login failed"
            fmsg = "UserName"+Rname+'  '+"password"+passw+' /'+"please enter your valid username or password"
            context={'fmsg':fmsg, 'lmsg':lmsg}
            return render(request,'message.html',context)            
    else:
        fmsg = "this first message is given by render"
        lmsg = "this is login form"
        context={'fmsg':fmsg, 'lmsg':lmsg}
        return render(request,'message.html',context)
    

from django .contrib import messages as m

def msg2(request):
    if request.method == 'POST':
         Rname = request.POST.get('uname')
         passw = request.POST.get('passw')
         if(Rname=='rahul' and passw=='123'):
            m.success(request,'Login succesful')
            m.info(request,'Username '+Rname+'password is '+passw)
            return render(request, 'message2.html')
         else:
             m.error(request,'Login failed')
             m.warning(request,'Username '+Rname+' password is '+passw+''+'please enter valid username or password')
             return render(request,'message2.html')
    else:
        m.add_message(request,m.INFO,'this is django message app information')
        m.add_message(request,m.INFO,'this is login form')
        m.warning(request,'please enter valid username or password')
        
        return render(request, 'message2.html')