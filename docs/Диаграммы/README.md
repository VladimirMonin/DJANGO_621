# Диаграммы Excalidraw

Редактируемые учебные схемы проекта. Файлы `.excalidraw` открываются в Excalidraw или совместимом расширении редактора кода.

## lesson_47

Все три диаграммы относятся к уроку `lesson_47`. Рекомендуемый порядок просмотра:

| № | Диаграмма | О чём |
| --- | --- | --- |
| 01 | [Путь запроса и MTV](lesson_47_01_request_mtv.excalidraw) | Как запрос главной страницы проходит от браузера через `urls.py` и view к шаблону. Обращение к модели показано как необязательный шаг. |
| 02 | [Данные из view в шаблон](lesson_47_02_template_context.excalidraw) | Передача `POST_CONTEXT` через `render()`, подстановка переменных в HTML, работа со списками, словарями, фильтром `join` и объектом `post`. |
| 03 | [Условия в шаблоне: if, elif, else](lesson_47_03_template_if.excalidraw) | Проверка публикации поста и вложенный выбор CSS-класса по рейтингу. Почему срабатывает только одна ветка и что означает `else`. |

## lesson_48

| № | Диаграмма | О чём |
| --- | --- | --- |
| 01 | [Цикл for: из списка — строки страницы](lesson_48_01_template_for.excalidraw) | Передача списка `posts` в шаблон, текущая запись `post`, счётчик `forloop.counter`, условия `forloop.first` / `forloop.last` и ветка `{% empty %}`. На данных текущего блога. |
| 02 | [Как CSS попадает на страницу](lesson_48_02_static.excalidraw) | `{% load static %}`, путь к CSS в HTML, отдельный запрос браузера, раздача статики при разработке и статус `200 OK` в Network. |
| 03 | [Тег url: ссылка по имени маршрута](lesson_48_03_url_tag.excalidraw) | `name="post_list"` → `{% url 'post_list' %}` → ссылка на `/posts/`. Имя маршрута и его адрес — разные вещи. |

## lesson_49

### URL и конвертеры

| № | Диаграмма | О чём |
| --- | --- | --- |
| 01 | [Адрес → аргумент view](lesson_49_01_dynamic_url.excalidraw) | Как `path("posts/<int:post_id>/", ...)` разбирает адрес `/posts/42/`: строка `42` превращается в `post_id=42` и попадает во view. Внизу — что даёт `404`, если формат не совпал. |
| 02 | [Конвертеры: какой адрес подойдёт](lesson_49_02_converters.excalidraw) | `int`, `str`, `slug`, `uuid`, `path`: примеры, что каждый принимает и что не пропускает. Без базы данных — только разбор адреса. |

### Наследование шаблонов

Порядок просмотра: 03 → 04 → 05 → 06 → 07 → 08.

| № | Диаграмма | О чём |
| --- | --- | --- |
| 03 | [base.html: скелет и блоки](lesson_49_03_base_blocks.excalidraw) | Что лежит в `base.html`: `head`, `nav`, `main`, `footer`, `scripts`. Блоки — именованные точки замены с содержимым по умолчанию. |
| 04 | [extends: ребёнок заменяет блоки](lesson_49_04_extends_override.excalidraw) | Один `base.html` и два ребёнка: что наследуется, что заменяется и почему `{% extends %}` стоит первой строкой. |
| 05 | [block.super: добавить, а не заменить](lesson_49_05_block_super.excalidraw) | Цепочка `base.html → section.html → page.html`: родительский слой плюс добавка. Отдельно — почему `{% super %}` не существует и как писать `{{ block.super }}`. |
| 06 | [include: один файл — разные страницы](lesson_49_06_include_partial.excalidraw) | Один `blog/post_card_include.html` в цикле на странице блога и в личном кабинете. Разные списки (`posts`, `my_posts`), разные страницы — один partial. |
| 07 | [partials: несколько шаблонов в одном файле](lesson_49_07_partials_view.excalidraw) | `{% partialdef %}` и `{% partial %}`: два именованных фрагмента в одном файле. View через `render(request, "blog/post_cards.html#name", ...)` отдаёт только один фрагмент. |
| 08 | [include with: тот же пост, другое имя](lesson_49_08_include_with.excalidraw) | Сверху — текущий код: цикл в `post_list.html`, include без `with`, partial читает `post`. Внизу — пример переименования: цикл остаётся в родителе, `{% include ... with post_data=post %}`, partial читает `post_data`; `forloop.counter` даёт 1, 2, 3. |

### Что когда использовать

| Задача | Инструмент | Где смотреть |
| --- | --- | --- |
| Общий каркас страниц | `{% extends %}` + `{% block %}` | 03–04 |
| Добавить к родительскому блоку | `{{ block.super }}` | 05 |
| Вставить готовый кусок | `{% include %}` | 06–08 |
| Передать в partial другое значение | `{% include ... with post_data=post %}` | 08 |
| Несколько вариантов в одном файле | `{% partialdef %}` + `{% partial %}` | 07 |
| Отдать только фрагмент | `render(request, "file.html#name", ...)` | 07 |

`partialdef` и `#name` — нативные возможности Django 6.1, отдельный пакет не нужен. `#name` — имя partial, а не CSS-id и не Vue-компонент.

## lesson_50

### AJAX, частичные шаблоны и HTMX

Порядок: 01 → 02 → 03 → 04 → 05.

| № | Диаграмма | О чём |
| --- | --- | --- |
| 01 | [Одна карточка, один запрос, один фрагмент](lesson_50_01_ajax.excalidraw) | Учебная гипотеза: клик → `fetch()` → view → `#card` → подмена `outerHTML`. HTMX нет. |
| 02 | [Один файл — два адреса — два ответа](lesson_50_02_partial_two_renders.excalidraw) | Реальный код: `/clock/` и `/clock/fragment/` → `clock_view` и `clock_fragment` → один `blog/clock.html`. Полная страница против `<span>`. Кнопка не нужна: фрагмент открывается вкладкой. |
| 03 | [inline: объявил и сразу показал](lesson_50_03_partialdef_inline.excalidraw) | Слои `<html>` → `<div id="clock">` → `<span>`, что делает `partialdef inline`, почему фрагмент маленький. Ловушка: `#clock` в `render()` — имя partial, `hx-target="#clock"` — CSS-селектор. |
| 04 | [Кнопка сама делает запрос и подмену](lesson_50_04_htmx_swap.excalidraw) | `{% htmx_script %}` в `base.html`, три атрибута `hx-*`, цепочка из пяти шагов, почему ответ `<span>` ложится в `innerHTML` и зачем `time.sleep(2)`. |
| 05 | [Кто делает шаги: fetch против HTMX](lesson_50_05_fetch_vs_htmx.excalidraw) | Таблица сравнения 01 и реальных часов: меняются только шаги 1 и 6; view, partial и фрагмент одинаковы. |

01 — гипотеза: `update_card_by_id`, `cards_page.html` и `fetch` в проекте нет. 02–05 построены на настоящем коде: `config/urls.py`, `blog/views.py`, `blog/templates/blog/clock.html`, `blog/templates/blog/base.html`.

Точный ответ `/clock/fragment/` проверен изолированным рендером Django: `<span>12:35:01</span>` с отступами, без `<div>` и `<html>`.

## lesson_51

### Триггеры, индикатор, карточка и поиск

Порядок: 01 → 02 → 03 → 04 → 05 → 06.

| № | Диаграмма | О чём |
| --- | --- | --- |
| 01 | [Откуда берётся click](lesson_51_01_triggers.excalidraw) | Событие по умолчанию по типу элемента: `form → submit`, `input/textarea/select → change`, остальное → `click`. Явный `hx-trigger` заменяет дефолт; замена события, модификаторы, интервал против времени ответа. |
| 02 | [Карточка по кнопке: что заменяется](lesson_51_02_card_button.excalidraw) | Геометрия `article`, `closest .post-card`, `outerHTML`, четыре атрибута одной кнопки, два нажатия подряд, два смысла 404, почему `forloop.counter` даёт голую точку. |
| 03 | [Адрес с вопросом: request.GET и отбор](lesson_51_03_request_get.excalidraw) | Адрес разложен на цветные куски, `QueryDict`, воронка 20 → 18 → 5 → 1, таблица из пяти адресов. Маршрут `posts/` не меняется. |
| 04 | [Форма собирает адрес сама](lesson_51_04_get_form.excalidraw) | Кольцо `name → URL → request.GET → контекст → value`, три пустых состояния, `{% if q or cat %}`, `with ... only`. |
| 05 | [Кто показывает, что запрос идёт](lesson_51_05_indicator.excalidraw) | `hx-indicator` и его селекторы (`this`, `closest`, `find`, `next`, `previous`, `inherit`, список через запятую), два имени класса `htmx-request` / `htmx-indicator`, настройка `htmx-config`, CSS из проекта, жизненный цикл класса, `hx-disabled-elt` и `hx-request`. |
| 06 | [Один запрос, семь решений](lesson_51_06_request_attributes.excalidraw) | Карта атрибутов одного запроса: `hx-trigger`, `hx-get`, `hx-target`, `hx-swap`, `hx-indicator`, `hx-disabled-elt`, `hx-request`; что происходит, если атрибут не написан. |

Сведения о событиях по умолчанию, именах классов и значениях по умолчанию сверены с локальным `htmx-2.js` из `django_htmx`. Код, которого нет в проекте, помечен `пример:`. Числа воронки и таблицы — из `blog/data.py`: 20 постов, 18 опубликованных, 4 категории. Ответ карточки — 885 символов, начинается с `<article …>`, без `<html>`.

## Как называем файлы

Формат: `lesson_<номер урока>_<порядок схемы>_<тема>.excalidraw`.

Например: `lesson_47_03_template_if.excalidraw`.

- `lesson_47` — урок; префикс пишется строчными буквами.
- `03` — порядок схемы внутри урока, всегда две цифры.
- `template_if` — краткая тема строчными латинскими буквами; слова разделяются `_`.

Для следующего урока меняется номер в префиксе, а порядок схем начинается с `01`. Новую диаграмму добавляем в раздел соответствующего урока в этом README.
