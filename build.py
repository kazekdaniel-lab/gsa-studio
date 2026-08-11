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
DOMENA = 'https://kazekdaniel-lab.github.io/gsa-studio'   # podglad; przy wdrozeniu podmien na domene docelowa
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
/* ══════════ PROZA I PODSTRONY ══════════ */
.proza{max-width:70ch}
.proza h2{font-size:clamp(26px,2.6vw,38px);font-weight:700;letter-spacing:-.025em;line-height:1.1;margin:56px 0 18px}
.proza>h2:first-child{margin-top:0}
.proza h3{font-size:clamp(20px,1.6vw,23px);font-weight:600;letter-spacing:-.015em;margin:36px 0 12px}
.proza p{margin-bottom:18px;font-size:17px;line-height:1.62}
.proza ul,.proza ol{margin:0 0 22px 0;padding-left:0;list-style:none;display:grid;gap:11px}
/* WAZNE: tresc <li> jest zawsze owinieta w <span>, zeby siatka miala dokladnie 2 elementy.
   Bez tego tekst po pogrubieniu wpada do waskiej kolumny i lamie sie po jednym slowie. */
.proza ul li{display:grid;grid-template-columns:14px minmax(0,1fr);gap:12px;align-items:start}
.proza ul li::before{content:'';width:9px;height:9px;margin-top:.5em;background:var(--accent);
  clip-path:polygon(50% 0,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0 50%,40% 40%)}
.proza ol{counter-reset:k}
.proza ol li{display:grid;grid-template-columns:32px minmax(0,1fr);gap:12px;counter-increment:k;align-items:start}
.proza ol li::before{content:counter(k,decimal-leading-zero);font-family:var(--ff-mono);font-size:12px;
  font-weight:500;letter-spacing:.14em;color:var(--accent);padding-top:.35em}
.proza li>span{display:block;line-height:1.6}
.proza table{width:100%;border-collapse:collapse;margin:28px 0;font-size:15.5px}
.proza th{text-align:left;font-family:var(--ff-mono);font-weight:500;font-size:11.5px;letter-spacing:.16em;
  text-transform:uppercase;color:rgba(26,20,16,.55);padding:0 16px 12px 0;border-bottom:1px solid var(--hairline-cream)}
.proza td{padding:14px 16px 14px 0;border-bottom:1px solid var(--hairline-cream);vertical-align:top}
.proza tr:nth-child(even) td{background:var(--surface-cream)}
.proza strong{font-weight:700}
.proza a{color:var(--accent);border-bottom:1px solid rgba(255,89,0,.35)}
.proza a:hover{border-bottom-color:var(--accent)}
.proza blockquote{border-left:2px solid var(--accent);padding-left:22px;margin:28px 0;font-size:19px;line-height:1.5}

.odp{font-size:clamp(19px,1.55vw,23px);line-height:1.45;font-weight:400;max-width:64ch;
  border-left:2px solid var(--accent);padding-left:26px;margin:34px 0 44px}
.spis{margin:0 0 56px;padding:0;list-style:none;display:grid;gap:9px;max-width:60ch}
.spis a{font-family:var(--ff-mono);font-size:12.5px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;
  color:rgba(26,20,16,.62);display:grid;grid-template-columns:34px 1fr;gap:10px}
.spis a:hover{color:var(--accent)}
.spis .n{color:var(--accent)}

.kruszywo{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:26px}
.karty{display:grid;grid-template-columns:repeat(2,1fr);gap:var(--gut) calc(var(--gut)*2)}
@media(max-width:767px){.karty{grid-template-columns:1fr}}
.karta{border-top:1px solid var(--hairline-cream);padding-top:22px;transition:transform .16s var(--ease)}
.karta:hover{transform:translateX(8px)}
.karta:hover .karta-t{color:var(--accent)}
.dark .karta,.canvas .karta{border-color:var(--hairline)}
.karta p{font-size:15.5px;line-height:1.5;color:rgba(26,20,16,.62)}
.karta .karta-t{font-size:21px;font-weight:600;letter-spacing:-.015em;line-height:1.22;margin:10px 0 8px;
  color:var(--ink-dark);transition:color .16s var(--ease)}
.dark .karta .karta-t,.canvas .karta .karta-t{color:var(--ink)}
.dark .karta p,.canvas .karta p{color:var(--ink-muted)}
.filtry{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 52px}
.filtr{font-family:var(--ff-mono);font-size:11.5px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;
  border:1px solid var(--hairline-cream);border-radius:999px;padding:9px 16px;color:rgba(26,20,16,.62);cursor:pointer;
  background:transparent;transition:.16s var(--ease)}
.filtr:hover{border-color:var(--accent);color:var(--accent)}
.filtr[aria-pressed="true"]{border-color:var(--accent);color:var(--ink-dark);
  box-shadow:inset 0 0 0 1px var(--accent)}
.dalej{border-top:1px solid var(--hairline-cream);margin-top:64px;padding-top:34px}
.autor{display:flex;gap:14px;align-items:center;margin-top:44px;padding-top:26px;border-top:1px solid var(--hairline-cream)}
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
        ('/zakres-wspolpracy/', 'Zakres'), ('/studio/', 'Studio'),
        ('/blog/', 'Blog'), ('/kontakt/', 'Kontakt')]

def naglowek(base, aktywny=''):
    poz = ''.join(f'<a href="{base.rstrip("/")}{u}"{" style=\"color:var(--accent)\"" if u==aktywny else ""}>{n}</a>'
                  for u, n in MENU)
    return f'''<header><div class="grid"><div class="hd">
  <div style="display:flex;align-items:center;min-width:0">
    <a href="{base}" class="brand"><i class="star"></i>GSA STUDIO</a></div>
  <nav class="mono" aria-label="Nawigacja">{poz}</nav>
  <a href="{base.rstrip("/")}/kontakt/" class="pill">Umów wizytę</a>
</div></div></header>'''

def stopka(base):
    b = base.rstrip('/')
    linki = ''.join(f'<a href="{b}{u}">{n}</a>' for u, n in MENU)
    return f'''<footer class="pad-tight"><div class="grid">
  <div class="foot">
    <div><a href="{base}" class="brand" style="margin-bottom:16px"><i class="star"></i>GSA STUDIO</a>
      <p class="marg" style="max-width:34ch">Studio wideopodcastowe w Warszawie. Nagranie, montaż i publikacja w jednym miejscu.</p></div>
    <div class="mono" style="flex-direction:column;align-items:flex-start;gap:12px">
      <span>Warszawa</span><span class="slot">[ULICA I NUMER]</span></div>
    <div class="mono" style="flex-direction:column;align-items:flex-start;gap:12px">
      <span class="slot">[TELEFON]</span><span class="slot">[E-MAIL]</span></div>
    <div class="mono" style="flex-direction:column;align-items:flex-start;gap:12px">{linki}</div>
  </div>
  <div class="foot-bot mono"><span>© 2026 GSA Studio</span>
    <span style="display:flex;gap:22px"><a href="{b}/polityka-prywatnosci/">Polityka prywatności</a><a href="{b}/regulamin/">Regulamin</a></span></div>
</div></footer>'''

def strona(tytul, opis, tresc, base='../', kanon='/', schema=None, aktywny=''):
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
<meta name="robots" content="noindex,nofollow">
<link rel="canonical" href="{DOMENA}{kanon}">
<meta property="og:title" content="{html.escape(tytul)}">
<meta property="og:description" content="{html.escape(opis)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{base}assets/site.css">
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
 dict(url='/produkcja-podcastow-warszawa/', tytul='Produkcja podcastów Warszawa - nagranie, montaż, publikacja',
   opis='Pełna produkcja wideopodcastów w Warszawie. Nagranie, montaż, rolki pionowe, opisy i publikacja. Jeden dzień na planie, materiał na miesiąc.',
   h1='Produkcja podcastów<br>od formatu po publikację', eyebrow='Usługa główna',
   odp='Pełna produkcja oznacza, że po Twojej stronie zostaje jeden dzień zdjęciowy i akceptacja materiału. Format, przygotowanie gości, nagranie, montaż, krótkie formy pionowe, opisy, transkrypcje i publikacja są po naszej. Wychodzisz z kompletem plików gotowych do wrzucenia, a nie z surówką.',
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

Nagrywamy blokiem, więc jeden dzień w studiu daje materiał na kilka tygodni publikacji. Zamiast czterech osobnych wizyt blokujesz jeden dzień.

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

Nie mamy jednego zestawu dla wszystkich. Są trzy poziomy zaangażowania: pojedyncze odcinki, serie i prowadzenie całego kanału. Różnią się tym, ile pracy zostaje po Twojej stronie. Opisaliśmy je na stronie [zakresu współpracy](/zakres-wspolpracy/).
''',
   faq=[('Kto wymyśla tematy i dobiera gości?','Ty. Merytoryka, tematy i kontakty do gości zostają po Twojej stronie na każdym poziomie współpracy, bo to Twoja wiedza i Twoja sieć. My odpowiadamy za to, jak rozmowa wygląda i brzmi, i za wszystko, co dzieje się z materiałem po nagraniu.'),
        ('Ile odcinków można nagrać jednego dnia?','Zależy od formatu i od tego, ile osób jest na planie. Nagrywamy blokowo, bo każdy kolejny odcinek tego samego dnia idzie szybciej niż pierwszy. Liczbę ustalamy przy planowaniu zjazdu.'),
        ('Kto pisze opisy i publikuje odcinki?','Zależy od poziomu zakresu. Przy serii i przy prowadzeniu kanału opisy, tagi, miniatury i publikacja są po naszej stronie. Konta pozostają Twoje, my mamy dostęp roboczy.'),
        ('Do kogo należą materiały?','Do Ciebie. Wszystkie prawa do nagrania i materiałów końcowych przechodzą na Ciebie po rozliczeniu. Fragment w portfolio pokazujemy wyłącznie za Twoją zgodą.'),
        ('Czy nagrywacie poza studiem?','Podstawowym miejscem jest nasze studio, bo tam mamy kontrolę nad akustyką i światłem. Nagrania w Twojej siedzibie ustalamy indywidualnie.')]),

 dict(url='/rolki-shorty-talking-head/', tytul='Rolki, shorty i talking head - produkcja krótkich form',
   opis='Krótkie formy pionowe dla firm: rolki wycinane z odcinka i talking head kręcony osobno. 1080×1920, napisy wypalane, gotowe do publikacji.',
   h1='Krótkie formy pionowe,<br>które działają same', eyebrow='Usługa',
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

 dict(url='/nagrania-szkoleniowe-kursy-online/', tytul='Nagrania szkoleniowe i kursy online - produkcja w Warszawie',
   opis='Produkcja materiałów e-learningowych i kursów online w Warszawie. Podział na moduły, prompter, napisy, pliki gotowe pod platformy szkoleniowe.',
   h1='Kursy online<br>i materiały szkoleniowe', eyebrow='Usługa',
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

 dict(url='/zakres-wspolpracy/', tytul='Zakres współpracy - pojedyncze odcinki, serie, cały kanał',
   opis='Trzy poziomy współpracy ze studiem: pojedyncze odcinki, serie z ustalonym formatem i prowadzenie całego kanału. Zakres ustalamy na rozmowie.',
   h1='Jeden odcinek, seria<br>albo cały kanał', eyebrow='Zakres',
   odp='Nie ma jednego zestawu dla wszystkich. Jest pytanie, jak daleko chcesz to zaprowadzić, i od tego zależy, ile pracy zostaje po Twojej stronie. Trzy poziomy różnią się nie liczbą godzin, tylko tym, jak dużą część produkcji i publikacji bierzemy na siebie. Merytoryka, czyli tematy, goście i to, o czym mówisz, zostaje po Twojej stronie na każdym poziomie.',
   body='''
## Poziom I - pojedyncze odcinki

Jeden temat, jedno nagranie, komplet materiału. Wchodzisz z gotowym pomysłem albo ustalamy go w trakcie jednej rozmowy. Dobre, kiedy chcesz sprawdzić, jak wyglądasz na ekranie i czy w ogóle chcesz to robić dalej.

**Po Twojej stronie:** temat i gość, jeden dzień w studiu, akceptacja materiału.
**Po naszej stronie:** ustawienie planu, nagranie, montaż, rolki, pliki gotowe do publikacji.

## Poziom II - serie

Cykl z zaplanowanym formatem i stałym terminem w kalendarzu. Nagrywamy blokowo, więc jeden dzień daje materiał na kilka tygodni publikacji. Tu zaczyna się praca nad tym, żeby odcinki wyglądały jak jedna całość, a nie jak zbiór nagrań.

**Po Twojej stronie:** tematy i goście, zjazd raz na ustalony okres, akceptacja.
**Po naszej stronie:** spójna oprawa wizualna serii, harmonogram zjazdów, produkcja wszystkich odcinków, komplet krótkich form, transkrypcje i miniatury, pliki opisane i gotowe do wrzucenia.

## Poziom III - cały kanał

Prowadzimy produkcję kanału jako całość. Ty przynosisz tematy i gości, my odpowiadamy za wszystko, co dzieje się ze sprzętem, materiałem i plikami, łącznie z wrzuceniem odcinka na platformy.

**Po Twojej stronie:** tematy, goście, merytoryka i decyzje kierunkowe.
**Po naszej stronie:** regularne zjazdy w kalendarzu, produkcja wszystkich odcinków, krótkie formy pod każdą platformę, miniatury i transkrypcje, publikacja na platformach, archiwum materiałów, raport z tego, co i kiedy wyszło.

## Jak wybrać poziom

| Sytuacja | Poziom |
|---|---|
| Nie wiem, czy chcę to robić dalej | I |
| Mam temat i osobę, chcę regularności | II |
| Chcę, żeby kanał rósł, i nie mam na to zespołu | III |
| Mam już podcast, ale zjada za dużo czasu | II albo III |

Porównanie trybów rozpisaliśmy szerzej w tekście [seria czy pojedyncze odcinki](/blog/seria-czy-pojedyncze-odcinki/).

## Co decyduje o zakresie

Trzy rzeczy: ile odcinków realnie chcesz wypuszczać, co już masz po swojej stronie i jak dużo kontroli chcesz zachować. Zakres ustalamy na rozmowie, bo bez tych trzech odpowiedzi każda propozycja jest zgadywaniem.
''',
   faq=[('Czy mogę zmienić poziom w trakcie?','Tak. Najczęściej ktoś zaczyna od pojedynczego odcinka, a po dwóch albo trzech przechodzi na serię, bo widzi, ile pracy poza nagraniem to wymaga.'),
        ('Czy przy poziomie I też dostaję rolki?','Tak. Komplet materiału z jednego nagrania obejmuje odcinek, krótkie formy i pliki gotowe do publikacji.'),
        ('Na jak długo się wiążę?','Bez umów lojalnościowych. Warunki wypowiedzenia ustalamy na starcie i są symetryczne.')]),

 dict(url='/jak-pracujemy/', tytul='Jak pracujemy - 5 etapów produkcji podcastu',
   opis='Proces produkcji podcastu w 5 etapach: format, przygotowanie, dzień zdjęciowy, postprodukcja, publikacja. Co jest po Twojej stronie, a co po naszej.',
   h1='Pięć etapów,<br>z których trzy dzieją się bez Ciebie', eyebrow='Proces',
   odp='Produkcja dzieli się na 5 etapów. Twoja obecność jest wymagana w dwóch: przy ustaleniu formatu i w dniu zdjęciowym. Przygotowanie, postprodukcja i publikacja idą po naszej stronie, a Ty dostajesz je do akceptacji.',
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

 dict(url='/sprzet/', tytul='Sprzęt studia - kamery, dźwięk, światło, formaty wyjściowe',
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

 dict(url='/o-nas/', tytul='O nas - studio prowadzone przez praktyków podcastu',
   opis='Prowadzimy własny podcast Growth, Scale & Automate. Znamy tę robotę od strony osoby, która wchodzi do studia z tematem i patrzy potem na statystyki.',
   h1='Robimy to<br>najpierw u siebie', eyebrow='Kto to robi',
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
 dict(url='/studio/', tytul='Studio wideopodcastowe Warszawa - przestrzeń i aranżacje',
   opis='Studio wideopodcastowe w Warszawie: wygłuszona sala, 3 aranżacje planu, światło ustawiane pod markę, zaplecze i dojazd.',
   h1='Miejsce, w którym<br>nic Cię nie rozprasza', eyebrow='Studio',
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

 dict(url='/realizacje/', tytul='Realizacje - odcinki nagrane w naszym studiu',
   opis='Odcinki, rolki i materiały szkoleniowe nagrane w naszym studiu w Warszawie. Zobacz efekt, zanim zadzwonisz.',
   h1='Najpierw kadry,<br>potem obietnice', eyebrow='Realizacje',
   odp='Na tej stronie zbieramy materiały, które wyszły z naszego studia. Każda pozycja to gotowy odcinek albo zestaw krótkich form, a nie wizualizacja. Katalog uzupełniamy po każdej publikacji, więc rośnie razem z kanałami, które prowadzimy.',
   body='''
## Co tu znajdziesz

Odcinki wideopodcastów, krótkie formy pionowe i materiały szkoleniowe. Przy każdej realizacji podajemy format, liczbę kamer i to, co dokładnie było po naszej stronie.

## Katalog

Katalog realizacji uzupełniamy materiałem po każdej publikacji. Jeśli chcesz zobaczyć konkretny format albo branżę, napisz - pokażemy materiał, którego nie ma jeszcze publicznie.

## Dlaczego to jest najważniejsza strona serwisu

Bo na większości stron studiów w Warszawie nie da się obejrzeć ani jednego odcinka nagranego w tym studiu. Deklaracja o jakości nic nie znaczy, dopóki nie widać efektu.
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
    <a href="{base}kontakt/" class="pill">Umów wizytę</a>
  </div></div>
</section>
<section class="light pad-norm"><div class="grid"><div class="c2-7 proza">{md2html(s['body'])}</div></div></section>
{sekcja_faq(faq)}
<section class="canvas glow-r pad-norm"><div class="grid"><div class="c1-6">
  <h2 class="h-sec">Zacznijmy od rozmowy</h2>
  <p class="lead" style="margin-top:22px">Pokażemy studio, ustawimy Cię przed kamerą i nagramy próbne 5 minut.</p>
  <a href="{base}kontakt/" class="pill" style="margin-top:32px">Umów wizytę</a>
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
      <p class="mono"><span>Czytaj dalej</span></p>
      {powiazane}
    </div>
  </div>
</div></section>
{sekcja_faq(faq)}
<section class="canvas glow-r pad-norm"><div class="grid"><div class="c1-6">
  <h2 class="h-sec">Chcesz to zrobić u siebie?</h2>
  <p class="lead" style="margin-top:22px">Pokażemy studio i ustalimy format, zanim cokolwiek zablokujemy w kalendarzu.</p>
  <a href="{base}kontakt/" class="pill" style="margin-top:32px">Umów wizytę</a>
</div></div></section>'''
    schema = [{"@context":"https://schema.org","@type":"Article","headline":a['tytul'],
               "description":a.get('opis',''),"inLanguage":"pl-PL",
               "author":{"@type":"Organization","name":MARKA},
               "publisher":{"@type":"Organization","name":MARKA},
               "mainEntityOfPage":DOMENA+'/blog/'+a['slug']+'/'},
              ld_okruszki([('/blog/','Blog'), ('/blog/'+a['slug']+'/', a['tytul'])])]
    if faq:
        schema.append(ld_faq(faq))
    return strona(a['tytul'] + f' | {MARKA}', a.get('opis',''), tresc, base, '/blog/'+a['slug']+'/', schema)

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
    <h1 class="h-sec" style="margin-top:20px">Najpierw przyjedź.<br><span class="acc">Potem zdecydujesz.</span></h1>
    <p class="lead" style="margin-top:26px">Pokażemy studio, ustawimy Cię przed kamerą i nagramy próbne 5 minut. Napisz, co chcesz nagrywać i dla kogo.</p>
    <div class="brace" style="margin-top:52px;padding-block:24px;max-width:520px"><div class="kontakt-blok">
      <div class="kv"><span class="mono"><span>Adres</span></span><span class="slot">[ULICA I NUMER, WARSZAWA]</span></div>
      <div class="kv"><span class="mono"><span>Telefon</span></span><span class="slot">[NUMER]</span></div>
      <div class="kv"><span class="mono"><span>E-mail</span></span><span class="slot">[ADRES E-MAIL]</span></div>
    </div></div>
  </div>
  <div class="c9-12" style="grid-column:8/13"><form class="sheet" id="zgloszenie" novalidate>
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
# 6. AUDYT
# ─────────────────────────────────────────────────────────────
ZAKAZANE = re.compile(r'\bz[łl]\b|\bPLN\b|netto|brutto|cennik|abonament|\bpakiet\w*|kosztuje\s+\d+\s*(z[łl]|PLN)|—|–', re.I)
def audyt(pliki):
    bledy = []
    for p in pliki:
        t = open(p, encoding='utf-8').read()
        for m in ZAKAZANE.finditer(t):
            kontekst = t[max(0, m.start()-45):m.end()+45].replace('\n', ' ')
            bledy.append(f'{os.path.relpath(p, ROOT)}: „{m.group(0)}" w: ...{kontekst}...')
        if t.count('<h1') > 1:
            bledy.append(f'{os.path.relpath(p, ROOT)}: wiecej niz jeden H1')
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
        f'User-agent: *\nAllow: /\n\nSitemap: {DOMENA}/sitemap.xml\n')

    # llms.txt - pod silniki generatywne
    lista = '\n'.join(f'- [{a["tytul"]}]({DOMENA}/blog/{s}/): {a.get("opis","")}' for s, a in arts.items())
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write(f'''# {MARKA}

> Studio wideopodcastowe w Warszawie. Pełna produkcja end-to-end: nagranie, montaż, rolki pionowe, opisy, transkrypcje i publikacja.

Zakres usług: wideopodcasty, krótkie formy pionowe (rolki, shorty, talking head), nagrania szkoleniowe i kursy online.
Nie realizujemy: webinarów i transmisji na żywo, sesji zdjęciowych.

Model pracy: jeden dzień zdjęciowy daje materiał na kilka tygodni publikacji. Nagrywanie blokowe, rejestracja ISO (osobna ścieżka na każdą kamerę i mikrofon).
Poziomy współpracy: pojedyncze odcinki, serie, prowadzenie produkcji całego kanału. Zakres ustalany na rozmowie.
Podział odpowiedzialności: merytoryka, tematy i dobór gości zostają po stronie klienta na każdym poziomie. Studio odpowiada za plan, sprzęt, realizację, montaż, krótkie formy, miniatury, transkrypcje i publikację techniczną. Nie prowadzimy strategii treści ani nie piszemy konspektów merytorycznych.

## Podstrony
- [Produkcja podcastów]({DOMENA}/produkcja-podcastow-warszawa/)
- [Rolki, shorty, talking head]({DOMENA}/rolki-shorty-talking-head/)
- [Nagrania szkoleniowe i kursy online]({DOMENA}/nagrania-szkoleniowe-kursy-online/)
- [Zakres współpracy]({DOMENA}/zakres-wspolpracy/)
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
    if b:
        print(f'\nAUDYT - {len(b)} problemów:')
        for x in b[:40]: print('  •', x)
        sys.exit(1)
    print('Audyt czysty: zero cen, zero długich pauz, jeden H1 na stronę')
