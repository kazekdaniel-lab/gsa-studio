# GSA Studio - strona studia wideopodcastowego

Serwis studia wideopodcastowego w Warszawie. Pełna produkcja: nagranie, montaż, krótkie formy pionowe, opisy, transkrypcje i publikacja. Współpraca na trzech poziomach, od pojedynczego odcinka po prowadzenie całego kanału.

**Podgląd:** https://kazekdaniel-lab.github.io/gsa-studio/

## Co jest w repo

| Ścieżka | Zawartość |
|---|---|
| `index.html` | strona główna, zarazem źródło systemu wizualnego (CSS i JS) |
| `build.py` | generator statyczny: podstrony, blog, sitemap, robots, llms.txt |
| `tresc/blog/*.md` | 30 artykułów w markdownie z front-matterem |
| `assets/` | CSS, JS, fonty i kadry lokalnie |
| `docs/` | decyzje, badanie konkurencji, oś treści, plan SEO/AEO/GEO, baza FAQ |

Najważniejszy dokument: [docs/DECYZJE-2026-09.md](docs/DECYZJE-2026-09.md). Jest nadrzędny wobec sierpniowych plików.

## Budowanie

```bash
python3 build.py
```

Generator wyciąga system wizualny prosto z `index.html`, więc istnieje jedno źródło stylu. Nowy komponent dodaje się do bloku `<style>` w `index.html`, a nie do `build.py`.

System wizualny: **plan zdjęciowy**. Tło `#FBFBF9`, tekst i ciemne pasma `#15161A`, jeden kolor `#0F3D32` (na ciemnym `#79D0B2`). Motyw przewodni to pasek 30 dni, w którym pełny jest tylko jeden kafel: dzień zdjęciowy. Zero zaokrągleń, zero cieni, strukturę niesie linia 1 px. Krój: General Sans (Fontshare, ITF Free Font License), nagłówki w grubości 500, tekst 400. JetBrains Mono zostaje wyłącznie na nazwy plików i sloty z danymi do uzupełnienia.

Oś treści: **jeden dzień zdjęciowy zamyka miesiąc materiału**. Publikacja nie jest główną wartością, bo przy pojedynczym odcinku i przy serii wrzuca klient. Własny kanał GSA (72 odcinki) stoi na stronie jako dowód kompetencji, nie jako główny argument. Pełne uzasadnienie w [docs/COPY-HERO-2026-10.md](docs/COPY-HERO-2026-10.md) i [docs/USP-2026-10.md](docs/USP-2026-10.md).

Na końcu rusza audyt, który przerywa build, gdy znajdzie: kwotę poza artykułem, długą pauzę, więcej niż jeden H1, tytuł dłuższy niż 62 znaki, brak meta description albo parę kolorów poniżej progu WCAG AA.

## Strona flagowa

`/prowadzenie-kanalu/` to autorski układ, nie szablon podstrony. Trzy poziomy współpracy, blok granicy zakresu, matryca porównawcza, kadry z własnego kanału, podział „dla kogo i dla kogo nie". Renderuje ją `render_poziomy()` w `build.py`.

## Przed wdrożeniem

W `build.py`, na górze pliku:

1. `DOMENA` - adres docelowy
2. `PODGLAD = False` - inaczej cały serwis zostaje z `noindex` i nie wejdzie do indeksu

## Skala

43 podstrony, 30 artykułów, około 53 700 słów. Schema: `LocalBusiness`, `Service` z `OfferCatalog`, `Article`, `FAQPage`, `VideoObject`, `BreadcrumbList`.

## Status

Prototyp. Miejsca w nawiasach kwadratowych czekają na dane: adres, telefon, metraż, modele sprzętu. Brakuje zdjęć studia w Warszawie - te kadry są na razie opisanymi ramkami z przerywaną kreską. Materiał wideo jest realny: 6 odcinków podcastu GSA w `assets/kadry/`.
