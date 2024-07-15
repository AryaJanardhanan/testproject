from django.shortcuts import render,redirect, HttpResponse
from .forms import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, "home.html")

def indexx(request):
    return render(request, "indexx.html")

def about(request):
    return render(request, "about.html")

def base(request):
    return render(request, "base.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'success.html', {'name':name})
    else:  
        form = ContactForm()


    return render(request,'contact.html', {'form':form})



def subform(request):
    return render(request, "test.html")


def modelfrm(request):
    if request.method == 'POST':
        form =  ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProfileForm()
    return render(request, 'form.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #save user object
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()

            #save profile object
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            profile = Profile.objects.create(user=user,first_name=first_name,last_name=last_name,username=username,email=email)
            return render(request, "success.html")

    else:
        form = RegistrationForm()
    return render(request, "register.html", {'form':form})
        
        
@login_required
def success(request):
    return render(request, "success.html")

def uslogin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return render(request, "success.html")
    else:
        form = LoginForm()
    return render(request, "login.html", {'form':form})

def uslogout(request):
    logout(request)
    return redirect ('home')

def additem(request):
    if request.method == 'POST':
        form = Itemsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = Itemsform()
    return render(request, "items.html", {'form':form})

def display(request):
    items = Item.objects.all()
    return render(request, "display.html", {'items':items})

def delt(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('display')
    return render (request, "confirm.html", {'item':item})


def editt(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = Itemsform(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = Itemsform(instance=item)
    return render(request, "edit.html", {'form':form})






