# GSA Studio - strona studia wideopodcastowego

Prototyp serwisu studia wideopodcastowego w Warszawie. Pełna produkcja end-to-end: nagranie, montaż, krótkie formy pionowe, opisy, transkrypcje i publikacja.

**Podgląd:** https://kazekdaniel-lab.github.io/gsa-studio/

## Co jest w repo

| Ścieżka | Zawartość |
|---|---|
| `index.html` | strona główna, zarazem źródło systemu wizualnego |
| `build.py` | generator statyczny: renderuje podstrony, blog, sitemap, robots i llms.txt |
| `tresc/blog/*.md` | 30 artykułów w markdownie z front-matterem |
| `assets/` | CSS, JS, fonty lokalnie |
| `docs/` | research rynku, sitemap, plan SEO/AEO/GEO, baza FAQ |

## Budowanie

```bash
python3 build.py
```

Generator wyciąga system wizualny prosto z `index.html`, więc istnieje jedno źródło stylu. Na końcu uruchamia audyt, który sprawdza trzy rzeczy: brak cen w całym serwisie, brak długich pauz i jeden H1 na stronę.

## Skala

43 podstrony, 30 artykułów, około 53 700 słów treści. Schema: `LocalBusiness`, `Service`, `Article`, `FAQPage`, `BreadcrumbList`.

## Status

Prototyp. Wszystkie miejsca oznaczone w nawiasach kwadratowych czekają na dane: adres, telefon, metraż, modele sprzętu. Brakuje też zdjęć i osadzonych odcinków - kadry są na razie pustymi ramkami.
