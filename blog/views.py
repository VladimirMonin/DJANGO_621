from django.shortcuts import render
from django.http import HttpResponse
from .data import CATEGORIES, POSTS



def index(request):
    return HttpResponse("<h1>Привет из Django 6.1!</h1>")


def post_list(request):
    posts = [post for post in POSTS if post['is_published']]
    context = {"posts": posts, "categories": CATEGORIES, "page_title": "Межпространственный блог"}
    return render(request, "blog/post_list.html", context)
