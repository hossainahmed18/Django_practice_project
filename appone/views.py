from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import UserProfile,article

# Create your views here.
from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .form import registrationForm

# Create your views here.


def home(request):
    return render(request,"appone/index.html")


def getlogin(request):
    if request.user.is_authenticated:
        return redirect('after')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            passs = request.POST.get('pass')
            auth = authenticate(request,username=user,password=passs)

            if auth is not None:
                login(request, auth)
                return redirect('after')
            else:
                return redirect('login')
    return render(request,"appone/login.html")


def getlogout(request):
    logout(request)
    return redirect('home')


def getafter(request):
    return render(request, "appone/after.html")


def getregister(request):
    form = registrationForm(request.POST or None)
    if form.is_valid():
        instancex = form.save(commit=False)
        instancex.save()
        return redirect('home')

    return render(request, "appone/register.html", {"form": form})


def getprofile(request):
    if request.user.is_authenticated:
        u = get_object_or_404(User, id=request.user.id)
        showuser = get_object_or_404(UserProfile, user_identify=u.id)
        context={
            "myuser": showuser
        }
        return render(request,"appone/profile.html", context)

    else:
        return redirect('home')


def getshow(request):
    all_post = article.objects.all()
    context = {
        "post": all_post
    }
    return render(request, "appone/show.html", context)
