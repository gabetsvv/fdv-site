"""Наполнение внутренних страниц. Ключ — slug страницы, значение — функция(prefix, site) -> HTML.
site — модуль build.py (контакты, меню, функции href/containers_html)."""

# Стандартные размеры по ISO 668. У разных производителей значения могут немного отличаться.
DIMENSIONS = [
    # тип, наружные Д×Ш×В (мм), внутренние Д×Ш×В (мм), дверной проём Ш×В (мм), объём м³, тара кг, грузоподъёмность кг, макс. брутто кг
    ("20′ DC (стандарт)", "6058 × 2438 × 2591", "5898 × 2352 × 2393", "2340 × 2280", "33,2", "≈ 2 200", "≈ 28 200", "30 480"),
    ("40′ DC (стандарт)", "12 192 × 2438 × 2591", "12 032 × 2352 × 2393", "2340 × 2280", "67,7", "≈ 3 750", "≈ 26 730", "30 480"),
    ("40′ HC (High Cube)", "12 192 × 2438 × 2896", "12 032 × 2352 × 2698", "2340 × 2585", "76,4", "≈ 3 900", "≈ 26 580", "30 480"),
]

CFO = ["Москва", "Московская область", "Белгородская область", "Брянская область", "Владимирская область",
       "Воронежская область", "Ивановская область", "Калужская область", "Костромская область",
       "Курская область", "Липецкая область", "Орловская область", "Рязанская область",
       "Смоленская область", "Тамбовская область", "Тверская область", "Тульская область",
       "Ярославская область"]

TERMS = [
    ("DC (Dry Cube, Dry Van)", "Стандартный сухогрузный контейнер высотой 2,59 м. Самый распространённый тип."),
    ("HC (High Cube)", "Контейнер повышенной высоты — 2,90 м снаружи. Внутри на 30 см выше стандартного."),
    ("20′ и 40′ (футы)", "Длина контейнера в футах: 20 футов ≈ 6,06 м, 40 футов ≈ 12,19 м."),
    ("TEU", "Двадцатифутовый эквивалент — единица измерения вместимости: один 20′ контейнер = 1 TEU, один 40′ = 2 TEU."),
    ("One Way (новый)", "Контейнер, совершивший один рейс от завода-изготовителя. Практически новый."),
    ("CW (Cargo Worthy)", "Б/у контейнер, пригодный для морской перевозки грузов: герметичный, с исправным каркасом и дверями."),
    ("WWT (Wind and Water Tight)", "Б/у контейнер, защищённый от ветра и воды. Подходит для хранения, но не для морских перевозок."),
    ("Тара (Tare)", "Собственный вес пустого контейнера."),
    ("Грузоподъёмность (Payload)", "Максимальный вес груза, который можно загрузить в контейнер."),
    ("Брутто (Max Gross)", "Максимальный общий вес контейнера вместе с грузом."),
    ("CSC-табличка", "Табличка о допуске контейнера к перевозкам по Международной конвенции о безопасных контейнерах."),
    ("Ричстакер (Reach Stacker)", "Погрузчик с телескопической стрелой для перестановки и погрузки контейнеров."),
]


def _section(inner, soft=False):
    return f'<section class="section{" section--soft" if soft else ""}"><div class="container">{inner}</div></section>'


def contacts(prefix, site):
    return _section(f"""
  <div class="contacts">
    <div class="contacts__list">
      <div class="contact"><span>Телефон</span><a href="tel:{site.PHONE_TEL}">{site.PHONE}</a></div>
      <div class="contact"><span>Почта</span><a href="mailto:{site.EMAIL}">{site.EMAIL}</a></div>
      <div class="contact"><span>Город</span><b>{site.ADDRESS}</b></div>
      <div class="contact"><span>Режим работы</span><b>{site.HOURS}</b></div>
      <div class="contact contact--org"><span>Реквизиты</span><b>{site.ORG}</b><small>ИНН {site.INN} · ОГРНИП {site.OGRNIP}</small></div>
    </div>
    <div class="contacts__map">
      <iframe src="https://yandex.ru/map-widget/v1/?text=%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%BE%D0%B2&amp;z=12" loading="lazy" title="Карта: {site.ADDRESS}" allowfullscreen></iframe>
    </div>
  </div>""") + _section(site.CTA_HTML, soft=True)


def regions(prefix, site):
    items = "".join(f"<li>{r}</li>" for r in CFO)
    return _section(f"""
  <div class="prose">
    <p class="lead">Доставляем морские контейнеры во все {len(CFO)} регионов Центрального федерального округа. Площадка находится в {site.ADDRESS.replace("г. ", "г. ")} — от неё до Москвы и Подмосковья контейнер приезжает быстрее всего.</p>
  </div>
  <ul class="regions">{items}</ul>
  <p class="note">Стоимость доставки зависит от расстояния и размера контейнера — уточните по телефону <a href="tel:{site.PHONE_TEL}">{site.PHONE}</a>.</p>""")


def _dims_table():
    head = "<tr><th>Тип</th><th>Наружные размеры, мм</th><th>Внутренние размеры, мм</th><th>Дверной проём, мм</th><th>Объём, м³</th></tr>"
    rows = "".join(f"<tr><td><b>{t}</b></td><td>{o}</td><td>{i}</td><td>{d}</td><td>{v}</td></tr>" for t, o, i, d, v, *_ in DIMENSIONS)
    return f'<div class="table-wrap"><table class="table">{head}{rows}</table></div>'


def _weights_table():
    head = "<tr><th>Тип</th><th>Тара, кг</th><th>Грузоподъёмность, кг</th><th>Макс. брутто, кг</th><th>Объём, м³</th></tr>"
    rows = "".join(f"<tr><td><b>{t}</b></td><td>{ta}</td><td>{p}</td><td>{g}</td><td>{v}</td></tr>" for t, o, i, d, v, ta, p, g in DIMENSIONS)
    return f'<div class="table-wrap"><table class="table">{head}{rows}</table></div>'


NOTE_ISO = '<p class="note">Указаны стандартные значения по ISO 668. У контейнеров разных производителей размеры и вес могут немного отличаться — точные данные указаны на CSC-табличке на двери контейнера.</p>'


def dimensions(prefix, site):
    return _section(f"""
  <div class="prose"><p class="lead">Габариты морских контейнеров стандартизированы, поэтому их одинаково удобно перевозить на судне, поезде и автомобиле.</p></div>
  {site.containers_html(prefix)}""") + _section(f"<h2 class=\"section__title\">Таблица размеров</h2>{_dims_table()}{NOTE_ISO}", soft=True)


def characteristics(prefix, site):
    return _section(f"""
  <div class="prose">
    <p class="lead">Основные характеристики морских контейнеров, которые помогут выбрать подходящий.</p>
    <h3>Стандартный (DC) или High Cube (HC)?</h3>
    <p>Стандартный контейнер высотой 2,59 м подходит для большинства задач: хранения, перевозки, использования под склад. High Cube на 30 см выше — его выбирают для лёгких объёмных грузов и для переоборудования под бытовку, мастерскую или офис, где важна высота потолка.</p>
    <h3>Новый или б/у?</h3>
    <p><b>Новый (One Way)</b> — контейнер после одного рейса с завода, без следов эксплуатации. <b>Б/у категории CW</b> годится для перевозок, <b>WWT</b> — для хранения: он не протекает и защищает от ветра, но может иметь вмятины и следы ржавчины.</p>
    <h3>Вес и грузоподъёмность</h3>
  </div>
  {_weights_table()}{NOTE_ISO}""")


def dictionary(prefix, site):
    items = "".join(f"<div class=\"term\"><dt>{t}</dt><dd>{d}</dd></div>" for t, d in TERMS)
    return _section(f'<dl class="terms">{items}</dl>')


def catalog(prefix, site):
    return _section(f"""
  <div class="prose"><p class="lead">Продаём морские контейнеры 20 и 40 футов — стандартные и повышенной высоты (High Cube), новые и б/у. Поможем выбрать под вашу задачу и привезём в любой регион ЦФО.</p></div>
  {site.containers_html(prefix)}
  <div class="sublinks" style="justify-content:flex-start;margin-top:32px">
    <a href="{site.href(prefix, 'info/dimensions')}">Габариты контейнеров</a>
    <a href="{site.href(prefix, 'info/characteristics')}">Характеристики</a>
    <a href="{site.href(prefix, 'info/dictionary')}">Словарь терминов</a>
  </div>""") + _section(site.CTA_HTML, soft=True)


def tiles(slug):
    """Страница-раздел: плитки со ссылками на подразделы."""
    def render(prefix, site):
        subs = next(s for sl, t, s in site.MENU if sl == slug)
        items = "".join(f'<a class="tile" href="{site.href(prefix, s)}"><span>{t}</span><i>→</i></a>'
                        for s, t in subs if s != slug)
        return _section(f'<div class="tiles">{items}</div>')
    return render


PAGES = {
    "contacts": contacts,
    "info/regions": regions,
    "info/dimensions": dimensions,
    "info/characteristics": characteristics,
    "info/dictionary": dictionary,
    "catalog": catalog,
    "services": tiles("services"),
    "info": tiles("info"),
}
