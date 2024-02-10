from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Photo
from django.http.response import JsonResponse
from .encoders import UUIDEncoder
import json

# Create your views here.


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect('/dash/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/login/?error=True')
    if request.GET.get('error', None):
        messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        if username and password and password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, "Signup successful")
            return redirect('/')
        else:
            messages.error(request, "Please enter username and a password")
            return redirect('/signup/?error=True')
    if request.GET.get('error', None):
        messages.error(request, "Please enter username and a password")
    return render(request, 'signup.html')


@login_required(login_url='/login')
def index_view(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            image = request.FILES['img_file']
            ## upload the image here
            photo = Photo.objects.create(
                user=request.user,
                name=name,
                image=image
            )
            messages.success(request, "Photo has been uploaded")
            return redirect(f"/edit/{photo.id}/")
        except Exception as err:
            print(err)
            messages.error(request, "Please upload an image and a name")
            return redirect('/?error=True')

    return render(request, 'index.html')


@login_required(login_url='/login')
def dash_view(request):
    context = Photo.objects.filter(user=request.user)
    return render(request, 'dash.html', {'context' : context})

@login_required(login_url='/login')
def edit_and_save_photo(request, id):
    if Photo.objects.filter(id=id, user=request.user).exists():
        photo = Photo.objects.get(id=id, user=request.user)
        if request.method == 'GET':
            return render(request, 'edit.html', {'context' : photo})
        elif request.method == 'POST':
            try:
                image = request.FILES['img_file']
                photo.image = image
                name = request.POST.get('name', None)
                if name:
                    photo.name = name
                photo.save()

                return JsonResponse(json.dumps({
                    "id" : photo.id,
                    "image" : photo.image.url,
                    "name" : photo.name,
                    "updated_on" : photo.updated_on,
                    "msg" : "success"
                }, cls=UUIDEncoder), safe=False)
            except Exception as err:
                return JsonResponse(json.dumps({
                    "error" : str(err),
                    "msg" : "error"
                }), safe=False)
        else:
            messages.error(request, "only GET & POST requests are allowed")
            return redirect('/dash/')
    else:
        messages.error(request, "Project was not found")
        return redirect('/dash/')


@login_required(login_url='/login')
def delete_photo(request, id):
    if Photo.objects.filter(id=id, user=request.user).exists():
        photo = Photo.objects.get(id=id, user=request.user).delete()
        return JsonResponse(json.dumps({
            "msg" : "success"
        }), safe=False)
    return JsonResponse(json.dumps({
            "msg" : "error"
    }), safe=False)



@login_required(login_url="/login")
def profile_view(request):
    context = request.user
    return render(request, 'profile.html', {'context' : context})
