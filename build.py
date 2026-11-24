#!/usr/bin/env python3
"""Генератор страниц сайта. Шапка и подвал общие — правятся здесь, затем: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent

COMPANY = "FDV"
TAGLINE = "Продажа контейнеров"
PHONE = "+7 (926) 290-29-39"
PHONE_TEL = "+79262902939"
EMAIL = "fdvcontainer@yandex.ru"
HOURS = "Пн–Вс, 9:00–20:00"
ADDRESS = "г. Дмитров"
ORG = "ИП Волков Пётр Андреевич"
INN = "500724243925"
OGRNIP = "324508100285690"

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
  <div class="topbar__group"><a href="mailto:{EMAIL}">{EMAIL}</a><a class="topbar__group--hide" href="tel:{PHONE_TEL}">{PHONE}</a></div>
</div></div>
<header class="header"><div class="container header__row">
  <a class="logo" href="{href(prefix, '')}">
    <img src="{prefix}img/logo.png" alt="{COMPANY}" onerror="this.remove()">
    <span class="logo__text">{COMPANY}<small>{TAGLINE}</small></span>
  </a>
  <nav class="nav"><ul class="nav__list">{''.join(items)}</ul></nav>
  <div class="header__contacts">
    <a class="header__phone" href="tel:{PHONE_TEL}">{PHONE}<small>{HOURS}</small></a>
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
      <p style="margin-top:18px"><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>{ADDRESS}<br>{HOURS}</p>
    </div>
    {''.join(cols)}
  </div>
  <div class="footer__bottom">
    <div class="footer__org"><span>© 2026 {COMPANY}. Все права защищены.</span><span>{ORG}</span><span>ИНН {INN}</span><span>ОГРНИП {OGRNIP}</span></div>
    <a href="#">Политика конфиденциальности</a>
  </div>
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
  <h1>Морские <span>контейнеры</span> с доставкой во все регионы ЦФО</h1>
  <p>Продажа, доставка, аренда и хранение морских контейнеров</p>
  <div class="hero__actions">
    <a class="btn btn--accent" href="catalog/index.html">Выбрать контейнер</a>
    <a class="btn btn--ghost" href="contacts/index.html">Оставить заявку</a>
  </div>
</div>
  <div class="hero__facts"><div class="container">
    <div class="hero__fact"><b>20′ · 40′ · 40′ HC</b><span>размеры в наличии на площадке</span></div>
    <div class="hero__fact"><b>Новые и б/у</b><span>состояние под вашу задачу и бюджет</span></div>
    <div class="hero__fact"><b>Регионы ЦФО</b><span>доставка во все регионы ЦФО</span></div>
  </div></div>
</section>

<section class="section"><div class="container">
  <div class="section__head">
    <h2 class="section__title">Почему выбирают нас</h2>
    <p class="section__lead">Текст-заглушка: коротко о компании и о том, чем мы отличаемся.</p>
  </div>
  <div class="features">
    <div class="feature"><div class="feature__num">1000+</div><h3>Контейнеров в наличии</h3><p>Новые и б/у, разных типов и размеров.</p></div>
    <div class="feature"><div class="feature__num">ЦФО</div><h3>Доставка во все регионы ЦФО</h3><p>Собственная логистика, привезём в нужное место.</p></div>
    <div class="feature"><div class="feature__num">2 нед.</div><h3>Бронирование контейнера</h3><p>Возможность забронировать подходящий контейнер до 2-х недель.</p></div>
    <div class="feature"><div class="feature__num">24ч</div><h3>Быстрый подбор</h3><p>Предложение в день обращения.</p></div>
  </div>
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section__head">
    <h2 class="section__title">Морские контейнеры</h2>
    <a class="btn btn--outline btn--sm" href="catalog/index.html">Весь каталог</a>
  </div>
CONTAINERS_HTML
</div></section>

<section class="section"><div class="container">
  <div class="section__head"><h2 class="section__title">Как мы работаем</h2></div>
  <div class="steps">
    <div class="step"><h3>Заявка</h3><p>Оставляете заявку на сайте или по телефону.</p></div>
    <div class="step"><h3>Подбор</h3><p>Подбираем контейнер под задачу и бюджет.</p></div>
    <div class="step"><h3>Условия оплаты</h3><p>Утверждаем условия и наиболее удобную форму оплаты.</p></div>
    <div class="step"><h3>Доставка</h3><p>Доставляем контейнер в запланированную дату.</p></div>
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


import math

CONTAINERS = [
    # название, подпись, длина, ширина, высота (м, внешние), объём м³, грузоподъёмность т
    ("20 футов", "Стандарт · 20′ DC", 6.06, 2.44, 2.59, "33,2", "до 28"),
    ("40 футов", "Стандарт · 40′ DC", 12.19, 2.44, 2.59, "67,7", "до 26,5"),
    ("40 футов High Cube", "Повышенный · 40′ HC", 12.19, 2.44, 2.90, "76,4", "до 26,5"),
]


def container_svg(L, W, H):
    """Контейнер в проекции с размерными линиями. Масштаб общий, чтобы размеры сравнивались честно."""
    s = 22.0
    uL = (math.cos(math.radians(16)) * s, math.sin(math.radians(16)) * s)
    uW = (-math.cos(math.radians(42)) * s * .8, math.sin(math.radians(42)) * s * .8)
    ox, oy = 118, 30 + (2.9 - H) * s

    def P(l, w, h):
        return (ox + l * uL[0] + w * uW[0], oy + l * uL[1] + w * uW[1] - h * s + 2.9 * s)

    def poly(pts, cls):
        return f'<polygon class="{cls}" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '"/>'

    def fmt(v):
        return f"{v:.2f}".replace(".", ",")

    out = []
    # грани: верх, длинная сторона (w=W), торец с дверями (l=L)
    out.append(poly([P(0, 0, H), P(L, 0, H), P(L, W, H), P(0, W, H)], "c-top"))
    out.append(poly([P(0, W, 0), P(L, W, 0), P(L, W, H), P(0, W, H)], "c-side"))
    out.append(poly([P(L, 0, 0), P(L, W, 0), P(L, W, H), P(L, 0, H)], "c-end"))
    # гофра на длинной стороне
    n = int(L / .3)
    for k in range(1, n):
        l = L * k / n
        a, c = P(l, W, .08), P(l, W, H - .08)
        out.append(f'<line class="c-rib" x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{c[0]:.1f}" y2="{c[1]:.1f}"/>')
    # двери: створки и запорные штанги
    for w in (W / 2,):
        a, c = P(L, w, 0), P(L, w, H)
        out.append(f'<line class="c-door" x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{c[0]:.1f}" y2="{c[1]:.1f}"/>')
    for w in (W * .18, W * .38, W * .62, W * .82):
        a, c = P(L, w, .15), P(L, w, H - .15)
        out.append(f'<line class="c-bar" x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{c[0]:.1f}" y2="{c[1]:.1f}"/>')

    def dim(p1, p2, off, label, anchor="middle"):
        (x1, y1), (x2, y2) = p1, p2
        x1, y1, x2, y2 = x1 + off[0], y1 + off[1], x2 + off[0], y2 + off[1]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if ang > 90 or ang < -90:
            ang += 180
        return (f'<line class="c-dim" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" marker-start="url(#ar)" marker-end="url(#ar)"/>'
                f'<text class="c-lbl" x="{mx:.1f}" y="{my:.1f}" text-anchor="{anchor}" transform="rotate({ang:.1f} {mx:.1f} {my:.1f}) translate(0 {14 if off[1] > 0 else -6})">{label}</text>')

    out.append(dim(P(0, W, 0), P(L, W, 0), (0, 12), f"{fmt(L)} м"))
    out.append(dim(P(L, W, 0), P(L, 0, 0), (9, 8), f"{fmt(W)} м"))
    a, c = P(0, W, 0), P(0, W, H)
    out.append(f'<line class="c-dim" x1="{a[0]-12:.1f}" y1="{a[1]:.1f}" x2="{c[0]-12:.1f}" y2="{c[1]:.1f}" marker-start="url(#ar)" marker-end="url(#ar)"/>'
               f'<text class="c-lbl" x="{a[0]-18:.1f}" y="{(a[1]+c[1])/2+4:.1f}" text-anchor="end">{fmt(H)} м</text>')
    defs = '<defs><marker id="ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="c-arrow"/></marker></defs>'
    return f'<svg class="cont__svg" viewBox="0 0 430 250" role="img" aria-label="Габариты {fmt(L)} × {fmt(W)} × {fmt(H)} м">{defs}{"".join(out)}</svg>'


def containers_html():
    cards = []
    for name, sub, L, W, H, vol, load in CONTAINERS:
        f = lambda v: f"{v:.2f}".replace(".", ",")
        cards.append(f"""    <a class="cont" href="catalog/index.html">
      <div class="cont__img">{container_svg(L, W, H)}</div>
      <div class="cont__body">
        <span class="cont__sub">{sub}</span>
        <h3>{name}</h3>
        <dl class="cont__specs">
          <div><dt>Длина</dt><dd>{f(L)} м</dd></div>
          <div><dt>Ширина</dt><dd>{f(W)} м</dd></div>
          <div><dt>Высота</dt><dd>{f(H)} м</dd></div>
          <div><dt>Объём</dt><dd>{vol} м³</dd></div>
          <div><dt>Грузоподъёмность</dt><dd>{load} т</dd></div>
        </dl>
        <span class="card__link">Подробнее →</span>
      </div>
    </a>""")
    return '  <div class="conts">\n' + "\n".join(cards) + '\n  </div>'


HOME = HOME.replace("CONTAINERS_HTML", containers_html())


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
