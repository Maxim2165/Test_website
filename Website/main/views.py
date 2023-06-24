from django.shortcuts import render
from .models import recipes
from django.views.generic import View
import base64
import re

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
    cooking_re =re.sub(r'(?<=\S)\s{2}(?=\S)', '\n', cooking)

    ingredients = zavtrak_id[0].ingredients
    ingredients_re = re.sub(r'(?<=\S)\s{2}(?=\S)', '\n', ingredients)
    print(ingredients_re)


    photo = base64.b64encode(zavtrak_id[0].image).decode("utf-8")
    return render(request, "main/zavtrak_detail.html", context={"zavtrak_id": zavtrak_id,
                                                                "photo": photo,
                                                                "cooking_re": cooking_re,
                                                                "ingredients_re": ingredients_re})


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