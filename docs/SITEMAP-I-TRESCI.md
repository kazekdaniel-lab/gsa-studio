# Architektura treści i sitemap

Studio wideopodcastowe, Warszawa. Model: pełna produkcja end-to-end.
Filary usługowe: wideopodcast, rolki/shorty/talking head, nagrania szkoleniowe i kursy online.
Poza zakresem: webinary i transmisje live, sesje foto, nagrania muzyczne i sale prób.

Dokumenty powiązane: [research rynku](RESEARCH-RYNEK-I-DESIGN.md), [koncepcja end-to-end](KONCEPCJA-STRONY-END-TO-END.md), [projekt strony](PROJEKT-STRONY.md), [plan SEO/AEO/GEO](PLAN-SEO-AEO-GEO.md), [30 artykułów](30-ARTYKULOW.md), [baza FAQ](FAQ-BAZA.md).

---

## 1. Osiem warstw treści

Zanim sitemap, trzeba nazwać, jakie typy treści w ogóle żyją na stronie studia wideopodcastowego. Każda warstwa odpowiada na inne pytanie w głowie klienta i ma inny cel.

| Warstwa | Pytanie klienta | Cel | Gdzie żyje |
|---|---|---|---|
| 1. Transakcyjna | Ile to kosztuje i jak zamówić | konwersja | `/cennik/`, `/kontakt/` |
| 2. Przestrzeń | Jak to będzie wyglądać na ekranie | dowód wizualny | `/studio/` + aranżacje |
| 3. Formaty | Czy robicie to, czego potrzebuję | kwalifikacja leada | 3 filary usługowe |
| 4. Dowód | Czy komuś to wyszło | zaufanie, cytowalność w AI | `/realizacje/` |
| 5. Proces i logistyka | Co mnie czeka i ile mnie to zajmie | zbijanie obiekcji | `/jak-pracujemy/`, `/faq/` |
| 6. Technika | Czy to jest dobre technicznie | wygrywanie porównań | `/sprzet/` |
| 7. Edukacja | Jak to w ogóle działa | ruch organiczny | `/blog/` |
| 8. Zaufanie | Kim jesteście | E-E-A-T, lokalne SEO | `/o-nas/`, `/opinie/` |

**Warstwy 5 i 6 leżą na rynku warszawskim odłogiem.** Sprawdziłem 13 studiów: nikt nie pisze wprost ile godzin klienta zjada podcast, ile trwa montaż, jak wygląda backup materiałów ani jakie dokładnie pliki dostaje klient. A to są pytania, które ludzie zadają dziś asystentom AI. Tam jest nasze wejście.

---

## 2. Konwencje

- Małe litery, myślniki, bez polskich znaków w URL-ach
- Bez dat i bez zagnieżdżania po roku
- Maksymalnie 3 poziomy
- Slash na końcu, konsekwentnie
- Blog płasko: `/blog/[slug]/`, nie `/blog/kategoria/[slug]/` - kategorie są tylko widokiem filtrującym

---

## 3. Sitemap z zawartością

### `/` - strona główna

**Fraza:** studio podcastowe warszawa (320/mies.)
**Cel:** konwersja plus dowód. Nie jest stroną SEO-ową w klasycznym sensie, jest wizytówką i rozdzielaczem ruchu.
**Schema:** `LocalBusiness` + `Organization`
**Linkuje do:** 3 filarów, `/cennik/`, `/realizacje/`, `/studio/`. Nigdy bezpośrednio do artykułów.

Sekcje w kolejności (pełna rozpiska z copy w [PROJEKT-STRONY.md](PROJEKT-STRONY.md), część II):
hero, pasek dowodu, co produkujemy (osadzone odcinki), jak to działa, ile Cię to kosztuje czasu, co dostajesz z jednego zjazdu, formaty, pakiety i cennik, dlaczego my, studio, specyfikacja techniczna, zespół, opinie, FAQ, kontakt, stopka.

---

### `/produkcja-podcastow-warszawa/` - filar 1

**Fraza:** produkcja podcastów warszawa, produkcja wideopodcastów
**Cel:** hub głównej usługi. Najważniejsza strona SEO na całym serwisie.
**Schema:** `Service` + `Offer` + `FAQPage`
**Objętość:** 1400-1800 słów
**Linkuje w dół do:** klastrów A, B, C, D, E (minimum 12 artykułów)

Co zawiera:
1. Nagłówek z frazą i obietnicą wyniku
2. Odpowiedź w 40-60 słów: czym jest pełna produkcja i co obejmuje. To karmi snippet
3. Dla kogo - trzy typy klienta: firma budująca markę eksperta, marka osobista, zespół sprzedaży B2B
4. Co obejmuje produkcja end-to-end - 5 etapów w skrócie, każdy z linkiem do artykułu rozwijającego
5. Co dostajesz z jednego zjazdu - konkretne liczby deliverables
6. Formaty w ramach usługi: rozmowa 2 osoby, panel 3-4, solo. Liczba kamer i kadry przy każdym
7. Ile to trwa - oś czasu od pierwszej rozmowy do publikacji
8. Ile to kosztuje - widełki plus link do `/cennik/`
9. Realizacje - 3 kafle plus link do `/realizacje/`
10. FAQ na 5 pytań
11. CTA

---

### `/rolki-shorty-talking-head/` - filar 2

**Fraza:** produkcja rolek warszawa, talking head, shorty dla firm
**Cel:** przechwycenie klienta, który nie jest gotowy na serię podcastową, ale potrzebuje krótkich form. Wejście do lejka.
**Schema:** `Service` + `Offer` + `FAQPage`
**Objętość:** 1200-1500 słów

Co zawiera:
1. Odpowiedź: czym są krótkie formy pionowe i skąd się biorą
2. Dwa źródła materiału: wycinane z długiego nagrania vs kręcone osobno jako talking head. Różnica w cenie i efekcie
3. Ile rolek realnie wychodzi z godziny nagrania - konkretna liczba, nie "wiele"
4. Format techniczny: 1080x1920, napisy wypalane, długość, bezpieczne marginesy pod interfejs platform
5. Pod jakie platformy: Reels, TikTok, Shorts, LinkedIn. Różnice w tym, co działa
6. Pakiety i ceny
7. Realizacje - siatka pionowych kafli
8. FAQ
9. CTA plus link krzyżowy do filaru 1 ("jeśli myślisz o serii, tu jest pełna produkcja")

---

### `/nagrania-szkoleniowe-kursy-online/` - filar 3

**Fraza:** nagrania szkoleniowe warszawa, produkcja kursu online, materiały e-learningowe
**Cel:** inny klient niż podcastowy (HR, L&D, twórcy kursów), ta sama przestrzeń i sprzęt.
**Schema:** `Service` + `Offer` + `FAQPage`
**Objętość:** 1200-1500 słów

Co zawiera:
1. Odpowiedź: co obejmuje nagranie kursu w studiu
2. Trzy typy materiałów: moduły wykładowe, onboarding pracowniczy, szkolenia produktowe
3. Prompter - dlaczego przy kursach jest obowiązkowy, a nie dodatkowy
4. Struktura nagrania: jak dzielić materiał na moduły, żeby dało się go później aktualizować pojedynczo
5. Co dostajesz: pliki, napisy, transkrypcja, wersje pod LMS
6. Ceny
7. FAQ
8. CTA

---

### `/cennik/` - strona transakcyjna

**Fraza:** studio podcastowe warszawa cennik (20/mies.), ile kosztuje nagranie podcastu
**Cel:** jedyna strona, na którą wchodzi ktoś gotowy kupić. Musi mieć osobny URL, bo tak szukają i tak linkują artykuły.
**Schema:** `Offer` z `priceCurrency: PLN` + `FAQPage`

Co zawiera:
1. Zdanie o tym, dlaczego ceny są jawne. Trzy studia w Warszawie ich nie podają i na tym tracą
2. Pilot - produkt wejściowy, cena, zakres
3. Trzy abonamenty w tabeli porównawczej, środkowy wyróżniony
4. Odcinek pojedynczy poza abonamentem
5. **Tabela "w cenie / dopłata"** - odpowiedź na największą pułapkę rynku, czyli identycznie nazwane oferty znaczące co innego
6. Dodatki z cenami jednostkowymi: rolki, transkrypcja, animacje, prompter, makijaż
7. Warunki: minimum, okres wypowiedzenia, polityka anulacji, terminy płatności
8. FAQ cenowe na 5 pytań
9. CTA

---

### `/studio/` - hub przestrzeni

**Fraza:** studio do nagrań wideo warszawa, wynajem studia podcastowego warszawa (40/mies. na wariant nagraniowy)
**Cel:** podwójny. Pokazać przestrzeń klientom produkcyjnym i przechwycić ruch szukający wynajmu, żeby przekierować go na produkcję.
**Schema:** `Place` + `LocalBusiness`

Co zawiera:
1. Kadr główny studia
2. Dane w blokach: powierzchnia, wysokość, maks. osób na planie, reżyserka, liczba konfiguracji
3. Trzy nazwane aranżacje jako kafle z linkiem do podstron
4. Zaplecze: garderoba, charakteryzatornia, kuchnia, klimatyzacja, parking
5. **Dojazd** - czas dojścia od metra i przystanków w minutach, numery linii, liczba miejsc parkingowych, mapa. Konkurencja to robi i to działa
6. Akapit przekierowujący: "szukasz wynajmu godzinowego?" z uczciwym wyjaśnieniem, że pracujemy w modelu produkcyjnym, i linkiem do `/cennik/`
7. CTA

---

### `/studio/[aranzacja]/` x3

**Cel:** to samo, co robi Studio Miś pod `/space/[nazwa]` - zamiana jednej sali w trzy rozpoznawalne miejsca. Koszt: kilka mebli i jedna sesja zdjęciowa.
**Schema:** `Place` + `ImageObject`
**Objętość:** 400-600 słów każda

Proponowany podział:
- **Aranżacja 1** - ciemna, kinowa. Pod biznes i rozmowy 1:1
- **Aranżacja 2** - jasna, ciepła. Pod lifestyle i rozmowy kameralne
- **Aranżacja 3** - z ekranem lub mocnym akcentem kolorystycznym. Pod panele i formaty publicystyczne

Nazwy własne do ustalenia razem z sesją zdjęciową - to branding, nie SEO.

Co zawiera każda:
1. Eyebrow z charakterem ("KOSMICZNA ENERGIA" u Miś to dobry wzór), nazwa, jedno zdanie
2. Galeria 4 kadrów wg [briefu fotograficznego](PROJEKT-STRONY.md)
3. Dla jakich formatów i tematów
4. Ile osób mieści, jakie ustawienia (stół, fotele, solo)
5. Link do pozostałych aranżacji
6. CTA

---

### `/realizacje/` - katalog dowodu

**Cel:** sekcja, której nie ma żaden konkurent w Warszawie w tej formie. Na 8 sprawdzonych polskich stron na żadnej nie da się obejrzeć odcinka nagranego w tym studiu.
**Schema:** `CollectionPage`

Co zawiera: siatka kafli z filtrem po branży i po formacie, każdy kafel wg wzoru kart gości z decku GSA (miniatura 16:9 z pomarańczową ramką, badge, nazwisko wersalikami, firma pomarańczowa).

---

### `/realizacje/[slug]/` - case study

**Cel:** najlepszy materiał pod cytowanie przez silniki AI, bo zawiera konkrety z liczbami.
**Schema:** `CreativeWork` + `VideoObject`
**Objętość:** 500-800 słów

Struktura: kto, po co, jaki format wybraliśmy i dlaczego, co dokładnie dostarczyliśmy (liczby), jaki był efekt (liczby), materiał do obejrzenia, cytat klienta.

---

### `/jak-pracujemy/` - proces

**Fraza:** jak wygląda produkcja podcastu
**Schema:** `HowTo` + `FAQPage`
**Objętość:** 1000-1200 słów

Co zawiera: 5 etapów rozpisanych szczegółowo (strategia i format, przygotowanie, zjazd zdjęciowy, postprodukcja, publikacja), oś czasu z konkretnymi dniami roboczymi, tabela "po Twojej stronie / po naszej stronie", akapit o akceptacji materiału i liczbie rund poprawek, akapit o backupie i przechowywaniu plików.

---

### `/sprzet/` - specyfikacja techniczna

**Fraza:** sprzęt do nagrywania podcastu, jakie kamery do podcastu
**Cel:** niedoceniana strona. Nikt na rynku nie ma osobnego URL-a ze specyfikacją, a to dokładnie to, czego szuka ktoś porównujący trzy oferty - i to, co silnik AI cytuje przy pytaniu "na czym nagrywa studio X".
**Schema:** `ItemList`
**Objętość:** 800-1000 słów

Co zawiera:
1. Obraz: kamery z modelami i liczbą, obiektywy, switcher, **rejestracja ISO na osobnych ścieżkach** z wyjaśnieniem, dlaczego to ma znaczenie dla klienta
2. Dźwięk: mikrofony z modelami, interfejs, rejestrator, ścieżki, mastering
3. Światło: modele, schemat 3-punktowy, standaryzacja dla wszystkich osób na planie
4. Dodatki: prompter, monitor podglądowy, ekran na grafiki
5. Formaty wyjściowe: 4K i 1080p poziom, 1080x1920 pion, mp3, transkrypcja srt i txt
6. Backup i przechowywanie: gdzie leżą pliki, jak długo, jak je odbieracie
7. Kadry: jakie ujęcia przy jakiej liczbie osób

**Zasada twarda:** tylko to, co realnie macie. Klienci porównują modele, a rozbieżność wychodzi na pierwszym nagraniu.

---

### `/faq/` - baza pytań

**Cel:** główna strona pod AEO. Studio Miś ma 30 pytań i to jest właściwa skala.
**Schema:** `FAQPage`
**Zawartość:** [FAQ-BAZA.md](FAQ-BAZA.md), 7 grup tematycznych

---

### `/o-nas/` i `/opinie/`

`/o-nas/` - zespół z rolami i twarzami, historia, i najważniejsze: dlaczego prowadzimy własny podcast. To jest przewaga, której konkurencja nie skopiuje. Schema: `AboutPage` + `Person` dla każdej osoby.

`/opinie/` - do uruchomienia dopiero po pierwszych realizacjach. Cytaty z nazwiskiem, funkcją i firmą. Nie wstawiać wymyślonych. Schema: `Review`.

---

### `/blog/` i artykuły

`/blog/` - hub z listą, kategoriami i wyróżnionym artykułem filarowym.
`/blog/[slug]/` - 30 artykułów, rozpisane w [30-ARTYKULOW.md](30-ARTYKULOW.md).

Kategorie jako widoki filtrujące: koszty i wycena, wybór studia, proces nagrania, strategia podcastu, dystrybucja i efekt.

---

### Techniczne i prawne

`/polityka-prywatnosci/`, `/regulamin/`, `/sitemap.xml`, `/robots.txt`, `/llms.txt`

---

## 4. Linkowanie wewnętrzne

Model hub and spoke. Trzy huby to trzy filary usługowe.

| Kierunek | Zasada |
|---|---|
| Strona główna → | tylko huby, `/cennik/`, `/realizacje/`, `/studio/`. Nigdy bezpośrednio do artykułów |
| Hub → w dół | 5-8 artykułów ze swojego klastra |
| Hub → w poprzek | `/cennik/`, `/realizacje/`, `/sprzet/` |
| Artykuł → w górę | zawsze do swojego huba |
| Artykuł → w bok | 2-3 artykuły z tego samego klastra |
| Artykuł → konwersja | **zawsze** `/cennik/` albo `/kontakt/` |

ArtBoyz robi 5-6 linków wewnętrznych na artykuł i to jest właściwy poziom. Mniej to zmarnowany link juice, więcej to spam.

---

## 5. Czego świadomie nie robimy

**Stron pod dzielnice.** „Studio podcastowe Mokotów", „studio podcastowe Wola" i tak dalej. Wolumen zerowy, a Google traktuje takie strony jako doorway pages i potrafi za nie ukarać. Zamiast tego jeden mocny blok dojazdu na `/studio/` i `/kontakt/` plus Google Business Profile.

**Fraz muzycznych i sal prób.** W danych Senuto to około 6540 wyszukiwań miesięcznie wobec 410 podcastowych, ale to inna usługa i inny klient. Muzyk szukający sali za 100 zł/h nigdy nie kupi produkcji za kilka tysięcy.

**Webinarów i transmisji live.** Poza zakresem usług.

**Sesji foto jako osobnej usługi.** Poza zakresem. Zdjęcia z sesji zostają dodatkiem w pakietach.
