from django.http import Http404
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from .data import CATEGORIES, POSTS


def index(request):
    return HttpResponse("<h1>Привет из Django 6.1!</h1>")


def post_list(request):
    posts = [post for post in POSTS if post["is_published"]]
    context = {
        "posts": posts,
        "categories": CATEGORIES,
        "page_title": "Межпространственный блог",
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, post_id=None, post_slug=None):
    for post in POSTS:
        matches_id = post_id is not None and post["id"] == post_id
        matches_slug = post_slug is not None and post["slug"] == post_slug
        if post["is_published"] and (matches_id or matches_slug):
            context = {
                "post": post,
                "categories": CATEGORIES,
                "page_title": post["title"],
            }
            return render(request, "blog/post_detail.html", context)
    error_message = (
        f"Пост с id={post_id} не найден"
        if post_id
        else f"Пост с slug={post_slug} не найден"
    )
    raise Http404(404, error_message)


def clock_view(request):
    return render(request, "blog/clock.html", {"now": timezone.localtime()})


def clock_fragment(request):
    import time

    # time.sleep(2)
    return render(request, "blog/clock.html#clock", {"now": timezone.localtime()})


def post_card_fragment(request, post_slug):
    import time
    time.sleep(2)  # имитация долгой работы сервера
    for post in POSTS:
        if post["slug"] == post_slug and post["is_published"]:
            context = {"post": post}
            return render(request, "blog/post_card_include.html", context)
    raise Http404(404, f"Пост с slug={post_slug} не найден")


def search_experiment(request):
    query_method = request.method
    query_dict = request.GET
    query_path = request.path

    # Параметр q - поисковый запрос
    query = query_dict.get("q", "")
    kompot = query_dict.get("kompot", "нет компота")
    
    context = {
        "query_method": query_method,
        "query_dict": query_dict,
        "query_path": query_path,
        "q_value": query,
        "kompot_value": kompot,

    }

    
    return render(request, "blog/search_experiment.html", context)