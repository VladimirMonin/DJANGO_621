from django.shortcuts import render
from django.http import HttpResponse

from dataclasses import dataclass
OWNER = "Mr. Robot"

@dataclass
class Post:
    title: str
    text: str
    hash_tags: list[str]
    views: int
    authors: dict[str, str]

    def test(self):
        return f"Да-да, в шаблоне мы можем вызывать метод экземпляра класса: {self.title} - {self.views} просмотров"


post = Post(
    title="Django 6.1",
    text="Django 6.1 - это круто!",
    hash_tags=["#django", "#python", "#web"],
    views=100500,
    authors={
        "main": "Mr. Robot",
        "secondary": "Тётя Варя",
    },
)


POST_CONTEXT = {
    "title": "Django 6.1",
    "text": "Django 6.1 - это круто!",
    "hash_tags": ["#django", "#python", "#web"],
    "views": 100500,
    "authors": {
        "main": "Mr. Robot",
        "secondary": "Тётя Варя",
    },
    "post": post,
}




def index(request):
    return HttpResponse("<h1>Привет из Django 6.1!</h1>")


def experiment(request):
    context = {"owner": "Маня Понич"}
    return render(request, "blog/experiment.html", POST_CONTEXT)

