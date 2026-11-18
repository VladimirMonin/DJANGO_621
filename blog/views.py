from django.http import Http404
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from .data import CATEGORIES, POSTS
from django.core.paginator import Paginator


def index(request):
    return HttpResponse("<h1>Привет из Django 6.1!</h1>")


def post_list(request):
    q = request.GET.get("q", "")
    cat = request.GET.get("cat", "").strip()
    posts = [post for post in POSTS if post["is_published"]]

    if cat:
        posts = [post for post in posts if post["category"]["name"] == cat]

    if q:
        posts = [post for post in posts if q.lower() in post["title"].lower()]

    # Получаем номер страницы из GET-параметров
    page_number = request.GET.get("page", 1)

    # Пагинация постов по 5 шт. на страницу
    paginator = Paginator(posts, 5)

    # Получаем объект страницы с постами
    page_obj = paginator.get_page(page_number)

    context = {
        "posts": page_obj.object_list,
        "page_obj": page_obj,
        "categories": CATEGORIES,
        "page_title": "Межпространственный блог",
        "q": q,
        "cat": cat,
    }
    if request.htmx:
        import time

        time.sleep(2)  # имитация долгой работы сервера
        return render(request, "blog/post_list.html#results", context)
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


# --- Эксперимент для занятия о фильтрах и тегах шаблонов --------------------
# Словарь LAB намеренно не связан с базой и с data.py: страница /lab/filters/
# показывает только шаблонный язык. Значения подобраны так, чтобы каждый фильтр
# светился по-разному: пустая строка против None, один против пяти, три строки
# против одной.

from datetime import datetime

LAB = {
    "title": "Дом 12, масло & мёд и ещё пара лишних слов",
    "subtitle": "",  # пустая строка: default сработает, default_if_none — нет
    "annotation": None,  # именно None: сработают оба фильтра
    "views_one": 1,  # «1 просмотр» — единственная форма
    "views_many": 5,  # «5 просмотров» — форма многих
    "views_21": 21,  # «21 просмотр» — ловушка: 21 ведёт себя как 1
    "tags": ["django", "шаблоны", "python"],
    "body": "Первая строка.\nВторая.\n\nПосле пустой.",
    "is_published": True,
    "is_draft": False,
    "published_at": datetime(2026, 11, 18, 19, 0),
    "search": "дом 12 & масло",
    "counter": 7,
    "rating_empty": "",
    "posts_mini": [
        {"name": "Альфа", "rating": 3},
        {"name": "Бета", "rating": 5},
        {"name": "Гамма", "rating": 1},
        {"name": "Дельта", "rating": None},
        {"name": "Эпсилон", "rating": "Чебурек"},
    ],
}


def lab_filters(request):
    return render(request, "blog/lab_filters.html", {"lab": LAB})
