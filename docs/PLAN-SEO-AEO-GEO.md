# Plan SEO, AEO i GEO - studio wideopodcastowe Warszawa

> Dokument z sierpnia 2026. Gdzie rozjeżdża się z [DECYZJE-2026-09.md](DECYZJE-2026-09.md), obowiązuje tamten.

Dokumenty powiązane: [sitemap i treści](SITEMAP-I-TRESCI.md), [30 artykułów](30-ARTYKULOW.md), [baza FAQ](FAQ-BAZA.md).

---

## 0. Punkt wyjścia z danych

Eksport Senuto pokazuje podział intencji, który determinuje całą strategię:

| Intencja | Frazy | Suma /mies. |
|---|---|---|
| Nagrania muzyczne, sale prób | studia nagraniowe 2900, studia nagraniowe warszawa 1300, studio nagrań warszawa 1000, sala prób warszawa 480, studio muzyczne warszawa 260, plus ogon cenowy | ~6540 |
| **Podcast** | **studio podcastowe warszawa 320, studio do podcastów 70, studio podcastowe warszawa cennik 20** | **~410** |

Nie wchodzimy w muzykę. Konsekwencja jest twarda i trzeba ją sobie powiedzieć wprost:

**Pierwsza pozycja na frazę główną to około 90 wejść miesięcznie.** Na tym nie stoi biznes. Dlatego strategia ma trzy nogi, a nie jedną:

1. **SEO** - zająć wszystkie frazy transakcyjne, których jest mało, ale są warte tysiące złotych za lead
2. **Content** - zbudować wolumen w ogonie informacyjnym, gdzie jest realna masa wyszukiwań
3. **GEO** - być odpowiedzią asystentów AI, bo przy takim wolumenie jedno cytowanie w ChatGPT jest warte więcej niż trzy kliknięcia z czwartej pozycji

**Do uzupełnienia:** eksport, który mam, był zbudowany wokół seeda „studio nagrań". Brakuje w nim całej gałęzi videocastowej. Przed ustawieniem ostatecznych priorytetów potrzebny drugi eksport pod seedy: videocast, produkcja podcastów, podcast firmowy, nagranie kursu online, produkcja rolek, talking head.

---

## 1. SEO on-page

### Zasady na każdą stronę

- Jeden H1, fraza główna w pierwszych 60 znakach
- Fraza główna w pierwszym akapicie, naturalnie, bez upychania
- H2 w formie pytań wszędzie, gdzie to naturalne - to karmi jednocześnie AEO
- Title do 60 znaków, z frazą i wyróżnikiem
- Meta description 150-160 znaków, **zawsze z konkretem**: liczbą, ceną albo terminem. „Zmontowany odcinek w 3 dni robocze. Cennik od X zł" bije „profesjonalne studio podcastowe w Warszawie"
- Nazwy plików obrazów frazowe, alty opisowe, format webp
- `loading="lazy"` na wszystkim poza pierwszym ekranem
- Tabela porównawcza w każdym artykule cenowym - Google wyciąga je do wyników

### Mapa fraz na strony

| Strona | Fraza główna | Frazy wspierające |
|---|---|---|
| `/` | studio podcastowe warszawa | studio wideopodcastowe, studio videocastowe warszawa |
| `/produkcja-podcastow-warszawa/` | produkcja podcastów warszawa | produkcja wideopodcastów, podcast firmowy produkcja |
| `/rolki-shorty-talking-head/` | produkcja rolek warszawa | shorty dla firm, talking head nagranie |
| `/nagrania-szkoleniowe-kursy-online/` | nagrania szkoleniowe warszawa | produkcja kursu online, materiały e-learningowe |
| `/cennik/` | studio podcastowe warszawa cennik | ile kosztuje nagranie podcastu, cennik produkcji podcastu |
| `/studio/` | studio do nagrań wideo warszawa | wynajem studia podcastowego warszawa |
| `/sprzet/` | sprzęt do nagrywania podcastu | jakie kamery do podcastu, ile kamer do podcastu |
| `/jak-pracujemy/` | jak wygląda produkcja podcastu | proces produkcji podcastu |
| `/faq/` | - | ogon pytaniowy, dziesiątki fraz long tail |

**Kontrola kanibalizacji:** żadne dwie strony nie mogą celować w tę samą frazę główną. Największe ryzyko: `/cennik/` kontra artykuł nr 1 („ile kosztuje nagranie wideopodcastu"). Rozwiązanie: `/cennik/` celuje w „studio podcastowe warszawa cennik" i jest stroną ofertową, artykuł celuje w „ile kosztuje nagranie podcastu" i jest analizą rynku. Artykuł linkuje do cennika, nie odwrotnie.

---

## 2. SEO techniczne

- Statyczny HTML albo Astro. Bez CMS-a na start
- **Core Web Vitals:** LCP poniżej 2,0 s, CLS poniżej 0,05, INP poniżej 200 ms
- Wideo w hero z `preload="none"` i posterem w webp. Plik do 3 MB
- Fonty lokalnie, `font-display: swap`, preload tylko wagi używanej w H1
- Kanoniczne na każdej stronie
- Breadcrumbs w JSON-LD na wszystkich podstronach
- Sitemap XML generowany automatycznie, zgłoszony w Search Console
- `robots.txt` bez blokad na CSS i JS
- Obrazy: webp, wymiary w atrybutach (przeciw CLS), **nigdy bez zachowania proporcji**

---

## 3. Schema - mapa typów

| Strona | Typ |
|---|---|
| `/` | `LocalBusiness` + `Organization` |
| Filary usługowe | `Service` + `Offer` + `FAQPage` |
| `/cennik/` | `Offer` z `priceCurrency: PLN` + `FAQPage` |
| `/studio/`, aranżacje | `Place` + `ImageObject` |
| `/realizacje/` | `CollectionPage` |
| `/realizacje/[slug]/` | `CreativeWork` + `VideoObject` |
| `/jak-pracujemy/` | `HowTo` + `FAQPage` |
| `/sprzet/` | `ItemList` |
| `/faq/` | `FAQPage` |
| `/o-nas/` | `AboutPage` + `Person` |
| `/opinie/` | `Review` + `AggregateRating` |
| Artykuły | `Article` + `BreadcrumbList` (+ `FAQPage` przy sekcji FAQ) |
| Karty odcinków | `VideoObject` z `thumbnailUrl`, `duration`, `uploadDate` |

`LocalBusiness` musi zawierać: `address`, `geo`, `telephone`, `openingHours`, `priceRange`, `areaServed: Warszawa`, `sameAs` z linkami do social i GBP.

---

## 4. GEO lokalne - Warszawa

To warstwa map i wyników lokalnych, osobna od GEO generatywnego z punktu 6.

**Google Business Profile**
- Kategoria główna: studio nagraniowe. Dodatkowe: usługa produkcji wideo, studio filmowe
- Zdjęcia z sesji - te same, co na stronie. Minimum 20, w tym wnętrze, sprzęt, plan w akcji
- Posty co tydzień: nowy odcinek, realizacja, aranżacja
- Pełne godziny otwarcia, opis z frazą główną, link do `/cennik/` a nie do strony głównej
- Sekcja pytań i odpowiedzi wypełniona samodzielnie pierwszymi 5 pytaniami z `/faq/`

**NAP spójny co do znaku.** Nazwa, adres i telefon w identycznym zapisie na stronie, w GBP i we wszystkich katalogach. „ul." albo „ulica" - jedno, wszędzie.

**Blok dojazdu** na `/studio/` i `/kontakt/`: czas dojścia od metra i przystanków w minutach, numery linii, liczba miejsc parkingowych, mapa osadzona lazy. Cynamon podaje „metro Imielin 7 min pieszo", Manufaktura wypisuje numery autobusów - to działa, bo znosi realną obiekcję.

**Opinie Google** - proces zbierania po każdej realizacji, z linkiem wysyłanym w mailu z plikami. Marsel ma 4,9 z 50 opinii i to widać w wynikach lokalnych.

**Agregatory:** Oferteo rankuje na „studio nagrań Warszawa". Obecność tam karmi jednocześnie GEO generatywne, bo asystenci czytają te listy.

---

## 5. AEO - optymalizacja pod odpowiedzi

Cel: featured snippet, People Also Ask, odpowiedzi asystentów.

### Zasady pisania

1. **Odpowiedź najpierw.** Każda sekcja zaczyna się od zwięzłej odpowiedzi w 40-60 słów, dopiero potem rozwinięcie. To jest dokładnie ten format, który wchodzi do snippetu.
2. **Definicja pod H1**, nad spisem treści. Jedno zdanie odpowiadające wprost na tytuł.
3. **H2 jako pytania.**
4. **Liczby zamiast przymiotników.** „Montaż zajmuje 3 dni robocze" zamiast „szybki montaż". „52 m2" zamiast „przestronne studio".
5. **Tabele przy każdym porównaniu** - są wyciągane bezpośrednio do wyników.
6. **Listy numerowane przy procesach** - karmią `HowTo`.
7. **Jedna myśl na akapit**, akapity po 2-4 zdania.

### Skąd biorą się pytania

`/faq/` jest generatorem tematów, nie zamkniętą listą. Każde pytanie z bazy, które ma potencjał wyszukiwania, dostaje z czasem własny artykuł. Kolejność: pytanie w FAQ → obserwacja w Search Console → jeśli generuje wyświetlenia, rozwinięcie w artykuł.

---

## 6. GEO generatywne - bycie cytowanym przez AI

Przy 320 wyszukiwaniach miesięcznie na frazę główną to jest ważniejsze niż pozycja w Google.

### Co powoduje cytowanie

1. **Jawne dane liczbowe.** Cennik z kwotami, metraż, liczba kamer, czasy dostawy. Studia, które chowają ceny, nie są cytowane, bo nie ma czego zacytować. To jest twardy argument za jawnym cennikiem, silniejszy niż argument konwersyjny.
2. **Unikalne dane własne.** Wasze liczby z prowadzenia GSA: ile trwa montaż odcinka, ile rolek wychodzi z godziny nagrania, jak wygląda krzywa oglądalności w pierwszych czterech tygodniach. Nikt inny takich danych nie ma, więc silnik musi wskazać źródło.
3. **Struktura odpowiedziowa** - punkt 5.
4. **Wzmianki poza własną domeną.** Zestawienia „najlepsze studia podcastowe w Warszawie" to pierwsze, co silniki czytają. Trzeba tam być: Oferteo, katalogi branżowe, artykuły w mediach, wymiana z podcasterami. Studio Miś ma sekcję „napisali o nas" z Wirtualnymi Mediami, Bankier.pl i WhiteMad - to nie przypadek.
5. **`llms.txt`** - analogiczny do tego, który macie przy GSA: streszczenie oferty, cennik, specyfikacja sprzętu, formaty, dane kontaktowe. Czysty tekst, bez marketingu.

### Monitoring

Raz w miesiącu zadać ChatGPT, Perplexity i sprawdzić Google AI Overviews na zestawie pytań:

1. Gdzie w Warszawie nagrać podcast firmowy?
2. Ile kosztuje produkcja podcastu firmowego w Polsce?
3. Najlepsze studia podcastowe w Warszawie
4. Studio wideopodcastowe Warszawa cennik
5. Ile kamer potrzeba do nagrania podcastu?
6. Czy lepiej nagrywać podcast w studiu czy w biurze?
7. Kto produkuje podcasty dla firm w Warszawie?
8. Ile trwa montaż odcinka podcastu?
9. Gdzie nagrać kurs online w Warszawie?
10. Jak wygląda produkcja podcastu od początku do końca?

Zapisywać: czy jesteśmy cytowani, kto jest cytowany zamiast nas, z jakiego źródła silnik bierze dane. To jest jedyna wiarygodna miara postępu w GEO.

---

## 7. Mierzenie

| Metryka | Narzędzie | Częstotliwość |
|---|---|---|
| Pozycje na frazy główne | Search Console | miesięcznie |
| Wyświetlenia i CTR per strona | Search Console | miesięcznie |
| Wejścia na `/cennik/` | GA4 | tygodniowo |
| Odtworzenia odcinków na stronie | GA4, zdarzenie | miesięcznie |
| **Wysłane formularze z podziałem na źródło** | GA4, zdarzenie | tygodniowo |
| Cytowania w AI | ręcznie, zestaw 10 pytań | miesięcznie |
| Opinie Google | GBP | miesięcznie |

**Cel jest biznesowy, nie ruchowy.** Przy tym wolumenie 10 dobrych formularzy miesięcznie jest warte więcej niż 3000 wejść. Nie optymalizujemy pod ruch, tylko pod wypełnione formularze od firm.
