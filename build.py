#!/usr/bin/env python3
"""Генератор страниц сайта. Шапка и подвал общие — правятся здесь, затем: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent

COMPANY = "FDV"
TAGLINE = "Продажа контейнеров"
PHONE = "+7 (000) 000-00-00"   # TODO
PHONE_FREE = "8 (800) 000-00-00"
EMAIL = "info@example.ru"      # TODO
HOURS = "Пн–Пт, 9:00–18:00"
ADDRESS = "г. Москва"

# (slug, название, [(slug, название), ...])
MENU = [
    ("company", "О компании", [
        ("company", "О нас"), ("company/reviews", "Отзывы"), ("company/clients", "Наши клиенты"),
        ("company/docs", "Документы"), ("company/faq", "Вопрос-ответ")]),
    ("price", "Цены", []),
    ("catalog", "Контейнеры", [
        ("catalog", "Виды и типы контейнеров"), ("modifications", "Модификации контейнеров"),
        ("purposes", "Контейнеры по назначению"), ("price", "Прайс-лист"), ("views", "Просмотр контейнеров")]),
    ("services", "Услуги", [
        ("services/delivery", "Доставка контейнеров"), ("services/installation", "Установка контейнеров"),
        ("services/rent", "Аренда контейнеров"), ("services/transportation", "Перевозки контейнеров"),
        ("services/unloading", "Разгрузка контейнеров"), ("services/repair", "Ремонт контейнеров"),
        ("services/storage", "Хранение контейнеров"), ("services/painting", "Покраска контейнеров"),
        ("services/online-view", "Онлайн-просмотр контейнеров"), ("services/insulation", "Утепление контейнеров"),
        ("services/construction", "Строительство из контейнеров"), ("services/repacking", "Перетарка контейнеров"),
        ("services/buyout", "Выкуп контейнеров"), ("services/conversion", "Переоборудование контейнеров")]),
    ("info", "Информация", [
        ("info", "Информация"), ("info/payment", "Оплата"), ("info/regions", "Регионы поставок"),
        ("articles", "Статьи"), ("info/dictionary", "Словарь терминов"),
        ("info/characteristics", "Характеристики контейнеров"), ("info/dimensions", "Габариты контейнеров")]),
    ("contacts", "Контакты", []),
]


def href(prefix, slug):
    return f"{prefix}{slug}/index.html" if slug else f"{prefix}index.html"


def header(prefix, active):
    items = []
    for slug, title, subs in MENU:
        cls = "nav__item" + (" has-drop" if subs else "") + (" is-active" if slug == active else "")
        caret = '<i class="nav__caret"></i>' if subs else ""
        drop = ""
        if subs:
            drop = '<ul class="nav__drop">' + "".join(
                f'<li><a href="{href(prefix, s)}">{t}</a></li>' for s, t in subs) + "</ul>"
        items.append(f'<li class="{cls}"><a class="nav__link" href="{href(prefix, slug)}">{title}{caret}</a>{drop}</li>')
    return f"""
<div class="topbar"><div class="container">
  <div class="topbar__group"><span>{ADDRESS}</span><span class="topbar__group--hide">{HOURS}</span></div>
  <div class="topbar__group"><a href="mailto:{EMAIL}">{EMAIL}</a><a class="topbar__group--hide" href="tel:{PHONE_FREE.replace(' ', '')}">{PHONE_FREE} — бесплатно по России</a></div>
</div></div>
<header class="header"><div class="container header__row">
  <a class="logo" href="{href(prefix, '')}">
    <img src="{prefix}img/logo.png" alt="{COMPANY}" onerror="this.remove()">
    <span class="logo__text">{COMPANY}<small>{TAGLINE}</small></span>
  </a>
  <nav class="nav"><ul class="nav__list">{''.join(items)}</ul></nav>
  <div class="header__contacts">
    <a class="header__phone" href="tel:{PHONE.replace(' ', '')}">{PHONE}<small>{HOURS}</small></a>
    <a class="btn btn--accent btn--sm" href="{href(prefix, 'contacts')}">Заказать звонок</a>
  </div>
  <button class="burger" aria-label="Меню"><span></span></button>
</div></header>"""


def footer(prefix):
    cols = []
    for slug, title, subs in MENU:
        if slug in ("company", "catalog", "info"):
            links = subs[:6]
            cols.append(f"<div><h4>{title}</h4><ul>" + "".join(
                f'<li><a href="{href(prefix, s)}">{t}</a></li>' for s, t in links) + "</ul></div>")
    return f"""
<footer class="footer"><div class="container">
  <div class="footer__grid">
    <div>
      <a class="logo" href="{href(prefix, '')}"><img src="{prefix}img/logo.png" alt="{COMPANY}"></a>
      <p style="margin-top:18px"><a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>{ADDRESS}<br>{HOURS}</p>
    </div>
    {''.join(cols)}
  </div>
  <div class="footer__bottom"><span>© 2026 {COMPANY}. Все права защищены.</span><a href="#">Политика конфиденциальности</a></div>
</div></footer>
<script src="{prefix}js/main.js"></script>"""


def page(prefix, active, title, body):
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {COMPANY}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Montserrat:ital,wght@0,700;0,800;1,700;1,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>
{header(prefix, active)}
<main>
{body}
</main>
{footer(prefix)}
</body>
</html>
"""


HOME = """
<section class="hero">
  <video class="hero__video" autoplay muted loop playsinline preload="auto" poster="video/hero-poster.jpg" aria-hidden="true">
    <source src="/_blob/46758f094bf4abab2c52dca71b29f148" type="video/mp4">
    <source src="video/hero.mp4" type="video/mp4">
  </video>
  <div class="container">
  <div class="hero__kicker">Контейнерная площадка FDV</div>
  <h1>Морские <span>контейнеры</span> с доставкой по России</h1>
  <p>Продажа, аренда, доставка и установка контейнеров. Подберём под вашу задачу и привезём в срок.</p>
  <div class="hero__actions">
    <a class="btn btn--accent" href="catalog/index.html">Выбрать контейнер</a>
    <a class="btn btn--ghost" href="contacts/index.html">Оставить заявку</a>
  </div>
</div>
  <div class="hero__facts"><div class="container">
    <div class="hero__fact"><b>20′ · 40′ · 40′ HC</b><span>размеры в наличии на площадке</span></div>
    <div class="hero__fact"><b>Новые и б/у</b><span>состояние под вашу задачу и бюджет</span></div>
    <div class="hero__fact"><b>Вся Россия</b><span>доставка и установка контейнера</span></div>
  </div></div>
</section>

<section class="section"><div class="container">
  <div class="section__head">
    <h2 class="section__title">Почему выбирают нас</h2>
    <p class="section__lead">Текст-заглушка: коротко о компании и о том, чем мы отличаемся.</p>
  </div>
  <div class="features">
    <div class="feature"><div class="feature__num">1000+</div><h3>Контейнеров в наличии</h3><p>Новые и б/у, разных типов и размеров.</p></div>
    <div class="feature"><div class="feature__num">РФ</div><h3>Доставка по России</h3><p>Собственная логистика, любой регион.</p></div>
    <div class="feature"><div class="feature__num">−10%</div><h3>Скидки постоянным</h3><p>Гибкие условия и отсрочка платежа.</p></div>
    <div class="feature"><div class="feature__num">24ч</div><h3>Быстрый подбор</h3><p>Предложение в день обращения.</p></div>
  </div>
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section__head">
    <h2 class="section__title">Морские контейнеры</h2>
    <a class="btn btn--outline btn--sm" href="catalog/index.html">Весь каталог</a>
  </div>
  <div class="cards">
    <a class="card" href="catalog/index.html"><div class="card__img"><i></i></div><div class="card__body"><h3>20 футов</h3><p>6 м · 33 м³ · до 28 т. Самый ходовой размер для склада и перевозки.</p><span class="card__link">Подробнее →</span></div></a>
    <a class="card" href="catalog/index.html"><div class="card__img"><i></i></div><div class="card__body"><h3>40 футов</h3><p>12 м · 67 м³ · до 26 т. Для больших объёмов груза.</p><span class="card__link">Подробнее →</span></div></a>
    <a class="card" href="catalog/index.html"><div class="card__img"><i></i></div><div class="card__body"><h3>40 футов High Cube</h3><p>Увеличенная высота 2,9 м · 76 м³. Для лёгких и объёмных грузов.</p><span class="card__link">Подробнее →</span></div></a>
    <a class="card" href="catalog/index.html"><div class="card__img"><i></i></div><div class="card__body"><h3>Рефрижераторные</h3><p>20 и 40 футов для грузов с контролем температуры.</p><span class="card__link">Подробнее →</span></div></a>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section__head"><h2 class="section__title">Как мы работаем</h2></div>
  <div class="steps">
    <div class="step"><h3>Заявка</h3><p>Оставляете заявку на сайте или по телефону.</p></div>
    <div class="step"><h3>Подбор</h3><p>Подбираем контейнер под задачу и бюджет.</p></div>
    <div class="step"><h3>Оплата</h3><p>Бронируем и заключаем договор.</p></div>
    <div class="step"><h3>Доставка</h3><p>Привозим и устанавливаем в согласованное время.</p></div>
  </div>
</div></section>

<section class="section" style="padding-top:0"><div class="container">
  <div class="cta">
    <div><h2>Нужна консультация?</h2><p>Оставьте телефон — перезвоним в течение 15 минут и подберём контейнер.</p></div>
    <form class="form" onsubmit="event.preventDefault(); alert('Форма пока не подключена');">
      <input type="text" placeholder="Ваше имя">
      <input type="tel" placeholder="Телефон" required>
      <button class="btn btn--accent" type="submit">Перезвоните мне</button>
      <small>Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных</small>
    </form>
  </div>
</div></section>
"""


def stub(prefix, title, parent, subs):
    crumbs = f'<a href="{href(prefix, "")}">Главная</a>'
    if parent:
        crumbs += f' / <a href="{href(prefix, parent[0])}">{parent[1]}</a>'
    sub_html = ""
    if subs:
        sub_html = '<div class="sublinks">' + "".join(
            f'<a href="{href(prefix, s)}">{t}</a>' for s, t in subs) + "</div>"
    return f"""
<section class="page-head"><div class="container">
  <div class="crumbs">{crumbs}</div>
  <h1>{title}</h1>
</div></section>
<section class="stub"><div class="container"><div class="stub__box">
  <h2>Раздел в разработке</h2>
  <p>Здесь скоро появится информация.</p>
  {sub_html}
</div></div></section>"""


def write(slug, html):
    path = ROOT / slug / "index.html" if slug else ROOT / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def main():
    write("", page("", "", "Продажа морских контейнеров", HOME))
    done = set()
    for slug, title, subs in MENU:
        pages = [(slug, title)] + subs
        for s, t in pages:
            if s in done:
                continue
            done.add(s)
            prefix = "../" * (s.count("/") + 1)
            is_top = s == slug
            parent = None if is_top else (slug, title)
            write(s, page(prefix, slug, t, stub(prefix, t, parent, subs if is_top else [])))
    print(f"Готово: {len(done) + 1} страниц")


if __name__ == "__main__":
    main()
