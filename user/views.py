from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import user
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as loginn
from django.contrib.auth.decorators import login_required
import random
import time

# Create your views here.
def home(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserCreationForm()
    return render(request,'index.html',{"form":form})
@login_required()
def userlist(request):
    user=request.user
    all_users=User.objects.all()
    liste=[]
    for i in all_users:
        liste.append(i.username)
    test=random.choice(liste)
    print(test)
    return render(request,'userlist.html',{'user':user,'test':test})
@login_required()
def user(request,username):
    all_users=User.objects.all()
    liste=[]
    for i in all_users:
        liste.append(i.username)
    test=random.choice(liste)
    print(test)
    t={"user":User.objects.get(username=username),'test':test}
    return render(request,'user.html',t)
def login(request):
    if request.method=='POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            loginn(request, user)
            return redirect('http://127.0.0.1:8000/user'+'/'+user.username)
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})
