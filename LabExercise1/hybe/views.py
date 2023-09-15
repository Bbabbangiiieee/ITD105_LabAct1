from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from hybe.functions import handle_uploaded_file
from hybe.forms import ArtistForm
from hybe.models import Artist

# Create your views here.
def index(request): 
    return render(request, 'welcome.html')

def newuser(request):
    if request.method == 'POST':
        print("post");
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("valid");
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            print(form.errors)
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/display') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')

@login_required
def addnew(request):
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)
        print("Before form validation")
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['img'])
                model_instance = form.save(commit=False)
                model_instance.save()
                return redirect('/show')
            except:
                pass
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ArtistForm()
    return render(request,"add.html",{'form':form})

@login_required
def show(request):
    artists = Artist.objects.all()
    return render(request,"read.html", {'artists':artists})

@login_required
def display(request):
    images = Artist.objects.all()
    return render(request,"gallery.html", {'images':images})

@login_required
def edit(request, id):  
    artist = Artist.objects.get(id=id)  
    return render(request,'edit.html', {'artist':artist})

@login_required
def update(request, id):  
    artist = Artist.objects.get(id=id)  
    form = ArtistForm(request.POST, instance = artist)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'artist': artist})

def destroy(request, id):  
    artist = Artist.objects.get(id=id)  
    artist.delete()  
    return redirect("/show")  