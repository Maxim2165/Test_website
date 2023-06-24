from django.shortcuts import render
from django.http import JsonResponse
from .models import recipes, users
from django.views.generic import View
import base64
import string
import re
import hashlib


def password_hash(password_sha):
    bytes_password = bytes(password_sha.encode("utf-8"))
    password_sha = hashlib.sha256(bytes_password).hexdigest()
    return password_sha


def index(request):
    return render(request, "main/index.html")


def zavtrak(request):
    recipes_savtrak = recipes.objects.filter(name_category="завтрак")
    for i in recipes_savtrak:
        photo = base64.b64encode(i.image).decode("utf-8")
        i.image = photo
    return render(request, "main/zavtrak.html", context={"data": recipes_savtrak})


def zavtrak_detail(request, zavtrak_id):
    zavtrak_id = recipes.objects.filter(id=zavtrak_id)

    cooking = zavtrak_id[0].cooking_process
    cooking_re = re.sub(r'(\d+.)', r'\n\1', cooking)

    photo = base64.b64encode(zavtrak_id[0].image).decode("utf-8")
    return render(request, "main/zavtrak_detail.html", context={"zavtrak_id": zavtrak_id,
                                                                "photo": photo,
                                                                "cooking_re": cooking_re})


def obed(request):
    recipes_obed = recipes.objects.filter(name_category="обед")
    for i in recipes_obed:
        photo = base64.b64encode(i.image).decode("utf-8")
        i.image = photo

    return render(request, "main/obed.html", context={"data": recipes_obed})


def obed_detail(request, obed_id):
    obed_id = recipes.objects.filter(id=obed_id)
    photo = base64.b64encode(obed_id[0].image).decode("utf-8")
    return render(request, "main/obed_detail.html", context={"obed_id": obed_id,
                                                             "photo": photo})


def uzhin(request):
    recipes_uzhin = recipes.objects.filter(name_category="ужин")
    for i in recipes_uzhin:
        photo = base64.b64encode(i.image).decode("utf-8")
        i.image = photo
    return render(request, "main/uzhin.html", context={"data": recipes_uzhin})


def uzhin_detail(request, uzhin_id):
    uzhin_id = recipes.objects.filter(id=uzhin_id)
    photo = base64.b64encode(uzhin_id[0].image).decode("utf-8")
    return render(request, "main/uzhin_detail.html", context={"uzhin_id": uzhin_id,
                                                              "photo": photo})


def login(request):
    return render(request, "main/login.html")


def registration_complete(request):
    return render(request, "main/registration_complete.html")


def login_complete(request):
    return render(request, "main/login_complete.html")


def login_reg(request):
    return render(request, "main/login_reg.html")


def login_login(request):
    return render(request, "main/login_login.html")


def login_reg_(request):
    if request.method == "POST":
        login_user = request.POST.get("login").translate({ord(c): None for c in string.whitespace})
        password_user = request.POST.get("password").translate({ord(c): None for c in string.whitespace})
        password_user = password_hash(password_user)
        users(user=str(login_user), password=str(password_user)).save()
        return registration_complete(request)


def login_login_(request):
    if request.method == "POST":
        login_user = request.POST.get("login").translate({ord(c): None for c in string.whitespace})
        password_user = request.POST.get("password").translate({ord(c): None for c in string.whitespace})
        sign_in = users.objects.filter(user=login_user)
        if (sign_in[0].user.translate({ord(c): None for c in string.whitespace})) == login_user and sign_in[0].password == password_hash(password_user):
            return login_complete(request)


