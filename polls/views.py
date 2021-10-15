from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Userdet
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import addimg
from django.shortcuts import get_object_or_404
from PIL import Image
from .models import Category
from .models import Cards

from django import forms
from .models import Userdet

import ocrspace
import requests


class IMGdet(forms.ModelForm):
    class Meta:
        model = Userdet
        fields = ('userIMG',)


class CARDdet(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ('IMG', 'Name')


def loginpage(request):
    return render(request, "loginpage.html")

@login_required
def base(request, id):
    car = Cards.objects.filter(userid=id, ).all()
    cat = Category.objects.filter(userid=id).all()
    det = Userdet.objects.filter(userid=id)
    if bool(det)  is True:
        return render(request, "base.html", {
            'cars' : car,
            'det': det[0],
            'cats' : cat,
        })
    else:
        return render(request, "base.html",{
            'cats' : cat,
            'cars': car,
        })

def setting(request, id):
    car = Cards.objects.filter(userid=id, ).all()
    cat = Category.objects.filter(userid=id).all()
    det = Userdet.objects.filter(userid=id)
    if bool(det)  is True:
        return render(request, "setting.html", {
            'cars' : car,
            'det': det[0],
            'cats' : cat,
        })
    else:
        return render(request, "setting.html",{
            'cats' : cat,
            'cars': car,
        })

def showmycard(request, id):
    car = Cards.objects.filter(userid=id, ).all()
    cat = Category.objects.filter(userid=id).all()
    det = Userdet.objects.filter(userid=id)
    if bool(det)  is True:
        return render(request, "category.html", {
            'cars' : car,
            'det': det[0],
            'cats' : cat,
        })
    else:
        return render(request, "category.html",{
            'cats' : cat,
            'cars': car,
        })

def loginUser(request):
    Username = request.POST.get('username')
    Password = request.POST.get('password')
    user = authenticate(request, username=Username, password=Password)
    if user is not None:
        login(request, user)
        user = User.objects.filter(username=Username)
        return redirect('mycard:base', id= user[0].id)
    else:
        return HttpResponse("Fails")

def logout_view(request):
    logout(request)
    return redirect('mycard:loginpage')


def register(request):
    Username = request.POST.get('username')
    Email = request.POST.get('email')
    Password = request.POST.get('password')
    try:
        return redirect('mycard:loginpage')
    except:
        user = User.objects.create_user(Username, Email, Password)
        if user:
            login(request, user)
            user = User.objects.filter(username=Username)
            Category.objects.create(userid=user[0].id, Name='main-category')
            return redirect('mycard:base', id=user[0].id)
        else:
            return HttpResponse('Error')

@login_required
def changepass(request):
    form_edit_password = PasswordChangeForm(request.user, request.POST)
    if form_edit_password.is_valid():
        form_edit_password.save()
        return redirect('mycard:loginpage')
    else:
        return HttpResponse('fails')

@login_required
def changepro(request):
    return render(request, 'changepro.html')


@login_required
def changeprofile(request):
    userid = request.POST.get('id')
    Username = request.POST.get('username')
    Email = request.POST.get('email')
    updateuser = User.objects.filter(id = userid).update(username= Username, email = Email)
    if updateuser:
        user = User.objects.filter(username=Username)
        return redirect('mycard:base', id=user[0].id)
    else:
        return HttpResponse('fails')

@login_required
def changepa(request):
    return render(request, 'change_pass_form.html')


@login_required
def adddetails(request):
    return render(request, 'addimg.html')


@login_required
def addphone(request):
    userid = request.POST.get('id')
    userphone = request.POST.get('phone')
    a = Userdet.objects.filter(userid=userid)
    b = bool(a)
    if b is True:
        updateuser = Userdet.objects.filter(userid=userid).update(userphone= userphone)
    else:
        updateuser = Userdet.objects.create(userid=userid, userphone= userphone)
    if updateuser:
        user = User.objects.filter(id = userid)
        return redirect('mycard:base', id=user[0].id)
    else:
        return HttpResponse('fails')



def image_upload_view(request):
    userid = request.POST.get('id')
    a = Userdet.objects.filter(userid=userid)
    if bool(a) is not True:
        Userdet.objects.create(userid=userid)
    image = Userdet.objects.get(userid=userid)
    form = IMGdet(request.POST, request.FILES, instance=image)
    if form.is_valid():
        a = form.instance
        a.save()
        user = User.objects.filter(id=userid)
        return redirect('mycard:base', id=user[0].id)

    else:
        return HttpResponse('fails')

def IMG(request):
    form = IMGdet(request.POST, request.FILES)
    return render(request, 'IMG.html', {'form':form})


def add_cat(request):
    return render(request, 'add_cat.html')


def addcategory(request):
    userid = request.POST.get('id')
    name = request.POST.get('name')
    if bool(name) is True:
        updateuser = Category.objects.create(userid= userid, Name= name)
        if updateuser:
            user = User.objects.filter(id=userid)
            return redirect('mycard:base', id=user[0].id)
        else:
            return HttpResponse('fails')
    else:
        return HttpResponse('fails')

def addcard(request):

    form = CARDdet(request.POST, request.FILES)
    return render(request, 'addcard.html', {'form':form})


def add_card(request):
    userid = request.POST.get('id')
    catname = request.POST.get('categoryname')
    if bool(catname) is not True:
        catid = Category.objects.get(Name= 'main-category', userid = userid)
    # elif bool(Category.objects.get(Name= catname)) is not True:
        # catid = Category.objects.create(Name= catname, userid = userid)
    else:
        catid = Category.objects.get(Name= catname, userid = userid)
    # Cards.objects.filter(userid = userid).create(catid = catid.id)
    image = Cards.objects.create(userid=userid, catid=catid.id)
    form = CARDdet(request.POST, request.FILES, instance=image)
    if form.is_valid():
        a = form.instance
        a.save()
        user = User.objects.filter(id=userid)
        return redirect('mycard:base', id=user[0].id)
    else:
        return HttpResponse('fails')


def showlist(request, id):
    cat = Category.objects.filter(id=id).all()
    userid = cat[0].userid
    car = Cards.objects.filter(catid=id, userid=userid).all()
    det = Userdet.objects.filter(userid=userid)
    if bool(det)  is True:
        return render(request, "card-list.html", {
            'cars': car,
            'det': det[0],
            'cats': cat,
        })
    else:
        return render(request, "card-list.html", {
            'cats': cat,
            'cars': car,
        })


def showcard(request, id):
    car = Cards.objects.get(id=id)
    userid = car.userid
    det = Userdet.objects.filter(userid=userid)
    api = ocrspace.API()
    if bool(car.Details) is not True:
        ocr = api.ocr_file(car.IMG)
        Cards.objects.filter(id=id).update(Details=ocr)
    car = Cards.objects.get(id=id)
    if bool(det) and bool(car) is True:
        return render(request, "card.html", {
            'cars': car,
            'det': det[0],

        })
    else:
        return render(request, "card.html", {

            'cars': car,
        })


def editcard(request, id):
    car = Cards.objects.filter(id=id).all()
    userid = car[0].userid
    catid = car[0].catid
    cat = Category.objects.filter(id = catid).all()
    det = Userdet.objects.filter(userid=userid)
    if bool(det)  is True:
        return render(request, "editcard.html", {
            'cars': car[0],
            'det': det[0],
            'cats': cat[0],
        })
    else:
        return render(request, "editcard.html", {
            'cats': cat[0],
            'cars': car[0],
        })


def edit(request, id):
    userid = request.POST.get('id')
    cat = request.POST.get('category')
    name = request.POST.get('name')
    det = request.POST.get('details')
    if bool(cat) is not True:
        catid = Category.objects.get(Name='main-category', userid=userid)
    else:
        catid = Category.objects.get(Name=cat, userid=userid)
    Cards.objects.filter(id=id).update(Name= name, Details= det, catid = catid)
    user = User.objects.filter(id=userid)
    return redirect('mycard:base', id=user[0].id)



def removecard(request, id):
    card = Cards.objects.filter(id = id).all()
    userid = card[0].userid
    Cards.objects.filter(id =id).delete()
    user = User.objects.filter(id=userid)
    return redirect('mycard:base', id=user[0].id)



def removecat(request, id):
    cat = Category.objects.filter(id=id).all()
    userid = cat[0].userid
    category = Category.objects.filter(Name= 'main-category', userid=userid)
    catid = category[0].id
    card = Cards.objects.filter(catid = id,userid= userid).update(catid = catid)
    Category.objects.filter(id=id).delete()
    user = User.objects.filter(id=userid)
    return redirect('mycard:base', id=user[0].id)
