from django.shortcuts import render
from app.forms import UserForm, URLForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .function import get_content
import urllib.request
from .models import Content
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'app/index.html')
def register(request):
    registered = False
    message=None
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)      
        if user_form.is_valid():
            user = user_form.save()
            print("user form is valid")
            user.set_password(user.password)
            user.save()
            registered = True
            return render(request, 'app/login.html', {})
        else:
            username = request.POST.get('username')
            try:
                user = User.objects.exclude(pk=request.user.pk).get(username=username)
                message='username already exists'
            except User.DoesNotExist:
                print(user_form.errors)
            
    else:
        user_form = UserForm()
    return render(request,'app/register.html',
                          {'user_form':user_form,
                           'registered':registered, 'message': message})
def user_login(request):
    message=None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('fetch'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            message='username or password does not exists'
            return render(request, 'app/login.html', {'message':message})
    else:
        return render(request, 'app/login.html', {'message':message})

@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def fetch(request):
    print("inside fetch")
    message=None
    if request.method == 'POST':
        print("inside fetch request post")
        url_form=URLForm(data=request.POST)
        if url_form.is_valid():
            url=request.POST.get("url")
            content=Content.objects.filter(Q(url=url)&Q(username=request.user)).values()
            if(len(content)==0):
                print("inside fetch validity")
                url_obj=url_form.save(commit=True)
                data = get_content(url)
                if(data):
                    url_obj.username.add(request.user)
                    url_obj.response=data
                    url_obj.save()
                    return render(request, "app/content.html",{'data':data})
                else:
                    message='something went wrong, either check your internet connectivity or enter a valid url'
                
            else:
                data=content[0]['response']
                return render(request, "app/content.html",{'data':data})
        else:
            print(url_form.errors)
    else:
        url_form = URLForm()
    return render(request,'app/fetch.html',
                          {'url_form':url_form, 'message':message})
def content(request):
    return render(request,'app/fetch.html')
