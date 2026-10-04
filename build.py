#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator statyczny strony studia wideopodcastowego.

Uruchomienie:  python3 build.py
Wejscie:       index.html (zrodlo systemu wizualnego), tresc/blog/*.md
Wyjscie:       podstrony w katalogach, blog, sitemap.xml, robots.txt, llms.txt

Zasady twarde (sprawdzane przez audyt na koncu):
  - zero cen w calym serwisie
  - wylacznie myslnik "-"
  - jeden H1 na strone
"""
import os, re, sys, html, json, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
BLOG_DIR = os.path.join(ROOT, 'tresc', 'blog')
# Jedno miejsce na adres. Przy wdrozeniu: podmien DOMENA i ustaw PODGLAD = False,
# inaczej caly serwis zostanie z noindex i nie wejdzie do indeksu.
DOMENA = 'https://kazekdaniel-lab.github.io/gsa-studio'
PODGLAD = True
MARKA = 'GSA Studio'
DZIS = datetime.date.today().isoformat()

# ─────────────────────────────────────────────────────────────
# 1. SYSTEM WIZUALNY - wyciagany z index.html, zeby byl jeden
# ─────────────────────────────────────────────────────────────
def wyciagnij_system():
    src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
    sym = re.search(r'(<svg width="0".*?</svg>)', src, re.S).group(1)
    js  = re.findall(r'<script>(.*?)</script>', src, re.S)[-1]
    return css, sym, js

CSS_PROZA = """
/* ══════════ PROZA I PODSTRONY - arkusz ══════════ */
.proza{max-width:68ch}
.proza h2{font-family:var(--ff-disp);font-weight:500;font-size:clamp(28px,3vw,44px);
  letter-spacing:-.012em;line-height:1.06;margin:56px 0 18px;padding-top:26px;
  border-top:1px solid var(--linia)}
.proza>h2:first-child{margin-top:0;padding-top:0;border-top:0}
.proza h3{font-family:var(--ff-txt);font-size:clamp(18px,1.5vw,21px);font-weight:600;
  letter-spacing:-.008em;margin:34px 0 11px}
.proza p{margin-bottom:17px;font-size:16.5px;line-height:1.65}
.proza ul,.proza ol{margin:0 0 22px 0;padding-left:0;list-style:none;display:grid;gap:10px}
.proza ul li{display:grid;grid-template-columns:11px 1fr;gap:13px;align-items:start;line-height:1.55}
.proza ul li::before{content:'';width:9px;height:9px;margin-top:.52em;background:var(--znak);
  clip-path:polygon(50% 0,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0 50%,40% 40%)}
.proza ol{counter-reset:k}
.proza ol li{counter-increment:k;display:grid;grid-template-columns:34px 1fr;gap:13px;align-items:start}
.proza ol li::before{content:counter(k,upper-roman);font-family:var(--ff-disp);font-size:19px;
  line-height:1.2;color:var(--znak)}
.proza strong{font-weight:600}
.proza a{color:var(--znak);border-bottom:1px solid var(--linia)}
.proza a:hover{border-bottom-color:var(--znak)}
.proza blockquote{border-left:2px solid var(--znak);padding-left:22px;margin:28px 0;
  font-family:var(--ff-disp);font-size:clamp(20px,1.9vw,26px);line-height:1.3}
.proza code{font-family:var(--ff-mono);font-size:.88em;background:var(--tlo-2);padding:2px 6px}
.proza table{width:100%;border-collapse:collapse;margin:28px 0;font-size:15.5px}
.proza th,.proza td{text-align:left;padding:12px 14px 12px 0;border-bottom:1px solid var(--linia)}
.proza thead th{border-bottom:2px solid var(--linia-mocna);font-family:var(--ff-txt);
  font-size:13px;font-weight:500;color:var(--tekst-2)}

/* spis tresci jak metryka arkusza */
.spis{list-style:none;display:grid;gap:9px;border-left:2px solid var(--znak);
  padding-left:24px;margin:32px 0 44px}
.spis a{display:flex;gap:14px;font-family:var(--ff-txt);font-size:14.5px;font-weight:500;
  color:var(--tekst-2)}
.spis a:hover{color:var(--znak)}
.spis .n{color:var(--znak)}

/* karty wpisow - kreski, nie pudelka */
.karty{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;
  border-top:2px solid var(--linia-mocna)}
.karta{display:block;padding:24px 26px 26px 0;border-bottom:1px solid var(--linia);
  border-right:1px solid var(--linia);transition:background .15s var(--ease)}
.karta:hover{background:var(--tlo-2)}
.karta:hover .karta-t{color:var(--znak)}
.karta-t{font-family:var(--ff-disp);font-size:clamp(20px,1.8vw,25px);line-height:1.12;margin-top:11px}
@media(max-width:900px){.karty{grid-template-columns:minmax(0,1fr)}
  .karta{border-right:0;padding-right:0}}

.filtry{display:flex;gap:9px;flex-wrap:wrap;margin:28px 0 8px}
.filtr{font-family:var(--ff-txt);font-size:13.5px;font-weight:500;
  padding:8px 14px;border:1px solid var(--linia);
  color:var(--tekst-2);cursor:pointer;background:transparent}
.filtr:hover{border-color:var(--znak);color:var(--znak)}
.filtr[aria-pressed="true"]{border-color:var(--linia-mocna);background:var(--tekst);color:var(--tlo)}
.grupa{display:contents}

.dalej{border-top:2px solid var(--linia-mocna);margin-top:60px;padding-top:30px}
.autor{display:flex;gap:14px;align-items:center;margin-top:42px;padding-top:24px;
  border-top:1px solid var(--linia)}
"""

# ─────────────────────────────────────────────────────────────
# 2. MINI-MARKDOWN
# ─────────────────────────────────────────────────────────────
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    return t

def md2html(md):
    out, i = [], 0
    linie = md.split('\n')
    while i < len(linie):
        l = linie[i]
        if not l.strip():
            i += 1; continue
        # tabela
        if l.strip().startswith('|') and i + 1 < len(linie) and re.match(r'^\s*\|[\s\-:|]+\|\s*$', linie[i+1]):
            naglowki = [c.strip() for c in l.strip().strip('|').split('|')]
            i += 2
            wiersze = []
            while i < len(linie) and linie[i].strip().startswith('|'):
                wiersze.append([c.strip() for c in linie[i].strip().strip('|').split('|')])
                i += 1
            out.append('<div style="overflow-x:auto"><table><thead><tr>' +
                       ''.join(f'<th>{inline(h)}</th>' for h in naglowki) +
                       '</tr></thead><tbody>' +
                       ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in w) + '</tr>' for w in wiersze) +
                       '</tbody></table></div>')
            continue
        # naglowki
        m = re.match(r'^(#{2,4})\s+(.*)$', l)
        if m:
            poz = len(m.group(1))
            tekst = m.group(2).strip()
            slug = slugify(tekst)
            out.append(f'<h{poz} id="{slug}">{inline(tekst)}</h{poz}>')
            i += 1; continue
        # cytat
        if l.startswith('> '):
            blok = []
            while i < len(linie) and linie[i].startswith('> '):
                blok.append(linie[i][2:]); i += 1
            out.append(f'<blockquote>{inline(" ".join(blok))}</blockquote>')
            continue
        # lista numerowana
        if re.match(r'^\d+[\.\)]\s+', l):
            el = []
            while i < len(linie) and re.match(r'^\d+[\.\)]\s+', linie[i]):
                el.append(re.sub(r'^\d+[\.\)]\s+', '', linie[i])); i += 1
            out.append('<ol>' + ''.join(f'<li><span>{inline(e)}</span></li>' for e in el) + '</ol>')
            continue
        # lista punktowa
        if re.match(r'^[-*]\s+', l):
            el = []
            while i < len(linie) and re.match(r'^[-*]\s+', linie[i]):
                el.append(re.sub(r'^[-*]\s+', '', linie[i])); i += 1
            out.append('<ul>' + ''.join(f'<li><span>{inline(e)}</span></li>' for e in el) + '</ul>')
            continue
        # akapit
        akapit = []
        while i < len(linie) and linie[i].strip() and not re.match(r'^(#{2,4}\s|[-*]\s|\d+[\.\)]\s|\||>\s)', linie[i]):
            akapit.append(linie[i].strip()); i += 1
        if akapit:
            out.append(f'<p>{inline(" ".join(akapit))}</p>')
    return '\n'.join(out)

def skroc(t, n=140):
    """Ucina na granicy slowa, nigdy w polowie wyrazu."""
    t = (t or '').strip()
    if len(t) <= n:
        return t
    return t[:n].rsplit(' ', 1)[0].rstrip(' ,.;:-') + '…'

ZNAKI = str.maketrans('ąćęłńóśżźĄĆĘŁŃÓŚŻŹ ', 'acelnoszzACELNOSZZ-')
def slugify(t):
    t = t.translate(ZNAKI).lower()
    t = re.sub(r'[^a-z0-9\-]+', '-', t)
    return re.sub(r'-{2,}', '-', t).strip('-')[:60]

def parsuj_front(tekst):
    """Prosty parser front-matter: klucz: wartosc, listy przez '-', zagniezdzone faq."""
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', tekst, re.S)
    if not m:
        return {}, tekst
    surowe, body = m.group(1), m.group(2)
    dane, klucz, lista, obiekt = {}, None, None, None
    for l in surowe.split('\n'):
        if not l.strip():
            continue
        if re.match(r'^\s{2,}-\s', l):                       # element listy obiektow
            if obiekt: lista.append(obiekt)
            obiekt = {}
            reszta = re.sub(r'^\s*-\s*', '', l)
            if ':' in reszta:
                k, v = reszta.split(':', 1); obiekt[k.strip()] = v.strip()
            continue
        if re.match(r'^\s{2,}\w+:', l) and obiekt is not None:
            k, v = l.split(':', 1); obiekt[k.strip()] = v.strip(); continue
        if re.match(r'^\s{2,}-\s*\S', l) and lista is not None:
            lista.append(re.sub(r'^\s*-\s*', '', l).strip()); continue
        if re.match(r'^\w[\w\-]*:', l):
            if obiekt: lista.append(obiekt); obiekt = None
            if klucz and lista is not None: dane[klucz] = lista
            lista = None
            k, v = l.split(':', 1)
            klucz, v = k.strip(), v.strip()
            if v == '':
                lista = []
            else:
                dane[klucz] = v
    if obiekt: lista.append(obiekt)
    if klucz and lista is not None: dane[klucz] = lista
    return dane, body

# ─────────────────────────────────────────────────────────────
# 3. SZKIELET STRONY
# ─────────────────────────────────────────────────────────────
MENU = [('/produkcja-podcastow-warszawa/', 'Produkcja'), ('/realizacje/', 'Realizacje'),
        ('/prowadzenie-kanalu/', 'Prowadzenie kanału'), ('/studio/', 'Studio'),
        ('/blog/', 'Blog'), ('/kontakt/', 'Kontakt')]

def naglowek(base, aktywny=''):
    poz = ''.join(f'<a href="{base.rstrip("/")}{u}"{" style=\"color:var(--accent)\"" if u==aktywny else ""}>{n}</a>'
                  for u, n in MENU)
    poz_m = ''.join(f'<a href="{base.rstrip("/")}{u}">{n}</a>' for u, n in MENU)
    return f'''<header><div class="grid"><div class="hd">
  <div style="display:flex;align-items:center;min-width:0">
    <a href="{base}" class="brand"><i class="star"></i>GSA Studio</a></div>
  <nav class="mono" aria-label="Nawigacja">{poz}</nav>
  <div style="display:flex;align-items:center;gap:20px">
    <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="menu">Menu</button>
    <a href="{base.rstrip("/")}/kontakt/" class="pill">Umów rozmowę</a>
  </div>
</div></div></header>
<div class="menu-panel" id="menu">{poz_m}
  <a href="{base.rstrip("/")}/kontakt/" class="pill">Umów rozmowę</a>
</div>'''

def stopka(base):
    b = base.rstrip('/')
    linki = ''.join(f'<a href="{b}{u}">{n}</a>' for u, n in MENU)
    return f'''<footer class="pad-tight"><div class="grid">
  <div class="foot">
    <div><a href="{base}" class="brand" style="margin-bottom:16px"><i class="star"></i>GSA Studio</a>
      <p class="marg" style="max-width:34ch">Studio wideopodcastowe w Warszawie. Jeden dzień zdjęciowy, komplet plików gotowych do wrzucenia.</p></div>
    <div class="mono" style="flex-direction:column;align-items:flex-start;gap:12px">
      <span>Warszawa</span><span class="slot">[ULICA I NUMER]</span></div>
    <div class="mono" style="flex-direction:column;align-items:flex-start;gap:12px">
      <span class="slot">[TELEFON]</span><span class="slot">[E-MAIL]</span></div>
    <div class="mono" style="flex-direction:column;align-items:flex-start;gap:12px">{linki}</div>
  </div>
  <div class="foot-bot mono"><span>© 2026 GSA Studio</span>
    <span style="display:flex;gap:22px"><a href="{b}/polityka-prywatnosci/">Polityka prywatności</a><a href="{b}/regulamin/">Regulamin</a></span></div>
</div></footer>'''

ROBOTS = ('<meta name="robots" content="noindex,nofollow">' if PODGLAD
          else '<meta name="robots" content="index,follow,max-image-preview:large">')


def strona(tytul, opis, tresc, base='../', kanon='/', schema=None, aktywny=''):
    # Serwis moze stac w podkatalogu (GitHub Pages), wiec kazdy link od korzenia
    # przepisujemy na relatywny wzgledem glebokosci strony.
    tresc = re.sub(r'(href|src)="/(?!/)', lambda m: f'{m.group(1)}="{base}', tresc)
    ld = ''
    if schema:
        ld = '\n'.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(tytul)}</title>
<meta name="description" content="{html.escape(opis)}">
{ROBOTS}
<link rel="canonical" href="{DOMENA}{kanon}">
<meta property="og:title" content="{html.escape(tytul)}">
<meta property="og:description" content="{html.escape(opis)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{DOMENA}{kanon}">
<meta property="og:site_name" content="{MARKA}">
<meta property="og:locale" content="pl_PL">
<link rel="stylesheet" href="{base}assets/site.css">
<noscript><style>.cut{{opacity:1}}.mask>span{{clip-path:none}}.menu-panel{{display:block;position:static;padding-top:0}}.menu-btn{{display:none}}</style></noscript>
{ld}
</head>
<body>
{SYMBOLE}
{naglowek(base, aktywny)}
{tresc}
{stopka(base)}
<script src="{base}assets/site.js"></script>
</body>
</html>'''

def okruszki(base, sciezka):
    """sciezka: lista (url, nazwa)"""
    el = ''.join(f'<span><a href="{base.rstrip("/")}{u}">{n}</a></span>' if u else f'<span>{n}</span>'
                 for u, n in sciezka)
    return f'<p class="mono kruszywo"><span><a href="{base}">Start</a></span>{el}</p>'

def ld_okruszki(sciezka):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMENA + (u or '/')}
        for i, (u, n) in enumerate(sciezka)]}

LD_FIRMA = {"@context": "https://schema.org", "@type": "LocalBusiness", "name": MARKA,
            "description": "Studio wideopodcastowe w Warszawie. Nagranie, montaż, rolki, opisy i publikacja.",
            "areaServed": "Warszawa", "url": DOMENA,
            "address": {"@type": "PostalAddress", "addressLocality": "Warszawa", "addressCountry": "PL"}}

def ld_faq(pary):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": o}} for p, o in pary]}

# ─────────────────────────────────────────────────────────────
# 4. PODSTRONY USLUGOWE I INFORMACYJNE
# ─────────────────────────────────────────────────────────────
STRONY = [
 dict(url='/produkcja-podcastow-warszawa/', tytul='Produkcja podcastów Warszawa - nagranie i montaż',
   opis='Pełna produkcja wideopodcastów w Warszawie. Nagranie, montaż, rolki pionowe, opisy i publikacja. Jeden dzień na planie, materiał na miesiąc.',
   h1='Produkcja podcastów <br>od formatu po komplet plików', eyebrow='Usługa główna',
   odp='Pełna produkcja oznacza, że po Twojej stronie zostaje jeden dzień zdjęciowy i akceptacja materiału. Format, przygotowanie gości, nagranie, montaż, krótkie formy pionowe, opisy i transkrypcje są po naszej. Wrzucanie zostaje u Ciebie, a przechodzi na nas przy prowadzeniu całego kanału.',
   body='''
## Dla kogo jest pełna produkcja

Dla firm, które chcą mieć kanał, a nie pojedyncze nagranie. Najczęściej pracujemy z trzema typami klientów.

- **Firma budująca markę eksperta.** Ktoś z zarządu albo z zespołu ma wiedzę, której nie widać na rynku. Podcast robi z niej materiał, który pracuje przez lata.
- **Marka osobista.** Osoba, która już mówi publicznie, ale robi to nieregularnie i bez oprawy.
- **Zespół sprzedaży B2B.** Rozmowy z klientami i partnerami jako materiał, który skraca cykl sprzedaży, bo odpowiada na pytania, zanim padną.

## Co obejmuje produkcja end-to-end

Pięć etapów. Twój jest jeden.

1. **Format i oprawa.** Ustalamy, jak wygląda pojedynczy odcinek: układ planu, aranżacja, długość i oprawa graficzna. O czym są odcinki, decydujesz Ty.
2. **Przygotowanie planu.** Harmonogram zjazdu, ustawienie planu i sprzętu, techniczne ustalenia z gościem. Tematy i nazwiska podajesz Ty.
3. **Dzień zdjęciowy.** Światło stoi, dźwięk zebrany, kamery ustawione. Nagrywamy blokowo.
4. **Postprodukcja.** Cięcie, przełączanie kadrów, kolor, mastering dźwięku, napisy, formaty pionowe.
5. **Publikacja.** Odcinek, opis, tagi, miniatura, transkrypcja. Konta zostają Twoje.

Rozpisaliśmy to szczegółowo w tekście [jak wygląda nagranie wideopodcastu krok po kroku](/blog/jak-wyglada-nagranie-wideopodcastu/).

## Co dostajesz z jednego zjazdu

Nagrywamy blokiem, więc jeden dzień w studiu daje materiał na cały miesiąc. Zamiast czterech osobnych wizyt blokujesz jeden dzień.

| Materiał | Format |
|---|---|
| Zmontowane odcinki | mp4, 4K i 1080p |
| Rolki pionowe z napisami | 1080×1920 |
| Wersja audio | mp3 |
| Transkrypcja i napisy | txt, srt |
| Opis, tytuł, rozdziały i tagi | txt |
| Miniatury do testu | png |
| Zdjęcia ze zjazdu | jpg |

Więcej o ekonomii takiego dnia w tekście o [nagrywaniu blokowym](/blog/batch-recording-nagrywanie-blokowe/).

## Jakie formaty nagrywamy

| Format | Osoby | Kamery | Kadry |
|---|---|---|---|
| Wideopodcast | 2 | 3 | 2 medium close-up i szeroki |
| Panel | 3-4 | 4 | medium close-up na każdą osobę i szeroki |
| Talking head | 1 | 2 | medium i detal |
| Kurs online | 1-2 | 3 | medium, prompter |

Nagrywamy w ISO, czyli każda kamera i każdy mikrofon na osobnej ścieżce. W montażu da się przez to uratować kaszel, przejęzyczenie i dzwoniący telefon.

## Ile to zajmuje Twojego czasu

Jeden dzień zdjęciowy w miesiącu plus około godziny rozłożonej na akceptacje. Wszystko pozostałe jest po naszej stronie. Rozbiliśmy to na godziny w tekście [ile Twojego czasu zjada podcast firmowy](/blog/ile-czasu-zajmuje-podcast-firmowy/).

## Jak ustalamy zakres

Nie mamy jednego zestawu dla wszystkich. Są trzy poziomy zaangażowania: pojedyncze odcinki, serie i prowadzenie całego kanału. Różnią się tym, ile pracy zostaje po Twojej stronie. Rozpisaliśmy je na stronie [prowadzenia kanału](/prowadzenie-kanalu/).
''',
   faq=[('Kto wymyśla tematy i dobiera gości?','Ty. Merytoryka, tematy i kontakty do gości zostają po Twojej stronie na każdym poziomie współpracy, bo to Twoja wiedza i Twoja sieć. My odpowiadamy za to, jak rozmowa wygląda i brzmi, i za wszystko, co dzieje się z materiałem po nagraniu.'),
        ('Ile odcinków można nagrać jednego dnia?','Zależy od formatu i od tego, ile osób jest na planie. Nagrywamy blokowo, bo każdy kolejny odcinek tego samego dnia idzie szybciej niż pierwszy. Liczbę ustalamy przy planowaniu zjazdu.'),
        ('Kto pisze opisy i publikuje odcinki?','Zależy od poziomu zakresu. Przy serii i przy prowadzeniu kanału opisy, tagi, miniatury i publikacja są po naszej stronie. Konta pozostają Twoje, my mamy dostęp roboczy.'),
        ('Do kogo należą materiały?','Do Ciebie. Wszystkie prawa do nagrania i materiałów końcowych przechodzą na Ciebie po rozliczeniu. Fragment w portfolio pokazujemy wyłącznie za Twoją zgodą.'),
        ('Czy nagrywacie poza studiem?','Podstawowym miejscem jest nasze studio, bo tam mamy kontrolę nad akustyką i światłem. Nagrania w Twojej siedzibie ustalamy indywidualnie.')]),

 dict(url='/rolki-shorty-talking-head/', tytul='Shorty i krótkie formy pionowe dla firm',
   opis='Krótkie formy pionowe dla firm: rolki wycinane z odcinka i talking head kręcony osobno. 1080×1920, napisy wypalane, gotowe do publikacji.',
   h1='Krótkie formy pionowe, <br>które działają same', eyebrow='Usługa',
   odp='Krótkie formy powstają na dwa sposoby: jako fragmenty wycięte z dłuższego nagrania albo jako materiał kręcony osobno przed kamerą. Pierwsze są tańsze w produkcji, drugie dają pełną kontrolę nad przekazem. Oba dostajesz w pionie 1080×1920, z wypalonymi napisami i gotowe do wrzucenia.',
   body='''
## Skąd bierze się materiał na rolki

Są dwa źródła i różnią się nie tylko ceną pracy, ale też efektem.

**Wycinane z odcinka.** Jeśli nagrywasz wideopodcast, każdy odcinek zawiera kilka fragmentów, które bronią się samodzielnie. Wycinamy je, kadrujemy w pionie, dodajemy napisy. Zaleta: zero dodatkowego czasu przed kamerą. Ograniczenie: fragment musi być zrozumiały bez kontekstu.

**Kręcone osobno jako talking head.** Siadasz przed kamerą i nagrywasz serię krótkich wypowiedzi pod konkretne tematy. Zaleta: pełna kontrola nad przekazem i pierwszą sekundą. Koszt: osobna sesja.

Rozwinęliśmy to porównanie w tekście o [produkcji rolek dla firmy](/blog/produkcja-rolek-dla-firmy/).

## Ile rolek wychodzi z jednego nagrania

Z godziny rozmowy realnie wychodzi kilka fragmentów, które są warte publikacji. Nie każdy odcinek daje tyle samo - to zależy od tego, ile w nim jest konkretnych, samodzielnych myśli. Odcinek zbudowany z anegdot da mniej niż odcinek zbudowany z tez.

## Format techniczny

| Parametr | Wartość |
|---|---|
| Rozdzielczość | 1080×1920 |
| Napisy | wypalane, kontrolowane ręcznie |
| Bezpieczne marginesy | pod interfejs każdej platformy |
| Pierwsza sekunda | kadrowana pod zatrzymanie przewijania |
| Wersje | osobne pod Reels, TikTok, Shorts i LinkedIn |

## Dlaczego napisy są wypalane

Bo automatyczne napisy platform mylą się na nazwach własnych, na branżowym słownictwie i na polskiej odmianie. Wypalony napis wygląda tak samo wszędzie i nie znika, gdy ktoś ogląda w aplikacji, która ich nie renderuje.

## Co robi krótka forma dla kanału

Krótkie formy są głównym sposobem docierania do osób, które Cię jeszcze nie znają. Długi materiał buduje relację z tymi, którzy już weszli. Rozpisaliśmy ten mechanizm w tekście [shorty z podcastu i zasięg kanału](/blog/shorty-z-podcastu-zasieg/).

## W naszym studiu

Talking head nagrywamy z prompterem, bo przy krótkich formach liczy się precyzja pierwszego zdania. Rolki z odcinków przygotowujemy w ramach tej samej postprodukcji, więc nie trzeba ich zamawiać osobno.
''',
   faq=[('Czy mogę zamówić same rolki, bez podcastu?','Tak. Talking head jest osobnym formatem i nie wymaga prowadzenia kanału podcastowego. Nagrywamy serię krótkich wypowiedzi w jednej sesji.'),
        ('Ile trwa sesja talking head?','Zależy od liczby tematów i od tego, czy korzystasz z promptera. Planujemy ją tak, żeby wyjść z materiałem na kilka tygodni publikacji.'),
        ('Czy przygotowujecie osobne wersje pod różne platformy?','Tak. Różnią się bezpiecznymi marginesami i długością, bo interfejs każdej platformy zasłania inną część kadru.')]),

 dict(url='/nagrania-szkoleniowe-kursy-online/', tytul='Nagrania szkoleniowe i kursy online Warszawa',
   opis='Produkcja materiałów e-learningowych i kursów online w Warszawie. Podział na moduły, prompter, napisy, pliki gotowe pod platformy szkoleniowe.',
   h1='Kursy online <br>i materiały szkoleniowe', eyebrow='Usługa',
   odp='Nagranie kursu różni się od nagrania podcastu przede wszystkim strukturą. Materiał dzielimy na moduły, które da się później aktualizować pojedynczo, a nie nagrywać całość od nowa. Prompter jest tu standardem, nie dodatkiem, bo treść szkoleniowa musi być precyzyjna.',
   body='''
## Trzy typy materiałów, które nagrywamy

- **Moduły wykładowe.** Kurs sprzedawany albo udostępniany klientom. Podzielony na lekcje, każda samodzielna.
- **Onboarding pracowniczy.** Materiał, który ogląda każda nowa osoba w firmie. Nagrywa się raz, działa latami.
- **Szkolenia produktowe.** Dla zespołu sprzedaży albo dla partnerów handlowych. Aktualizowane przy każdej zmianie w produkcie.

## Dlaczego podział na moduły jest decyzją produkcyjną

Kurs nagrany jako jedna długa całość starzeje się w całości. Wystarczy zmiana w jednym procesie i trzeba nagrywać wszystko od nowa. Kurs podzielony na krótkie moduły aktualizuje się modułami.

To wpływa na sposób nagrywania: unikamy odwołań do sąsiednich lekcji, nie mówimy "jak wspominałem w poprzednim module", nie numerujemy lekcji w treści mówionej.

## Prompter

Przy podcastach prompter rzadko się przydaje, bo rozmowa ma brzmieć jak rozmowa. Przy kursach jest praktycznie obowiązkowy, bo treść musi być kompletna i precyzyjna, a osoba przed kamerą nie może improwizować definicji.

## Co dostajesz

| Materiał | Format |
|---|---|
| Moduły wideo | mp4, 1080p i 4K |
| Napisy | srt, osobno na moduł |
| Transkrypcja | txt |
| Wersja audio | mp3 |
| Miniatury lekcji | png |

## Ile trwa nagranie kursu

Zależy od liczby modułów i od tego, czy scenariusz jest gotowy. Największym pożeraczem czasu nie jest nagrywanie, tylko brak przygotowanej treści. Opisaliśmy cały proces w tekście [jak nagrać profesjonalny kurs online](/blog/jak-nagrac-kurs-online/).
''',
   faq=[('Czy pomagacie napisać scenariusz kursu?','Pomagamy ułożyć podział na moduły i długość pojedynczej lekcji, bo to wpływa na sposób nagrywania i późniejsze aktualizacje. Merytoryka zostaje po Twojej stronie, bo to Twoja wiedza jest produktem.'),
        ('Czy nagrywacie z prezentacją na ekranie?','Tak. Grafiki i slajdy wchodzą w montażu jako pełne przebitki albo jako element kadru.'),
        ('W jakich formatach dostaję pliki?','W formatach gotowych pod typowe platformy szkoleniowe, razem z napisami i transkrypcją każdego modułu.')]),

 dict(url='/jak-pracujemy/', tytul='Jak pracujemy - 5 etapów produkcji podcastu',
   opis='Proces produkcji podcastu w 5 etapach: format, przygotowanie, dzień zdjęciowy, postprodukcja, publikacja. Co jest po Twojej stronie, a co po naszej.',
   h1='Pięć etapów. <br>Twoje są dwa', eyebrow='Proces',
   odp='Produkcja dzieli się na 5 etapów. Twoja obecność jest wymagana w dwóch: przy ustaleniu formatu i w dniu zdjęciowym. Przygotowanie i postprodukcja idą po naszej stronie, a Ty dostajesz materiał do akceptacji. Wrzucanie zostaje u Ciebie, a przechodzi na nas przy prowadzeniu całego kanału.',
   body='''
## Etap 1 - format i oprawa

Ustalamy, jak wygląda pojedynczy odcinek: układ planu, aranżacja, długość, oprawa graficzna i to, co ma wychodzić z jednego zjazdu.

Merytoryka zostaje po Twojej stronie. Tematy, dobór gości i to, o czym mówisz, są Twoje, bo to Twoja wiedza i Twoje kontakty. My odpowiadamy za to, jak to wygląda i brzmi na ekranie.

## Etap 2 - przygotowanie planu

Harmonogram zjazdu, ustawienie planu i sprzętu, techniczne ustalenia z gościem: o której ma być, ile potrwa, jak się ubrać. Tematy i nazwiska podajesz Ty.

Co warto wysłać gościowi przed nagraniem, opisaliśmy w tekście [jak przygotować gościa do podcastu](/blog/jak-przygotowac-goscia-do-podcastu/).

## Etap 3 - dzień zdjęciowy

Światło stoi, dźwięk zebrany, kamery ustawione, zanim wejdziesz. Nagrywamy blokowo, bo każdy kolejny odcinek tego samego dnia idzie szybciej niż pierwszy.

To jedyny etap, który wymaga Twojej pełnej obecności. Przebieg godzina po godzinie opisaliśmy w tekście [jak wygląda nagranie](/blog/jak-wyglada-nagranie-wideopodcastu/).

## Etap 4 - postprodukcja

Cięcie, przełączanie kadrów, kolor, czyszczenie i mastering dźwięku, napisy, formaty pionowe. Dostajesz podgląd do akceptacji.

Uwagi zbieramy na osi czasu materiału, a nie mailem z opisem minut. Dzięki temu wiadomo dokładnie, którego momentu dotyczy uwaga.

## Etap 5 - publikacja

Odcinek, opis, tagi, miniatura, transkrypcja. Konta zostają Twoje, my mamy dostęp roboczy.

## Podział odpowiedzialności

| Etap | Po Twojej stronie | Po naszej stronie |
|---|---|---|
| Format i oprawa | tematy, goście, merytoryka | układ planu, aranżacja, oprawa |
| Przygotowanie planu | podanie tematów i nazwisk | harmonogram, plan, sprzęt, logistyka |
| Dzień zdjęciowy | obecność i rozmowa | plan, sprzęt, realizacja |
| Postprodukcja | uwagi do podglądu | całość pracy |
| Publikacja | nic | opisy, tagi, miniatury, wrzucenie |
''',
   faq=[('Ile rund uwag mam do materiału?','Liczbę rund ustalamy na starcie. W praktyce przy ustalonym formacie druga runda zdarza się rzadko, bo pierwsza wersja trafia w oczekiwania.'),
        ('Co jeśli gość odwoła w ostatniej chwili?','Przy stałej współpracy przesuwamy termin w ramach ustalonego okresu. Przy pojedynczym nagraniu ustalamy nowy termin.'),
        ('Jak długo przechowujecie materiały?','Materiał zapisujemy równolegle na dwóch nośnikach w trakcie nagrania. Czas przechowywania po dostarczeniu plików ustalamy w umowie.')]),

 dict(url='/sprzet/', tytul='Sprzęt studia - kamery, dźwięk, światło',
   opis='Specyfikacja techniczna studia wideopodcastowego: kamery, mikrofony, światło, nagrywanie ISO, formaty wyjściowe i backup materiału.',
   h1='Specyfikacja techniczna', eyebrow='Sprzęt',
   odp='Porównywanie ofert bez modeli sprzętu nie ma sensu, dlatego trzymamy pełną listę w jednym miejscu. Najważniejsza pozycja to nagrywanie ISO, czyli osobna ścieżka dla każdej kamery i każdego mikrofonu. To ono decyduje o tym, ile da się poprawić w montażu.',
   body='''
## Obraz

- Kamery: <span class="slot">[MODEL]</span>, rejestracja w 4K
- Obiektywy: <span class="slot">[MODELE]</span>
- Nagrywanie ISO, każda kamera zapisuje osobny plik
- Spójna kolorystyka między korpusami, korekcja w postprodukcji

## Dźwięk

- Mikrofony: <span class="slot">[MODEL]</span>
- Interfejs i rejestrator: <span class="slot">[MODEL]</span>
- Osobna ścieżka na każdą osobę
- Czyszczenie i mastering w postprodukcji

## Światło

- Źródła: <span class="slot">[MODELE]</span>
- Schemat trzypunktowy, standaryzowany dla wszystkich osób na planie
- Światło praktyczne jako element scenografii

## Formaty wyjściowe

| Materiał | Format |
|---|---|
| Odcinek poziomy | 4K i 1080p, mp4 |
| Krótkie formy | 1080×1920, mp4, napisy wypalane |
| Audio | mp3 |
| Napisy i transkrypcja | srt i txt |

## Backup

Materiał zapisywany jest równolegle podczas nagrania, więc awaria jednego nośnika nie kończy się utratą zdjęć. Po sesji materiał trafia na dysk roboczy i pozostaje dostępny przez ustalony okres.

## Dlaczego ISO ma znaczenie dla Ciebie

Bez ISO montażysta dostaje jeden gotowy miks obrazu i dźwięku. Każda pomyłka na planie zostaje w materiale na zawsze. Z ISO da się usunąć kaszel jednej osoby bez wycinania zdania drugiej, zmienić decyzję o tym, kogo pokazujemy, i uratować fragment, w którym ktoś mówi jednocześnie.

Rozwinęliśmy to w tekście [ile kamer potrzebuje Twój podcast](/blog/ile-kamer-do-podcastu/).
''',
   faq=[('Czy mogę przyjść z własnym sprzętem?','Możesz przynieść materiały do pokazania na ekranie. Sprzęt zdjęciowy i dźwiękowy jest po naszej stronie, bo cały plan jest pod niego ustawiony.'),
        ('Czy dostaję surowe pliki?','Standardowo dostajesz materiał zmontowany i przygotowany do publikacji. Przekazanie surówek ustalamy indywidualnie.'),
        ('Ile kamer używacie przy rozmowie dwóch osób?','Trzy: po jednym kadrze medium close-up na każdą osobę i jeden szeroki na przejścia i kontekst.')]),

 dict(url='/o-nas/', tytul='O nas - studio prowadzone przez praktyków',
   opis='Prowadzimy własny podcast Growth, Scale & Automate. Znamy tę robotę od strony osoby, która wchodzi do studia z tematem i patrzy potem na statystyki.',
   h1='Robimy to <br>najpierw u siebie', eyebrow='Kto to robi',
   odp='Prowadzimy podcast Growth, Scale & Automate. Znamy tę robotę od strony osoby, która musi wejść do studia z tematem, a potem patrzeć na statystyki. Dlatego rozmawiamy z klientem jak operator, a nie jak usługodawca.',
   body='''
## Skąd to się wzięło

Przez pierwsze miesiące własnego podcastu popełniliśmy praktycznie każdy błąd, który da się popełnić. Zły format, za długie odcinki, tematy wybierane w piątek na następny wtorek, montaż, który zjadał więcej czasu niż nagranie. Nic z tego nie jest teorią.

Studio powstało z tego, czego się przy okazji nauczyliśmy. Nie z pomysłu na wynajem sali.

## Czym się to różni w praktyce

Usługodawca sprzedaje zakres prac. **My wiemy, w którym momencie kanał się sypie i co trzeba wtedy zmienić**, bo sami przez ten moment przeszliśmy.

To widać w trzech miejscach: przy ustalaniu formatu, przy wyborze fragmentów na krótkie formy i przy tym, co dzieje się z odcinkiem w drugim i trzecim tygodniu po publikacji.

## Zespół

Prowadzenie projektu, realizacja na planie i montaż. Przy stałej współpracy masz jeden punkt kontaktu, a nie skrzynkę zbiorczą.

Oskar Szarek prowadzi GSA i realnie współbuduje marki, więc rozmowa o Twoim kanale nie kończy się na liście pytań do gościa. Jeśli chcesz, siada z Tobą jako gospodarz Twojego formatu.
''',
   faq=[('Czy mogę zobaczyć studio przed decyzją?','Tak. Pokazujemy studio, ustawiamy przed kamerą i nagrywamy próbne kilka minut, żebyś zobaczył, jak to wygląda.'),
        ('Czy pracujecie tylko z firmami?','Głównie z firmami i markami osobistymi, które chcą prowadzić kanał regularnie, a nie nagrać jeden materiał.')]),
]

STRONY += [
 dict(url='/studio/', tytul='Studio wideopodcastowe Warszawa - przestrzeń',
   opis='Studio wideopodcastowe w Warszawie: wygłuszona sala, 3 aranżacje planu, światło ustawiane pod markę, zaplecze i dojazd.',
   h1='Miejsce, w którym <br>nic Cię nie rozprasza', eyebrow='Studio',
   odp='Studio jest wygłuszone, z trzema aranżacjami planu i światłem ustawianym pod Twoją markę. Przyjeżdżasz na gotowe: plan stoi, dźwięk jest zebrany, kamery ustawione. Przy stałej współpracy aranżację można zmieniać między odcinkami, żeby odcinki nie wyglądały identycznie.',
   body='''
## Trzy aranżacje planu

Jedna sala, trzy różne miejsca. Każda aranżacja ma inny kolor dominujący i inne przeznaczenie, więc dwa odcinki nagrane tego samego dnia nie wyglądają jak ten sam materiał.

- **Aranżacja ciemna, kinowa.** Pod rozmowy jeden na jeden i tematy biznesowe.
- **Aranżacja jasna, ciepła.** Pod rozmowy kameralne i tematy lżejsze.
- **Aranżacja z mocnym akcentem.** Pod panele i formaty publicystyczne.

Wybór ustalamy przed nagraniem. Wpływ tła na odbiór marki opisaliśmy w tekście o [scenografii podcastu](/blog/scenografia-podcastu/).

## Dane techniczne sali

| Parametr | Wartość |
|---|---|
| Powierzchnia | <span class="slot">[X]</span> m² |
| Wysokość | <span class="slot">[X]</span> m |
| Maksymalnie osób na planie | <span class="slot">[X]</span> |
| Reżyserka | <span class="slot">[TAK/NIE]</span> |
| Aranżacje planu | 3 |

## Zaplecze

Garderoba, miejsce na przygotowanie, kuchnia, klimatyzacja. Kawa, herbata i woda są w cenie każdej sesji, bo zjazd zdjęciowy trwa kilka godzin i nikt nie powinien go spędzić na szukaniu wody.

## Dojazd

<span class="slot">[ULICA I NUMER]</span>, Warszawa. <span class="slot">[X]</span> minut pieszo od stacji metra <span class="slot">[NAZWA]</span>, przystanki autobusowe <span class="slot">[NUMERY]</span>. Na miejscu <span class="slot">[X]</span> miejsc parkingowych dla klientów.

## Czy to jest wynajem sali

Nie. Pracujemy w modelu produkcyjnym, czyli razem z realizacją i postprodukcją, bo tylko wtedy odpowiadamy za efekt końcowy. Jeśli szukasz samej przestrzeni na godziny, powiedz to na starcie i skierujemy Cię gdzie indziej, zamiast sprzedawać coś, czego nie potrzebujesz.

Porównanie obu modeli opisaliśmy w tekście [samoobsługa czy studio z realizatorem](/blog/samoobsluga-czy-studio-z-realizatorem/).
''',
   faq=[('Czy mogę zobaczyć studio przed nagraniem?','Tak i to rekomendujemy. Pokazujemy salę, ustawiamy Cię przed kamerą i nagrywamy próbne kilka minut, żebyś zobaczył, jak wyglądasz w kadrze.'),
        ('Ile osób mieści się na planie?','Plan jest przygotowany pod rozmowy dwuosobowe i panele do czterech osób. Przy większej liczbie ustalamy układ indywidualnie.'),
        ('Czy jest parking?','Tak, na miejscu. Liczbę miejsc podajemy przy potwierdzeniu terminu.')]),

 dict(url='/realizacje/', tytul='Realizacje - odcinki i krótkie formy',
   opis='Materiał wideo, który realnie wypuszczamy: odcinki podcastu GSA i krótkie formy. Obejrzyj, zanim zadzwonisz.',
   h1='Najpierw kadry, <br>potem obietnice', eyebrow='Realizacje',
   odp='Zaczynamy od własnego kanału, bo to jedyny materiał, który możemy pokazać bez pytania nikogo o zgodę. Poniżej odcinki podcastu GSA, który nagrywamy i wydajemy sami. Realizacje klientów dokładamy tu po każdej publikacji, za zgodą.',
   dodatek='''<section class="dark pad-norm"><div class="grid">
  <div class="c2-7"><p class="mono"><span>Własny kanał</span><span>Podcast GSA</span></p>
    <h2 class="h-sec" style="margin-top:20px">Co wypuszczamy <br>tydzień po tygodniu</h2>
    <p class="lead" style="margin-top:24px">Ponad 70 odcinków rozmów z ludźmi, którzy budują firmy w Polsce. Kliknij dowolny i oceń sam.</p></div>
  <div class="dowody">{KAFLE}</div>
</div></section>''',
   body='''
## Co tu znajdziesz

Odcinki wideopodcastów, krótkie formy pionowe i materiały szkoleniowe. Przy każdej realizacji podajemy format, liczbę kamer i to, co dokładnie było po naszej stronie.

## Katalog

Realizacje klientów dokładamy po każdej publikacji i wyłącznie za zgodą. Przy części projektów nie pokazujemy nic, bo tak wynika z umowy. Jeśli chcesz zobaczyć konkretny format albo branżę, napisz - pokażemy materiał, którego nie ma jeszcze publicznie.

## Dlaczego to jest najważniejsza strona serwisu

Sprawdziliśmy strony studiów w Warszawie: na większości nie da się obejrzeć ani jednego odcinka, który z nich wyszedł. Deklaracja o jakości nic nie znaczy, dopóki nie widać efektu.
''',
   faq=[('Czy pokazujecie materiały klientów bez ich zgody?','Nie. Fragment w portfolio pokazujemy wyłącznie za zgodą, a przy części projektów nie pokazujemy nic, bo tak wynika z umowy.'),
        ('Czy mogę zobaczyć realizacje z mojej branży?','Napisz, w czym działasz. Pokażemy materiał najbliższy Twojemu formatowi, także taki, którego nie ma publicznie.')]),
]

STRONY_PROSTE = [
 dict(url='/polityka-prywatnosci/', tytul='Polityka prywatności', opis='Polityka prywatności serwisu.',
      h1='Polityka prywatności', body='<p class="lead">Dokument do uzupełnienia przed publikacją serwisu.</p>'),
 dict(url='/regulamin/', tytul='Regulamin', opis='Regulamin świadczenia usług.',
      h1='Regulamin', body='<p class="lead">Dokument do uzupełnienia przed publikacją serwisu.</p>'),
]

HUBY = {'koszty':('/produkcja-podcastow-warszawa/','Produkcja podcastów'),
        'wybor':('/produkcja-podcastow-warszawa/','Produkcja podcastów'),
        'proces':('/jak-pracujemy/','Jak pracujemy'),
        'strategia':('/prowadzenie-kanalu/','Prowadzenie kanału'),
        'dystrybucja':('/prowadzenie-kanalu/','Prowadzenie kanału'),
        'szkolenia':('/nagrania-szkoleniowe-kursy-online/','Nagrania szkoleniowe i kursy')}

KLASTRY = {'koszty':'Koszty i wycena','wybor':'Wybór studia','proces':'Proces nagrania',
           'strategia':'Strategia podcastu','dystrybucja':'Dystrybucja i efekt','szkolenia':'Szkolenia i kursy'}

# ─────────────────────────────────────────────────────────────
# 5. RENDEROWANIE
# ─────────────────────────────────────────────────────────────
def zapisz(url, tresc):
    kat = os.path.join(ROOT, url.strip('/'))
    os.makedirs(kat, exist_ok=True)
    with open(os.path.join(kat, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(tresc)

def sekcja_faq(pary, base=''):
    if not pary:
        return ''
    el = ''.join(f'''<div><p class="qn">{str(i+1).zfill(2)}</p><h3 class="h-line">{html.escape(p)}</h3><p>{html.escape(o)}</p></div>'''
                 for i, (p, o) in enumerate(pary))
    return f'''<section class="light pad-norm"><div class="grid">
  <div class="c2-6"><p class="mono"><span>Pytania</span></p>
    <h2 class="h-sec" style="margin-top:20px">Częste pytania</h2></div>
  <div class="c1-12 qa" style="margin-top:56px">{el}</div>
</div></section>'''

def render_usluga(s):
    base = '../'
    faq = [(p, o) for p, o in s.get('faq', [])]
    tresc = f'''<section class="canvas glow-l pad-norm" style="padding-top:140px">
  <div class="grid"><div class="c1-8">
    {okruszki(base, [(s['url'], s['tytul'].split(' - ')[0])])}
    <p class="mono"><span>{s['eyebrow']}</span><span>Warszawa</span></p>
    <h1 class="h-hero" style="margin-top:22px;font-size:clamp(38px,4.6vw,72px)">{s['h1']}</h1>
    <p class="odp" style="border-color:var(--accent);color:var(--ink)">{html.escape(s['odp'])}</p>
    <a href="{base}kontakt/" class="pill">Umów rozmowę</a>
  </div></div>
</section>
<section class="light pad-norm"><div class="grid"><div class="c2-7 proza">{md2html(s['body'])}</div></div></section>
{s.get('dodatek', '').replace('{KAFLE}', kafle_dowodow(base))}
{sekcja_faq(faq)}
<section class="canvas glow-r pad-norm"><div class="grid"><div class="c1-6">
  <h2 class="h-sec">Zacznijmy od rozmowy</h2>
  <p class="lead" style="margin-top:22px">Pokażemy studio, ustawimy Cię przed kamerą i nagramy próbne 5 minut.</p>
  <a href="{base}kontakt/" class="pill" style="margin-top:32px">Umów rozmowę</a>
</div></div></section>'''
    schema = [LD_FIRMA,
              {"@context":"https://schema.org","@type":"Service","name":s['tytul'].split(' - ')[0],
               "provider":{"@type":"LocalBusiness","name":MARKA},"areaServed":"Warszawa",
               "description":s['opis']},
              ld_okruszki([(s['url'], s['tytul'].split(' - ')[0])])]
    if faq:
        schema.append(ld_faq(faq))
    return strona(s['tytul'] + f' | {MARKA}', s['opis'], tresc, base, s['url'], schema)

def render_prosta(s):
    base = '../'
    tresc = f'''<section class="light pad-norm" style="padding-top:150px"><div class="grid"><div class="c2-7 proza">
      {okruszki(base, [(s['url'], s['h1'])])}
      <h1 class="h-sec">{s['h1']}</h1>{s['body']}</div></div></section>'''
    return strona(s['tytul'] + f' | {MARKA}', s['opis'], tresc, base, s['url'], [ld_okruszki([(s['url'], s['h1'])])])

def render_artykul(a, wszystkie):
    base = '../../'
    h2 = re.findall(r'^##\s+(.*)$', a['body'], re.M)
    spis = ''.join(f'<li><a href="#{slugify(t)}"><span class="n">{str(i+1).zfill(2)}</span><span>{html.escape(t)}</span></a></li>'
                   for i, t in enumerate(h2))
    faq = [(f.get('pytanie',''), f.get('odpowiedz','')) for f in a.get('faq', []) if isinstance(f, dict)]
    hub_url, hub_nazwa = HUBY.get(a.get('klaster',''), ('/produkcja-podcastow-warszawa/', 'Produkcja podcastów'))
    if hub_url == '/prowadzenie-kanalu/':
        usluga = (f'Robimy to na trzech poziomach zaangażowania, od pojedynczego odcinka po prowadzenie '
                  f'całego kanału: <a href="{base.rstrip("/")}{hub_url}">{hub_nazwa}</a>.')
    else:
        usluga = (f'Ten temat wchodzi w zakres naszej usługi: <a href="{base.rstrip("/")}{hub_url}">{hub_nazwa}</a>. '
                  f'Poziomy współpracy rozpisaliśmy na stronie '
                  f'<a href="{base.rstrip("/")}/prowadzenie-kanalu/">prowadzenia kanału</a>.')
    powiazane = ''
    slugi = [s for s in a.get('linki', []) if s in wszystkie and s != a['slug']][:3]
    if slugi:
        powiazane = '<div class="karty" style="margin-top:26px">' + ''.join(
            f'''<a class="karta" href="{base}blog/{s}/"><p class="mono"><span>{KLASTRY.get(wszystkie[s]["klaster"],"")}</span></p>
                <p class="karta-t">{html.escape(wszystkie[s]["tytul"])}</p></a>''' for s in slugi) + '</div>'
    tresc = f'''<section class="light pad-norm" style="padding-top:150px"><div class="grid">
  <div class="c2-7">
    {okruszki(base, [('/blog/','Blog'), ('', KLASTRY.get(a['klaster'],''))])}
    <h1 class="h-sec" style="margin-top:8px">{html.escape(a['tytul'])}</h1>
    <p class="odp">{html.escape(a.get('odpowiedz',''))}</p>
    <ul class="spis">{spis}</ul>
    <div class="proza">{md2html(a['body'])}</div>
    <div class="dalej">
      <p class="mono"><span>Usługa</span></p>
      <p style="margin-top:14px">{usluga}</p>
      <p class="mono" style="margin-top:40px"><span>Czytaj dalej</span></p>
      {powiazane}
    </div>
  </div>
</div></section>
{sekcja_faq(faq)}
<section class="canvas glow-r pad-norm"><div class="grid"><div class="c1-6">
  <h2 class="h-sec">Chcesz to zrobić u siebie?</h2>
  <p class="lead" style="margin-top:22px">Pokażemy studio i ustalimy format, zanim cokolwiek zablokujemy w kalendarzu.</p>
  <a href="{base}kontakt/" class="pill" style="margin-top:32px">Umów rozmowę</a>
</div></div></section>'''
    schema = [{"@context":"https://schema.org","@type":"Article","headline":a['tytul'],
               "description":a.get('opis',''),"inLanguage":"pl-PL",
               "author":{"@type":"Organization","name":MARKA},
               "publisher":{"@type":"Organization","name":MARKA},
               "mainEntityOfPage":DOMENA+'/blog/'+a['slug']+'/'},
              ld_okruszki([('/blog/','Blog'), ('/blog/'+a['slug']+'/', a['tytul'])])]
    if faq:
        schema.append(ld_faq(faq))
    return strona(a.get('tytul_seo') or a['tytul'], a.get('opis',''), tresc, base, '/blog/'+a['slug']+'/', schema)

def render_blog(arts):
    base = '../'
    wg = {}
    for a in arts.values():
        wg.setdefault(a['klaster'], []).append(a)
    filtry = ''.join(f'<button class="filtr" data-k="{k}" aria-pressed="false">{n}</button>' for k, n in KLASTRY.items())
    grupy = ''
    for k, n in KLASTRY.items():
        if k not in wg: continue
        karty = ''.join(f'''<a class="karta" href="{base}blog/{a['slug']}/" data-k="{k}">
            <p class="karta-t" style="margin-top:0">{html.escape(a['tytul'])}</p>
            <p>{html.escape(skroc(a.get('opis','')))}</p></a>''' for a in wg[k])
        grupy += f'''<div class="grupa" data-k="{k}" style="margin-bottom:64px">
          <p class="mono" style="margin-bottom:24px"><span>{n}</span><span>{len(wg[k])} tekstów</span></p>
          <div class="karty">{karty}</div></div>'''
    tresc = f'''<section class="light pad-norm" style="padding-top:150px"><div class="grid">
  <div class="c1-8">{okruszki(base, [('', 'Blog')])}
    <p class="mono"><span>{len(arts)} tekstów</span><span>6 klastrów</span></p>
    <h1 class="h-sec" style="margin-top:14px">Wszystko, o co pytają przed pierwszym nagraniem</h1>
    <p class="lead" style="margin-top:26px">Koszty, wybór studia, przebieg nagrania, format i to, co dzieje się z odcinkiem po publikacji.</p>
  </div>
  <div class="c1-12" style="margin-top:64px"><div class="filtry">{filtry}</div>{grupy}</div>
</div></section>
<script>
document.querySelectorAll('.filtr').forEach(b=>b.addEventListener('click',()=>{{
  const on=b.getAttribute('aria-pressed')==='true';
  document.querySelectorAll('.filtr').forEach(x=>x.setAttribute('aria-pressed','false'));
  b.setAttribute('aria-pressed',String(!on));
  document.querySelectorAll('.grupa').forEach(g=>{{
    g.style.display=(on||g.dataset.k===b.dataset.k)?'':'none';}});
}}));
</script>'''
    return strona(f'Blog - produkcja podcastów, koszty, proces | {MARKA}',
                  'Teksty o produkcji podcastów: od czego zależy koszt, jak wybrać studio, jak wygląda nagranie i co dzieje się z odcinkiem po publikacji.',
                  tresc, base, '/blog/', [ld_okruszki([('/blog/','Blog')])])

def render_kontakt():
    base = '../'
    tresc = f'''<section class="canvas glow-r pad-norm" style="padding-top:150px"><div class="grid" style="row-gap:56px">
  <div class="c1-6">{okruszki(base, [('/kontakt/','Kontakt')])}
    <p class="mono"><span>Zgłoszenie</span></p>
    <h1 class="h-sec" style="margin-top:20px">Najpierw przyjedź. <br><span class="acc">Potem zdecydujesz.</span></h1>
    <p class="lead" style="margin-top:26px">Pokażemy studio, ustawimy Cię przed kamerą i nagramy próbne 5 minut. Napisz, co chcesz nagrywać i dla kogo.</p>
    <div class="brace" style="margin-top:52px;padding-block:24px;max-width:520px"><div class="kontakt-blok">
      <div class="kv"><span class="mono"><span>Adres</span></span><span class="slot">[ULICA I NUMER, WARSZAWA]</span></div>
      <div class="kv"><span class="mono"><span>Telefon</span></span><span class="slot">[NUMER]</span></div>
      <div class="kv"><span class="mono"><span>E-mail</span></span><span class="slot">[ADRES E-MAIL]</span></div>
    </div></div>
  </div>
  <div class="c8-12"><form class="sheet" id="zgloszenie" novalidate>
    <div class="f-row"><div class="field"><label for="f1">Imię i nazwisko</label><input id="f1" required></div>
      <div class="field"><label for="f2">Firma albo marka</label><input id="f2"></div></div>
    <div class="field"><label for="f3">Co chcesz nagrywać</label><textarea id="f3"></textarea></div>
    <div class="f-row"><div class="field"><label for="f4">Jak często</label>
      <select id="f4"><option>Jednorazowo</option><option>Raz w miesiącu</option><option>Kilka razy w miesiącu</option><option>Jeszcze nie wiem</option></select></div>
      <div class="field"><label for="f5">Poziom zakresu</label>
      <select id="f5"><option>Pojedyncze odcinki</option><option>Serie</option><option>Cały kanał</option><option>Jeszcze nie wiem</option></select></div></div>
    <div class="field"><label for="f6">Telefon albo e-mail</label><input id="f6" required></div>
    <button class="pill" type="submit" style="justify-self:start;margin-top:8px">Wyślij zgłoszenie</button>
    <p class="marg" id="stan">Odpowiadamy na każde zgłoszenie, także wtedy, gdy uznamy, że to nie jest robota dla nas.</p>
  </form></div>
</div></section>'''
    return strona(f'Kontakt | {MARKA}', 'Umów wizytę w studiu wideopodcastowym w Warszawie. Pokażemy studio i nagramy próbne 5 minut.',
                  tresc, base, '/kontakt/', [LD_FIRMA, ld_okruszki([('/kontakt/','Kontakt')])])

# ─────────────────────────────────────────────────────────────
# 5b. PROWADZENIE KANALU - trzy poziomy wejscia
# ─────────────────────────────────────────────────────────────

# Odcinki wlasnego podcastu GSA. Identyfikatory wyciagniete z gsa/odcinki/,
# miniatury leca prosto z YouTube, wiec nie trzymamy ich w repo.
DOWODY = [
    ('4i750BGR7ZM', 'Strategia firmy to nie 300 slajdów', 'Marcin Czyczerski',
     'podcast-gsa-strategia-firmy-marcin-czyczerski'),
    ('gP9jATbTaR8', 'Jak OSHEE wygrało z Powerade i Gatorade', 'Aleksander Woś',
     'podcast-gsa-oshee-marka-napojow-aleksander-wos'),
    ('ISzBXDLPJXE', 'HYROX: model biznesowy fenomenu', 'Mateusz Krogulec',
     'podcast-gsa-hyrox-model-biznesowy-mateusz-krogulec'),
    ('am1tq4CP77o', 'Omnichannel w beauty', 'Agnieszka Bernaś-Oleszczuk',
     'podcast-gsa-omnichannel-beauty-agnieszka-bernas-oleszczuk'),
    ('H17LIwgJSMQ', 'Jak zrobić 100 mln sprzedaży w B2B', 'Krzysztof Pawlak',
     'podcast-gsa-sprzedaz-b2b-krzysztof-pawlak'),
    ('6Uqk0F0rNJg', '200 mln w 3 lata: strategia biznesowa', 'Konrad Kwiatkowski',
     'podcast-gsa-strategia-wzrostu-konrad-kwiatkowski'),
]

# Wiersz matrycy: (nazwa, dopisek, I, II, III). Wartosci: True, False albo tekst.
MATRYCA = [
    ('Ustalenie formatu i oprawy', 'układ planu, aranżacja, długość, grafika', True, True, True),
    ('Nagranie w studiu', 'światło, dźwięk, kamery, obsługa planu', True, True, True),
    ('Montaż odcinka', 'cięcie, przełączanie kadrów, kolor, mastering', True, True, True),
    ('Krótkie formy pionowe', '1080x1920, napisy wypalone', True, True, True),
    ('Napisy i transkrypcja', 'srt oraz txt', True, True, True),
    ('Opis, tytuł, rozdziały i tagi', 'gotowe do wklejenia', False, True, True),
    ('Miniatury', 'wersje do testu A/B', False, True, True),
    ('Spójna oprawa całej serii', 'żeby odcinki czytały się jak jedna całość', False, True, True),
    ('Stały termin zjazdów w kalendarzu', 'blokowany z góry na kwartał', False, True, True),
    ('Publikacja na platformach', 'konta zostają Twoje, my mamy dostęp roboczy', False, False, True),
    ('Archiwum materiałów', 'surówki i pliki źródłowe pod ręką', False, False, True),
    ('Raport wydań', 'co i kiedy wyszło, co poszło dalej', False, False, True),
    ('Tematy, goście i merytoryka', 'to samo na każdym poziomie', 'Ty', 'Ty', 'Ty'),
]

POZIOMY = [
    dict(rz='I', nazwa='Pojedyncze odcinki', dla='Kiedy sprawdzasz, czy to w ogóle Twoje',
         opis='Jeden temat, jedno wejście do studia, komplet materiału na wyjściu. '
              'Wchodzisz z gotowym pomysłem albo układamy go w trakcie jednej rozmowy. '
              'Najczęściej wybierane wtedy, gdy ktoś chce najpierw zobaczyć, jak wygląda i brzmi na ekranie, '
              'zanim zablokuje sobie kalendarz na pół roku.',
         ty=['Temat i gość', 'Jeden dzień w studiu', 'Akceptacja materiału'],
         my=['Ustawienie planu i sprzętu', 'Nagranie', 'Montaż odcinka',
             'Krótkie formy pionowe', 'Napisy i transkrypcja', 'Pliki gotowe do publikacji'],
         linia=['Nagranie', 'Montaż', 'Krótkie formy', 'Napisy', 'Pliki']),
    dict(rz='II', nazwa='Seria', dla='Kiedy masz temat i osobę, brakuje regularności',
         opis='Cykl z ustalonym formatem i stałym terminem w kalendarzu. Nagrywamy blokowo, '
              'więc jeden dzień zdjęciowy daje materiał na cały miesiąc. '
              'Tu zaczyna się praca, której przy pojedynczym odcinku nie widać: '
              'żeby dziesiąty odcinek wyglądał jak pierwszy, a nie jak zupełnie inny kanał.',
         ty=['Tematy i goście', 'Zjazd raz na ustalony okres', 'Akceptacja materiału'],
         my=['Wszystko z poziomu I', 'Spójna oprawa całej serii', 'Harmonogram zjazdów',
             'Opisy, tytuły, rozdziały i tagi', 'Miniatury do testu',
             'Pliki opisane i gotowe do wrzucenia'],
         linia=['Wszystko z I', 'Spójna oprawa', 'Stały termin', 'Opisy', 'Miniatury']),
    dict(rz='III', nazwa='Cały kanał', dla='Kiedy ma rosnąć, a Ty nie masz na to zespołu',
         opis='Prowadzimy produkcję kanału jako całość. Ty przynosisz tematy, gości i wiedzę, '
              'my odpowiadamy za wszystko, co dzieje się ze sprzętem, materiałem i plikami, '
              'łącznie z wrzuceniem odcinka na platformy i pilnowaniem, żeby wychodził wtedy, kiedy ma wyjść. '
              'Po Twojej stronie zostaje jeden dzień w miesiącu i decyzje kierunkowe.',
         ty=['Tematy i goście', 'Merytoryka i decyzje kierunkowe', 'Jeden dzień zdjęciowy w miesiącu'],
         my=['Wszystko z poziomu II', 'Regularne zjazdy w kalendarzu',
             'Krótkie formy pod każdą platformę', 'Publikacja na platformach',
             'Archiwum materiałów', 'Raport z tego, co i kiedy wyszło'],
         linia=['Wszystko z II', 'Publikacja', 'Archiwum', 'Raport wydań']),
]

GRANICE = [
    ('01', 'Nie wymyślimy, na czym się znasz',
     'Z tego, co przyniesiesz, ułożymy format, kolejność odcinków i plan zjazdów. '
     'Ale wiedzy nie da się oddać w outsourcing. Jeśli wchodzisz bez konkretu, po trzecim odcinku '
     'nie ma o czym nagrywać i widać to na ekranie.'),
    ('02', 'Nie usiądziemy przed kamerą za Ciebie',
     'Ktoś z firmy musi mówić i musi to robić regularnie. Nie musi być mówcą, bo od tego jest '
     'montaż i drugie podejście. Musi być i musi chcieć.'),
    ('03', 'Nie obiecamy zasięgu',
     'Nikt uczciwy nie obieca. Odpowiadamy za to, żeby materiał wyglądał, brzmiał i wychodził na czas. '
     'Co się z nim stanie dalej, zależy głównie od tego, czy masz coś do powiedzenia.'),
]

FAQ_POZIOMY = [
    ('Ile to kosztuje?',
     'Zależy od poziomu i od tego, ile odcinków ma wychodzić miesięcznie. Przy trzech i przy dziesięciu '
     'to są dwie różne roboty, więc widełki na stronie nic by Ci nie powiedziały. Po rozmowie dostajesz '
     'konkretną kwotę na konkretny zakres, nie przedział.'),
    ('Czy muszę mieć już kanał?',
     'Nie. Na poziomie I i II nie ma to znaczenia. Przy prowadzeniu całego kanału istniejące konto '
     'jest wygodniejsze na starcie, bo widać, co już działało, ale zaczynaliśmy też od zera.'),
    ('Co jeśli nie wiem, jak ma wyglądać odcinek?',
     'To normalne i rzadko ktoś to wie. Układ planu, długość, oprawę i kolejność ustalamy razem '
     'na pierwszym etapie. Nie ustalimy za Ciebie tylko jednego: o czym masz mówić.'),
    ('Ile mojego czasu to realnie zajmuje?',
     'Na poziomie III jeden dzień zdjęciowy w miesiącu plus krótka akceptacja materiału. '
     'Na poziomie II tyle samo, ale rzadziej. Reszta nie wymaga Twojej obecności, także wtedy, '
     'gdy coś trzeba poprawić.'),
    ('Czy mogę zmienić poziom w trakcie?',
     'Tak i tak to najczęściej wygląda. Ktoś zaczyna od jednego odcinka, po dwóch albo trzech widzi, '
     'ile pracy jest poza nagraniem, i przechodzi wyżej. W drugą stronę też się da.'),
    ('Co jeśli w danym miesiącu nie dam rady przyjechać?',
     'Przesuwamy zjazd w ramach ustalonego okresu. Dlatego nagrywamy blokowo, bo zapas materiału '
     'oznacza, że jeden przesunięty termin nie wywraca harmonogramu publikacji.'),
    ('Do kogo należą materiały?',
     'Do Ciebie. Wszystkie prawa do nagrania i plików końcowych przechodzą na Ciebie po rozliczeniu. '
     'Fragment w portfolio pokazujemy wyłącznie za Twoją zgodą.'),
    ('Na jak długo się wiążę?',
     'Bez umów lojalnościowych. Warunki wypowiedzenia ustalamy na starcie i są symetryczne, '
     'czyli obowiązują nas tak samo jak Ciebie.'),
]


def odmiana(n, poj, kilka, wiele):
    """1 pozycja / 3 pozycje / 6 pozycji"""
    if n == 1: return f'{n} {poj}'
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: return f'{n} {kilka}'
    return f'{n} {wiele}'


def _komorka(v, kol):
    kl = ' class="kol-III"' if kol == 'III' else ''
    if v is True:
        return f'<td{kl}><span class="jest" role="img" aria-label="w zakresie">+</span></td>'
    if v is False:
        return f'<td{kl}><span class="brak" role="img" aria-label="poza zakresem"></span></td>'
    return f'<td{kl}><span class="txt">{html.escape(str(v))}</span></td>'


def kafle_dowodow(base):
    """Siatka kadrow z wlasnego podcastu. Ten sam material na stronie poziomow i w realizacjach."""
    return ''.join(f'''<figure>
      <a class="frame frame--link" style="aspect-ratio:16/9" href="https://www.youtube.com/watch?v={v}"
         target="_blank" rel="noopener" aria-label="Obejrzyj na YouTube: {html.escape(t)}">
        <img src="{base}assets/kadry/{k}.webp" alt="Kadr z odcinka podcastu GSA: {html.escape(t)}, gość {html.escape(g)}"
             width="960" height="540" loading="lazy" decoding="async">
        <span class="gra"><i><svg><use href="#play"/></svg></i></span></a>
      <figcaption><p class="t">{html.escape(t)}</p>
        <p class="mono"><span>{html.escape(g)}</span><span>Podcast GSA</span></p></figcaption></figure>'''
        for v, t, g, k in DOWODY)


def render_poziomy():
    base = '../'
    url = '/prowadzenie-kanalu/'

    granice = ''.join(f'''<div><p class="n">{n}</p><h3>{html.escape(t)}</h3><p>{html.escape(o)}</p></div>'''
                      for n, t, o in GRANICE)

    pasma = ''
    for i, p in enumerate(POZIOMY):
        ty = ''.join(f'<li><i class="star"></i>{html.escape(x)}</li>' for x in p['ty'])
        my = ''.join(f'<li><i class="star"></i>{html.escape(x)}</li>' for x in p['my'])
        linia = ''.join(f'<span>{html.escape(x)}</span>' for x in p['linia'])
        pasma += f'''
  <div class="pasmo pasmo-{p['rz']}">
    <div class="grid"><div class="pasmo-body cut">
      <span class="rzym" aria-hidden="true">{p['rz']}</span>
      <p class="mono"><span>Poziom {p['rz']}</span></p>
      <div class="poz-head"><h3>{html.escape(p['nazwa'])}</h3></div>
      <p class="poz-dla">{html.escape(p['dla'])}</p>
      <p class="lead" style="margin-top:22px;max-width:62ch">{html.escape(p['opis'])}</p>
      <div class="mikro">
        <div><span class="chip chip--ty">Po Twojej stronie</span><span class="licz">{odmiana(len(p['ty']), 'pozycja', 'pozycje', 'pozycji')}</span>
          <ul>{ty}</ul></div>
        <div><span class="chip chip--my">Po naszej stronie</span><span class="licz">{odmiana(len(p['my']), 'pozycja', 'pozycje', 'pozycji')}</span>
          <ul>{my}</ul></div>
      </div>
      <p class="mono" style="margin-top:32px">{linia}</p>
    </div></div>
  </div>'''

    wiersze = ''.join(
        f'''<tr><th scope="row">{html.escape(n)}<small>{html.escape(d)}</small></th>'''
        f'''{_komorka(a,'I')}{_komorka(b,'II')}{_komorka(c,'III')}</tr>'''
        for n, d, a, b, c in MATRYCA)

    kafle = kafle_dowodow(base)

    tresc = f'''<section class="canvas glow-l" style="padding-top:150px;padding-bottom:var(--norm)">
  <div class="grid">
    <div class="c1-8">
      {okruszki(base, [(url, 'Prowadzenie kanału')])}
      <p class="mono"><span>Dla firm i marek eksperckich</span><span>Warszawa</span></p>
      <h1 class="h-hero" style="margin-top:22px;font-size:clamp(38px,5vw,84px)">Trzy poziomy. <br>
        <span class="acc">Od jednego odcinka <br>do całego kanału.</span></h1>
      <p class="lead" style="margin-top:30px;max-width:54ch">Nie każdy musi od razu oddawać cały kanał.
        Poniżej trzy poziomy, które różnią się jedną rzeczą: ile pracy zostaje po Twojej stronie.
        Merytoryka zostaje u Ciebie na każdym z nich, bo tego nie da się przekazać.</p>
      <div class="hero-cta">
        <a href="{base}kontakt/" class="pill">Umów rozmowę</a>
        <a href="#matryca" class="link-arrow">Porównaj poziomy ↓</a>
      </div>
    </div>
    <div class="licznik">
      <div><p class="v">1</p><p class="k mono"><span>Dzień zdjęciowy w miesiącu</span></p></div>
      <div><p class="v"><i class="slot">[X]</i></p><p class="k mono"><span>Odcinków z jednego zjazdu</span></p></div>
      <div><p class="v"><i class="slot">[X]</i><span class="suf">h</span></p><p class="k mono"><span>Twojego czasu na odcinek</span></p></div>
      <div><p class="v"><i class="slot">[X]</i><span class="suf">m²</span></p><p class="k mono"><span>Studio w Warszawie</span></p></div>
    </div>
    <div class="c1-12"><p class="mono" style="margin-top:56px;padding-top:26px;border-top:1px solid var(--hairline)">
      <span>Nagrywamy blokowo</span><span>Rejestracja ISO</span>
      <span>Pliki gotowe do publikacji</span><span>Prawa do materiału po Twojej stronie</span></p></div>
  </div>
</section>

<section class="light pad-norm">
  <div class="grid">
    <div class="c1-6">
      <p class="mono"><span>Granica zakresu</span></p>
      <h2 class="h-sec" style="margin-top:20px">Czego nie zrobimy <br>za Ciebie</h2>
      <p class="lead" style="margin-top:24px">Zaczynamy od tego, bo to jest jedyna część oferty,
        której nie da się dopisać później. Reszta to kwestia zakresu.</p>
    </div>
    <div class="granica">{granice}</div>
  </div>
</section>

<section class="dark">{pasma}</section>

<section class="light pad-norm" id="matryca">
  <div class="grid">
    <div class="c2-7">
      <p class="mono"><span>Porównanie</span><span>Trzy poziomy</span></p>
      <h2 class="h-sec" style="margin-top:20px">Co wchodzi <br>na którym poziomie</h2>
      <p class="lead" style="margin-top:24px">Ostatni wiersz jest taki sam w każdej kolumnie i to nie jest przeoczenie.</p>
    </div>
    <div class="matryca">
      <p class="mono matryca-hint"><span>Przewiń tabelę w bok</span></p>
      <div class="matryca-skrol">
      <table>
        <caption>Zakres prac na trzech poziomach współpracy</caption>
        <thead><tr><th scope="col"><span class="nz">Zakres</span></th>
          <th scope="col"><span class="rz">I</span><span class="nz">Pojedyncze odcinki</span></th>
          <th scope="col"><span class="rz">II</span><span class="nz">Seria</span></th>
          <th scope="col" class="kol-III"><span class="rz">III</span><span class="nz">Cały kanał</span></th></tr></thead>
        <tbody>{wiersze}</tbody>
      </table>
      </div>
      <p class="marg matryca-noga">Zakres poza tabelą ustalamy na rozmowie. Jeśli czegoś potrzebujesz,
        a nie ma tego wyżej, to zwykle znaczy, że da się to zrobić, tylko nikt dotąd o to nie pytał.</p>
    </div>
  </div>
</section>

<section class="dark pad-norm">
  <div class="grid">
    <div class="c2-7">
      <p class="mono"><span>Dowód</span><span>Własny kanał</span></p>
      <h2 class="h-sec" style="margin-top:20px">Zanim oddasz <br>komuś swój kanał</h2>
      <p class="lead" style="margin-top:24px">Zobacz, jak ktoś prowadzi własny. Poniżej odcinki podcastu GSA,
        który nagrywamy i wydajemy sami, tydzień po tygodniu. Nie cudze realizacje z portfolio.</p>
    </div>
    <div class="dowody">{kafle}</div>
    <div class="c1-12" style="margin-top:44px">
      <p class="marg" style="max-width:62ch">Przez pierwsze miesiące własnego kanału popełniliśmy
        prawie każdy możliwy błąd: zły format, za długie odcinki, tematy wybierane w piątek na wtorek.
        Dlatego rozmawiamy o Twoim kanale jak ktoś, kto to robi, a nie jak ktoś, kto to sprzedaje.</p>
    </div>
  </div>
</section>

<section class="light pad-norm">
  <div class="grid">
    <div class="c1-6">
      <p class="mono"><span>Przebieg</span><span>Jeden miesiąc</span></p>
      <h2 class="h-sec" style="margin-top:20px">Jak wygląda <br>miesiąc współpracy</h2>
      <p class="lead" style="margin-top:24px">Na poziomie III. Niżej ten sam przebieg, tylko rzadziej.</p>
    </div>
    <div class="c1-12" style="margin-top:56px">
      <div class="etap"><span class="n">01</span>
        <div><h3 class="h-line">Ustalenie tematów</h3>
          <p class="body">Przysyłasz listę tematów albo nazwisk. Odsiewamy to, co się powtarza,
            układamy kolejność i mówimy, czego brakuje, żeby zjazd miał sens.</p></div>
        <span class="chip chip--ty">Po Twojej stronie</span></div>
      <div class="etap"><span class="n">02</span>
        <div><h3 class="h-line">Dzień zdjęciowy</h3>
          <p class="body">Jeden dzień w studiu, blok odcinków. Światło stoi, dźwięk zebrany, kamery ustawione,
            zanim wejdziesz. Każdy kolejny odcinek tego samego dnia idzie szybciej niż pierwszy.</p></div>
        <span class="chip chip--ty">Po Twojej stronie</span></div>
      <div class="etap"><span class="n">03</span>
        <div><h3 class="h-line">Postprodukcja</h3>
          <p class="body">Montaż, kolor, dźwięk, krótkie formy pionowe, napisy, miniatury, opisy.
            Uwagi zbieramy na osi czasu materiału, nie mailem z listą minut.</p></div>
        <span class="chip chip--my">Po naszej stronie</span></div>
      <div class="etap"><span class="n">04</span>
        <div><h3 class="h-line">Wydania przez cały miesiąc</h3>
          <p class="body">Odcinki i krótkie formy wychodzą według harmonogramu ustalonego przed zjazdem.
            Konta zostają Twoje, my mamy dostęp roboczy. Na koniec miesiąca dostajesz raport, co i kiedy wyszło.</p></div>
        <span class="chip chip--my">Po naszej stronie</span></div>
    </div>
  </div>
</section>

<section class="canvas pad-norm">
  <div class="grid">
    <div class="c1-6">
      <p class="mono"><span>Dopasowanie</span></p>
      <h2 class="h-sec" style="margin-top:20px">Dla kogo to jest, <br>a dla kogo nie</h2>
    </div>
    <div class="kontra">
      <div><span class="chip chip--my">To jest dla Ciebie</span>
        <h3>Jeśli którekolwiek z tych zdań jest o Tobie</h3>
        <ul>
          <li><i class="star"></i>Masz wiedzę, o którą klienci pytają w rozmowach handlowych</li>
          <li><i class="star"></i>Ktoś w firmie jest gotowy usiąść przed kamerą i robić to regularnie</li>
          <li><i class="star"></i>Możesz oddać jeden dzień w miesiącu na nagrania</li>
          <li><i class="star"></i>Chcesz, żeby całość szła przez jeden zespół, a nie przez pięć podpiętych zleceń</li>
          <li><i class="star"></i>Zależy Ci na regularności bardziej niż na jednym efektownym materiale</li>
        </ul></div>
      <div class="nie"><span class="chip">To nie jest dla Ciebie</span>
        <h3>Tu lepiej poszukać gdzie indziej</h3>
        <ul>
          <li>Potrzebujesz jednego filmu reklamowego i tyle</li>
          <li>Szukasz najtańszego montażu na rynku</li>
          <li>Liczysz na zasięg w pierwszym miesiącu</li>
          <li>Nie ma w firmie nikogo, kto chce występować</li>
          <li>Oczekujesz, że wymyślimy za Ciebie, o czym mówić</li>
        </ul></div>
    </div>
  </div>
</section>

{sekcja_faq(FAQ_POZIOMY)}

<section class="canvas glow-r pad-norm"><div class="grid"><div class="c1-6">
  <p class="mono"><span>Następny krok</span></p>
  <h2 class="h-sec" style="margin-top:20px">Najpierw przyjedź. <br><span class="acc">Potem zdecydujesz.</span></h2>
  <p class="lead" style="margin-top:24px">Pokażemy studio, ustawimy Cię przed kamerą i nagramy próbne 5 minut.
    Na tej rozmowie ustalamy poziom i dostajesz konkretną wycenę, a nie przedział.</p>
  <a href="{base}kontakt/" class="pill" style="margin-top:32px">Umów rozmowę</a>
</div></div></section>'''

    tytul = 'Prowadzenie kanału YouTube dla firm - 3 poziomy'
    opis = ('Prowadzenie kanału wideo dla firm w Warszawie na trzech poziomach: pojedyncze odcinki, '
            'seria, cały kanał. Jeden dzień zdjęciowy, reszta produkcji po naszej stronie.')
    schema = [LD_FIRMA,
              {"@context": "https://schema.org", "@type": "Service",
               "name": "Prowadzenie kanału wideo dla firm",
               "serviceType": "Produkcja i prowadzenie kanału wideo",
               "provider": {"@type": "LocalBusiness", "name": MARKA},
               "areaServed": "Warszawa", "description": opis,
               "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Poziomy współpracy",
                   "itemListElement": [
                       {"@type": "Offer", "name": f"Poziom {p['rz']} - {p['nazwa']}",
                        "description": p['dla'],
                        "itemOffered": {"@type": "Service", "name": p['nazwa']}}
                       for p in POZIOMY]}},
              ld_okruszki([(url, 'Prowadzenie kanału')]),
              ld_faq(FAQ_POZIOMY),
              {"@context": "https://schema.org", "@type": "ItemList",
               "name": "Odcinki podcastu GSA", "itemListElement": [
                   {"@type": "ListItem", "position": i + 1,
                    "item": {"@type": "VideoObject", "name": t,
                             "description": f"Odcinek podcastu GSA z udziałem, gość: {g}.",
                             "thumbnailUrl": f"{DOMENA}/assets/kadry/{k}.webp",
                             "embedUrl": f"https://www.youtube.com/embed/{v}"}}
                   for i, (v, t, g, k) in enumerate(DOWODY)]}]
    return strona(tytul + f' | {MARKA}', opis, tresc, base, url, schema, aktywny=url)

# ─────────────────────────────────────────────────────────────
# 6. AUDYT
# ─────────────────────────────────────────────────────────────
KWOTY = re.compile(r'\d[\d\s.,]*\s*(?:z[łl]|PLN)\b|\bnetto\b|\bbrutto\b', re.I)
PAUZY = re.compile(r'—|–')
def audyt(pliki):
    """Kwoty wolno podawac tylko w artykulach - tam sa faktem o rynku, a nie nasza cena.
    Na stronach ofertowych zadnych kwot: wycena idzie przez rozmowe."""
    bledy = []
    for p in pliki:
        t = open(p, encoding='utf-8').read()
        wzgledna = os.path.relpath(p, ROOT)
        artykul = wzgledna.startswith('blog' + os.sep) and wzgledna != os.path.join('blog', 'index.html')
        if not artykul:
            for m in KWOTY.finditer(t):
                kontekst = t[max(0, m.start()-45):m.end()+45].replace('\n', ' ')
                bledy.append(f'{wzgledna}: kwota „{m.group(0).strip()}" poza artykulem w: ...{kontekst}...')
        for m in PAUZY.finditer(t):
            kontekst = t[max(0, m.start()-45):m.end()+45].replace('\n', ' ')
            bledy.append(f'{wzgledna}: dluga pauza w: ...{kontekst}...')
        if t.count('<h1') > 1:
            bledy.append(f'{wzgledna}: wiecej niz jeden H1')
        if '<title>' in t and len(re.search(r'<title>(.*?)</title>', t, re.S).group(1)) > 62:
            bledy.append(f'{wzgledna}: title ma {len(re.search(chr(60)+chr(116)+"itle>(.*?)</title>", t, re.S).group(1))} znakow, limit 62')
        if 'name="description"' not in t:
            bledy.append(f'{wzgledna}: brak meta description')
    return bledy


# ─────────────────────────────────────────────────────────────
# 6b. KONTRAST - progi WCAG 2.1 AA, sprawdzane przy kazdym buildzie
# ─────────────────────────────────────────────────────────────
def _lin(k):
    k /= 255
    return k / 12.92 if k <= 0.04045 else ((k + 0.055) / 1.055) ** 2.4


def _lum(hx):
    hx = hx.lstrip('#')
    r, g, b = (int(hx[i:i + 2], 16) for i in (0, 2, 4))
    return .2126 * _lin(r) + .7152 * _lin(g) + .0722 * _lin(b)


def kontrast(a, b):
    la, lb = _lum(a), _lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + .05) / (lo + .05)


def _zmieszaj(fg, alfa, tlo):
    f = [int(fg.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)]
    t = [int(tlo.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)]
    return '#%02x%02x%02x' % tuple(round(f[i] * alfa + t[i] * (1 - alfa)) for i in range(3))


def audyt_kontrastu(css):
    """Tokeny czytamy z wygenerowanego CSS, zeby audyt pilnowal realnego stanu.
    Prog 4.5 dla tekstu, 3.0 dla znakow niosacych tresc, 2.2 dla kreski druku
    (kreska jest separatorem dekoracyjnym, ale ma byc widoczna jak nadruk)."""
    tok = dict(re.findall(r'--([a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})', css))
    brak = [k for k in ('tlo', 'tlo-2', 'tekst', 'tekst-2', 'linia', 'znak',
                        'na-ciemnym', 'na-ciemnym-2', 'znak-jasny', 'linia-ciemna') if k not in tok]
    if brak:
        return [f'kontrast: brak tokenow w CSS: {", ".join(brak)}']

    tlo, tlo2, ciemne = tok['tlo'], tok['tlo-2'], tok['tekst']
    pary = [
        ('tekst na tle', tok['tekst'], tlo, 4.5),
        ('tekst drugorzedny na tle', tok['tekst-2'], tlo, 4.5),
        ('znak na tle', tok['znak'], tlo, 4.5),
        ('znak na drugim tonie tla', tok['znak'], tlo2, 4.5),
        ('linia na tle', tok['linia'], tlo, 2.2),
        ('tekst na pasmie ciemnym', tok['na-ciemnym'], ciemne, 4.5),
        ('tekst drugorzedny na pasmie ciemnym', tok['na-ciemnym-2'], ciemne, 4.5),
        ('znak jasny na pasmie ciemnym', tok['znak-jasny'], ciemne, 4.5),
        ('linia na pasmie ciemnym', tok['linia-ciemna'], ciemne, 2.2),
    ]
    bledy = []
    for opis, fg, tlo, prog in pary:
        k = kontrast(fg, tlo)
        if k < prog:
            bledy.append(f'kontrast: {opis} = {k:.2f}:1, wymagane {prog}:1 ({fg} na {tlo})')
    return bledy

# ─────────────────────────────────────────────────────────────
# 7. MAIN
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    CSS, SYMBOLE, JS = wyciagnij_system()
    os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
    open(os.path.join(ROOT, 'assets', 'site.css'), 'w', encoding='utf-8').write(
        "@import url('fonts.css');\n" + CSS + CSS_PROZA)
    open(os.path.join(ROOT, 'assets', 'site.js'), 'w', encoding='utf-8').write(JS)

    # artykuly
    arts = {}
    if os.path.isdir(BLOG_DIR):
        for fn in sorted(os.listdir(BLOG_DIR)):
            if not fn.endswith('.md'): continue
            dane, body = parsuj_front(open(os.path.join(BLOG_DIR, fn), encoding='utf-8').read())
            if not dane.get('slug'):
                print('  ! brak slug w', fn); continue
            dane['body'] = body
            arts[dane['slug']] = dane

    zrobione = []
    for s in STRONY:
        zapisz(s['url'], render_usluga(s)); zrobione.append(s['url'])
    for s in STRONY_PROSTE:
        zapisz(s['url'], render_prosta(s)); zrobione.append(s['url'])
    zapisz('/prowadzenie-kanalu/', render_poziomy()); zrobione.append('/prowadzenie-kanalu/')
    zapisz('/kontakt/', render_kontakt()); zrobione.append('/kontakt/')
    zapisz('/blog/', render_blog(arts)); zrobione.append('/blog/')
    for slug, a in arts.items():
        zapisz('/blog/' + slug + '/', render_artykul(a, arts)); zrobione.append('/blog/' + slug + '/')

    # sitemap
    urls = ['/'] + zrobione
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        pri = '1.0' if u == '/' else ('0.9' if u.count('/') == 2 else '0.7')
        sm += f'  <url><loc>{DOMENA}{u}</loc><lastmod>{DZIS}</lastmod><priority>{pri}</priority></url>\n'
    sm += '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
    open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8').write(
        ('User-agent: *\nDisallow: /\n' if PODGLAD else
         f'User-agent: *\nAllow: /\n\nSitemap: {DOMENA}/sitemap.xml\n'))

    # llms.txt - pod silniki generatywne
    lista = '\n'.join(f'- [{a["tytul"]}]({DOMENA}/blog/{s}/): {a.get("opis","")}' for s, a in arts.items())
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write(f'''# {MARKA}

> Studio wideopodcastowe w Warszawie. Pełna produkcja end-to-end: nagranie, montaż, rolki pionowe, opisy, transkrypcje i publikacja.

Zakres usług: wideopodcasty, krótkie formy pionowe (rolki, shorty, talking head), nagrania szkoleniowe i kursy online.
Nie realizujemy: webinarów i transmisji na żywo, sesji zdjęciowych.

Model pracy: jeden dzień zdjęciowy daje materiał na cały miesiąc. Nagrywanie blokowe, rejestracja ISO (osobna ścieżka na każdą kamerę i mikrofon).
Poziomy współpracy: trzy. Poziom I - pojedyncze odcinki. Poziom II - seria ze stałym terminem zjazdów i spójną oprawą. Poziom III - prowadzenie całego kanału razem z publikacją, archiwum i raportem wydań. Pełne porównanie zakresu: {DOMENA}/prowadzenie-kanalu/
Podział odpowiedzialności: tematy, dobór gości i merytoryka zostają po stronie klienta na każdym poziomie. Pomagamy ułożyć z tej wiedzy format, kolejność odcinków i plan zjazdów, ale nie tworzymy merytoryki za klienta. Studio odpowiada za plan, sprzęt, realizację, montaż, krótkie formy pionowe, miniatury, transkrypcje i publikację techniczną.
Czego nie robimy: nie wymyślamy tematów za klienta, nie występujemy przed kamerą zamiast niego i nie obiecujemy zasięgu.
Ceny: nie publikujemy cennika. Wycena powstaje po rozmowie i zależy od poziomu oraz liczby odcinków w miesiącu.

## Podstrony
- [Produkcja podcastów]({DOMENA}/produkcja-podcastow-warszawa/)
- [Rolki, shorty, talking head]({DOMENA}/rolki-shorty-talking-head/)
- [Nagrania szkoleniowe i kursy online]({DOMENA}/nagrania-szkoleniowe-kursy-online/)
- [Prowadzenie kanału, trzy poziomy]({DOMENA}/prowadzenie-kanalu/)
- [Jak pracujemy]({DOMENA}/jak-pracujemy/)
- [Sprzęt]({DOMENA}/sprzet/)
- [O nas]({DOMENA}/o-nas/)
- [Kontakt]({DOMENA}/kontakt/)

## Blog
{lista}
''')

    print(f'Zbudowano: {len(zrobione)} podstron, w tym {len(arts)} artykułów')
    pliki = [os.path.join(ROOT, 'index.html')] + [os.path.join(ROOT, u.strip('/'), 'index.html') for u in zrobione]
    b = audyt([p for p in pliki if os.path.exists(p)])
    b += audyt_kontrastu(CSS)
    if b:
        print(f'\nAUDYT - {len(b)} problemów:')
        for x in b[:40]: print('  •', x)
        sys.exit(1)
    print('Audyt czysty: kwoty tylko w artykułach, zero długich pauz, jeden H1,\n'
          '              title i description na miejscu, kontrast WCAG AA na wszystkich parach')
