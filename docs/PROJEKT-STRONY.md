# Projekt strony studia - specyfikacja wykonawcza

> Dokument z sierpnia 2026. Gdzie rozjeżdża się z [DECYZJE-2026-09.md](DECYZJE-2026-09.md), obowiązuje tamten.

Model: pełna produkcja end-to-end. Podstawa: [research rynku](RESEARCH-RYNEK-I-DESIGN.md) i [koncepcja end-to-end](KONCEPCJA-STRONY-END-TO-END.md).

Wszystko w nawiasach kwadratowych `[TAK]` to placeholder do uzupełnienia przez Was. Copy poniżej to gotowy draft, nie opis "co tu wstawić".

---

## CZĘŚĆ I - SYSTEM PROJEKTOWY

Źródło stylu: `OFERTA_GSA_v2.pdf`. Poniżej rozłożony na części pierwsze, bo to nie jest "ciemny motyw z pomarańczem" tylko zbudowany język z kilkoma powtarzalnymi sygnaturami. Strona ma być rozwinięciem tego decku na web, nie osobnym projektem.

### 1.1 Dwa tryby, nie jeden

Najważniejsza obserwacja z decku: **on oddycha przeplotem**. Slajdy chodzą naprzemiennie ciemny - kremowy - kremowy - ciemny - ciemny - kremowy. Ciemne niosą emocję i obraz (okładka, portret Oskara, karty gości, formaty reklamowe), kremowe niosą dane i liczby (statystyki kanału, demografia, cennik).

To jest gotowa reguła dla strony: **ciemne = dowód i emocja, kremowe = liczby i warunki**. Strona zbudowana wyłącznie na ciemnym tle straciłaby połowę tego systemu.

**Tryb ciemny**
| Token | Hex | Zastosowanie |
|---|---|---|
| `--dark-bg` | `#1A0F0A` | tło, ciepła prawie-czerń z brązem (nie neutralna czerń) |
| `--dark-bg-deep` | `#120A06` | krawędzie kadru, dolne partie gradientu |
| `--dark-card` | `#0B0705` | wnętrze kart wideo, obszary pod obraz |
| `--dark-line` | `#3A2A20` | separatory 1px |
| `--cream` | `#F5E9D5` | tekst główny na ciemnym |
| `--cream-muted` | `#A89684` | podpisy, metadane, tekst drugorzędny |

**Tryb kremowy**
| Token | Hex | Zastosowanie |
|---|---|---|
| `--light-bg` | `#FAF7F2` | tło sekcji danych |
| `--ink` | `#1A1410` | tekst główny na kremowym |
| `--ink-muted` | `#6B6259` | labelki, opisy pod liczbami |
| `--light-line` | `#DED7CC` | linie w tabelach |

**Akcent, wspólny dla obu trybów**
| Token | Hex | Zastosowanie |
|---|---|---|
| `--orange` | `#FF5900` | druga część nagłówka, liczby, ramki, bullety, ceny |
| `--orange-deep` | `#C2410C` | hover, cieńsze obramowania |

Proporcja akcentu w decku jest bardzo zdyscyplinowana: pomarańcz nigdy nie jest tłem dużej powierzchni. Jest wyłącznie na tekście, liczbach, cienkich ramkach i pigułkach. Trzymamy to na stronie.

### 1.2 Poświata i ziarno

Ciemne slajdy nie są płaskie. Mają dwie warstwy, które trzeba odtworzyć w CSS, bo bez nich całość wygląda tanio:

1. **Radialna poświata pomarańczowa** w narożniku, bardzo rozmyta i słaba: `radial-gradient(ellipse 80% 60% at 15% 20%, rgba(255,89,0,0.16), transparent 60%)`. Na okładce idzie z lewej góry, na slajdzie kontaktowym z prawej.
2. **Ziarno filmowe** - subtelny szum na całości, `opacity: 0.04`, jako `svg feTurbulence` inline albo mały kafelek png. To jest to, co daje decku kinowy, a nie prezentacyjny charakter.

Kremowe slajdy są czyste - zero poświaty, zero ziarna. Kontrast faktur jest częścią rytmu.

### 1.3 Typografia

Deck używa **bold geometrycznego grotesku o wysokim x-height, z dwupiętrowym `a`**. To nie jest Bebas Neue (którego używa obecna strona gsa) ani Poppins. Charakterystyka pasuje do rodziny Aeonik / Gilroy / Greycliff CF / Cera Pro.

**Do ustalenia:** potrzebuję pliku fontu użytego w decku, żeby strona była 1:1. Jeśli licencja nie pozwala na web, najbliższe darmowe zamienniki to Plus Jakarta Sans ExtraBold i Figtree Black - obie mają tę samą geometrię i dwupiętrowe `a`.

Jedna rodzina na całość, różnicowana wagą - deck nie miesza krojów:

| Rola | Waga | Rozmiar desktop | Rozmiar mobile | Uwagi |
|---|---|---|---|---|
| H1 hero | 800 | 92px | 44px | line-height `0.98`, tracking `-0.02em` |
| H2 sekcja | 800 | 60px | 34px | line-height `1.02`, tracking `-0.02em` |
| Wielka liczba | 800 | 88px | 48px | tabular-nums, sufiks 40% rozmiaru |
| H3 karta | 700 | 26px | 21px | |
| Lead | 500 | 21px | 17px | max szerokość 660px |
| Body | 400 | 17px | 16px | line-height `1.55` |
| Eyebrow | 600 | 12px | 11px | uppercase, tracking `0.22em` |
| Nazwisko na karcie | 700 | 15px | 14px | uppercase, tracking `0.06em` |

**Nagłówek dwukolorowy** to sygnatura decku: pierwsza część kremowa, druga pomarańczowa. "Reklama, / **która nie znika**". "Najlepsze sloty schodzą **pierwsze**". Na stronie stosujemy to na H1 i na najważniejszych H2, ale nie na wszystkich - w decku też nie każdy nagłówek to ma.

### 1.4 Sygnatury - elementy, po których to poznasz

To jest sedno. Bez tych czterech rzeczy strona nie będzie wyglądała jak GSA, choćby kolory się zgadzały.

**A. Nawias klamrowy**
Duży, cienki, pomarańczowy nawias otwierający i zamykający, obejmujący blok treści. W decku obejmuje: box z momentum, kartę Oskara Szarka, każdą cenę. To jest najmocniejszy rozpoznawalny element całego systemu.

Wykonanie: pseudoelementy `::before` i `::after`, obramowanie `2px` po trzech krawędziach, promień `20px`, kolor `--orange`, wysokość `100%`, szerokość `18px`. Na mobile schodzi do `12px`.

Na stronie stosujemy go przy: cenie każdego pakietu, wyróżnionej liczbie w pasku dowodu, bloku "co dostajesz z jednego zjazdu" i cytacie w sekcji o Waszym podcaście. **Nie częściej niż 4 razy na stronie głównej** - w decku też jest oszczędny.

**B. Gwiazdka GSA jako bullet**
Ośmioramienna gwiazdka z logo, pomarańczowa, zastępuje kropki na wszystkich listach. Rozmiar `14px`, odstęp od tekstu `12px`, wyrównana do pierwszej linii. W decku pojawia się też jako separator przy kanałach dystrybucji ("✱ YouTube ✱ Spotify").

**C. Eyebrow z szerokim trackingiem**
Nad każdym nagłówkiem sekcji: uppercase, `12px`, tracking `0.22em`. Na ciemnym w kolorze `--orange`, na kremowym w `--ink-muted`. W decku: "PODCAST GROWTH SCALE AUTOMATE", "FORMAT REKLAMOWY", "ROZMAWIALI W GSA", "DEMOGRAFIA WIDZA", "KLUCZOWE WNIOSKI DLA SPONSORÓW".

To zastępuje moją wcześniejszą propozycję numerowania sekcji `01 /`. Numeracja była z innego systemu - eyebrow jest z Waszego.

**D. Bold pomarańczowy w środku zdania**
Inline highlight na kluczowej frazie w akapicie: `font-weight: 700; color: var(--orange)`. Deck robi tym całą hierarchię czytania w tekstach opisowych ("transfer autorytetu Oskara", "w pierwszych 5-10 minutach", "Najdroższa pojedyncza jednostka"). Na stronie to główne narzędzie skanowalności - zamiast wypunktowań wszędzie.

### 1.5 Komponenty

**Karta wideo / odcinka** - najważniejszy komponent, bo strona stoi na dowodzie wideo. Wprost z kart gości w decku:
- proporcja `16:9`, promień `14px`
- obramowanie `2px solid --orange` na kartach wyróżnionych, `2px solid --cream` na kartach oznaczonych inaczej (deck używa kremowego obramowania dla odcinków przed emisją - mamy gotowy mechanizm na oznaczanie stanów)
- badge w prawym górnym rogu: ikona + liczba, `12px`, tło `rgba(0,0,0,0.6)`, promień pełny
- badge w lewym górnym rogu na stany: "Odcinek przed emisją" z trójkątem play
- pod kartą, wyśrodkowane: nazwisko wersalikami `--cream`, pod nim firma wersalikami `--orange` mniejszym stopniem
- siatka 3 kolumny x 2 rzędy na desktopie, 2 kolumny na tablecie, 1 na mobile

**Pigułka ceny** - z tabeli cennika w decku: obramowanie `1.5px solid --orange`, promień pełny, tekst `--orange` waga 700, padding `10px 22px`, tło przezroczyste. Suma końcowa bez pigułki, za to wielka i pomarańczowa.

**Wiersz cennika** - jasne tło, wiersze rozdzielone `1px --light-line`, nazwa pozycji po lewej wagą 700, opis pod nią `13px --ink-muted`, cena po prawej w pigułce. Ostatni wiersz oddzielony grubszą linią `2px --ink`.

**Blok czterech wniosków** - z pasków pod danymi: nad każdym nagłówkiem pozioma kreska `2px --orange` szerokości `48px`, pod nią nagłówek wagą 700, pod nim akapit `14px` z inline highlightami. Cztery kolumny na desktopie, dwie na tablecie.

**Przycisk główny** - deck ma go w formie kremowej pigułki ("SUBSKRYBUJESZ", "ZOBACZ JAK TO WYGLĄDA W AKCJI"). Na stronie: tło `--cream` na ciemnym tle sekcji, tekst `--dark-bg`, waga 700, uppercase, tracking `0.08em`, promień pełny, padding `16px 32px`. Wariant pomarańczowy tylko dla jednego, najważniejszego CTA na stronie.

**Przycisk drugi** - obramowanie `1.5px --cream-muted`, tekst `--cream`, przezroczysty. Hover: obramowanie `--orange`.

**Portret wycięty** - Oskar na okładce jest wycięty z tła i położony na ciemnym. To działa i warto powtórzyć w sekcji o zespole: portrety wycięte, nie kadrowane prostokąty.

### 1.6 Siatka i przestrzeń

- Kontener `1320px`, padding boczny `24px` mobile / `64px` desktop
- Siatka 12 kolumn, gutter `24px`
- Odstęp między sekcjami: `140px` desktop / `80px` mobile
- **Marginesy w decku są duże i to jest część charakteru.** Nagłówek startuje wysoko, treść nie dotyka krawędzi, między blokami jest powietrze. Nie zagęszczać.
- Promienie: karty `14px`, pigułki i przyciski pełne, nawias klamrowy `20px`. Zaokrąglone, nie kanciaste.

### 1.7 Rytm sekcji na stronie głównej

Przełożenie przeplotu z decku na kolejność ekranów:

| Sekcja | Tryb |
|---|---|
| 01 Nawigacja | ciemny, przezroczysty na starcie |
| 02 Hero | **ciemny** + poświata + ziarno |
| 03 Pasek dowodu | **kremowy** - liczby |
| 04 Co produkujemy | **ciemny** - karty wideo |
| 05 Jak to działa | **kremowy** - proces i dane |
| 06 Ile Cię to kosztuje czasu | **kremowy** - wykres |
| 07 Co dostajesz z jednego zjazdu | **ciemny** - liczby w nawiasach |
| 08 Formaty | **ciemny** - kadry i zdjęcia planu |
| 09 Pakiety i cennik | **kremowy** - tabela |
| 10 Dlaczego my | **ciemny** + portret + poświata |
| 11 Studio | **ciemny** - galeria |
| 12 Specyfikacja techniczna | **kremowy** - dane |
| 13 Zespół | **kremowy** - portrety wycięte |
| 14 Opinie | **ciemny** |
| 15 FAQ | **kremowy** |
| 16 Kontakt | **ciemny** + poświata z prawej, jak slajd kontaktowy w decku |
| 17 Stopka | ciemny głębszy |

Przejścia między trybami bez separatorów i bez skosów. Twarda krawędź, tak jak między slajdami.

### 1.8 Zasady wizualne

1. Materiał wideo dominuje nad zdjęciami wnętrza. Sekcja 04 dostaje najwięcej powierzchni.
2. Żadnego deformowania obrazów. Zawsze `object-fit: cover` z zachowaniem proporcji.
3. Hero: wyciszone wideo z planu, `autoplay`, `loop`, `playsinline`, do 3 MB, poster jako fallback. Na nim ta sama poświata i ziarno co na okładce decku.
4. Animacje: `fade-up` przy wejściu w viewport, 400 ms, `ease-out`. Liczby animowane licznikiem od zera. Zero parallaxu.
5. Mobile: sticky pasek na dole z jednym CTA. Nawias klamrowy zwęża się, nie znika.
6. Deck jest w proporcji 16:9 i ma dużo powietrza po bokach - strona ma to utrzymać. Nie rozciągać treści na całą szerokość ekranu.

---

## CZĘŚĆ II - STRONA GŁÓWNA, EKRAN PO EKRANIE

### 01 - Nawigacja

Sticky, wysokość `72px`, tło `rgba(12,10,8,0.85)` z `backdrop-filter: blur(12px)`, dolna linia `1px --line`.

Lewa: logo. Środek: `Jak działamy` / `Realizacje` / `Pakiety` / `Studio` / `Kontakt`. Prawa: telefon `[TELEFON]` jako link tel: + przycisk **Umów rozmowę**.

Mobile: logo + hamburger, CTA zjeżdża do sticky paska na dole.

---

### 02 - Hero

Layout: pełna szerokość, wysokość `88vh`. Tło: wideo z planu, na nim nakładka `linear-gradient(180deg, rgba(12,10,8,0.5), rgba(12,10,8,0.95))`.

**Label (12px, accent):** PRODUKCJA WIDEOPODCASTÓW / WARSZAWA

**H1:**
> TWÓJ PODCAST.
> OD POMYSŁU DO PUBLIKACJI.

**Lead (22px, max 640px):**
> Przyjeżdżasz na jeden dzień i rozmawiasz. Całą resztę - format, kamery, montaż, rolki, opisy i publikację - bierzemy na siebie. Sami prowadzimy podcast [NAZWA/GSA], więc wiemy, co się dzieje z odcinkiem po tym, jak wyjdziesz ze studia.

**CTA:** `Umów rozmowę` (główny) + `Zobacz, co produkujemy` (drugi, scroll do sekcji 04)

**Pasek pod CTA (12px, muted, rozdzielony kropkami):**
> 3 kamery 4K · Realizator w cenie · Zmontowany odcinek w [X] dni roboczych

---

### 03 - Pasek dowodu

Wąska sekcja, tło `--surface`, padding `48px 0`.

Wariant A (jeśli macie logotypy klientów): rząd 5-8 logotypów w skali szarości, opacity `0.5`, hover pełny kolor.

Wariant B (na start, jeśli logotypów brak): 4 wielkie liczby.

| `[X]` | `[X]` | `[X]` | `[X]` |
|---|---|---|---|
| ODCINKÓW WYPRODUKOWANYCH | GODZIN NA PLANIE | MAREK NA POKŁADZIE | DNI OD NAGRANIA DO PUBLIKACJI |

**Nie wstawiać wymyślonych liczb.** Jeśli nie ma czym wypełnić, sekcja wypada, a jej miejsce zajmuje sekcja 04.

---

### 04 - Co produkujemy (sekcja kluczowa)

To jest jedyna rzecz na tej stronie, której nie ma żaden konkurent w Warszawie. Dostaje najwięcej powierzchni.

**Eyebrow:** CO PRODUKUJEMY
**H2:** OBEJRZYJ, ZANIM ZADZWONISZ

**Lead:**
> Nie opowiadamy o jakości. Poniżej są odcinki, które wyszły z tego studia. Włącz dowolny i oceń sam.

Layout: pierwszy odcinek duży (`16:9`, 8 kolumn), obok niego lista 3 kolejnych (4 kolumny, miniatura `160px` + tytuł + metadane). Pod spodem rząd 3 mniejszych kafli.

Każdy kafel: miniatura z overlayem play, tytuł odcinka, nazwa marki/gościa, długość, format (np. `wideopodcast · 2 osoby · 3 kamery`).

Odtwarzanie: lightbox z osadzonym YouTube, `lazy`, bez autoplay przy wejściu na stronę.

Na dole sekcji: **Zobacz wszystkie realizacje** (link do `/realizacje`).

---

### 05 - Jak to działa

**Eyebrow:** PROCES
**H2:** PIĘĆ ETAPÓW. TWÓJ JEST JEDEN.

Layout: pozioma oś czasu na desktopie (5 kolumn połączonych linią `1px --line` z kropkami `--accent`), pionowa lista na mobile.

| Etap | Nagłówek | Treść |
|---|---|---|
| 01 | STRATEGIA I FORMAT | Ustalamy, po co Ci ten podcast i jak ma wyglądać. Kto prowadzi, jak długi jest odcinek, jaka jest oprawa, co ma się dziać po publikacji. Wychodzisz z tego etapu z planem na pierwsze [X] odcinków. |
| 02 | PRZYGOTOWANIE | Bierzemy na siebie kalendarz, kontakt z gośćmi i tematy. Dostajesz konspekt przed nagraniem, żeby wejść na plan przygotowany, a nie zaskoczony. |
| 03 | ZJAZD ZDJĘCIOWY | **Ten etap to Twój jedyny obowiązek.** Jeden dzień w studiu, w którym nagrywamy blok odcinków. Charakteryzacja, prompter, 3 kamery, realizator. Ty rozmawiasz. |
| 04 | POSTPRODUKCJA | Montaż, korekcja koloru, czyszczenie i mastering dźwięku, intro i outro, rolki pionowe z napisami. Dostajesz podgląd do akceptacji, nanosimy uwagi. |
| 05 | PUBLIKACJA | Wrzucamy odcinki na platformy, piszemy opisy i transkrypcje, przygotowujemy komplet materiałów na social media. Raportujemy, co się dzieje po publikacji. |

---

### 06 - Ile Cię to kosztuje czasu

Sekcja odpowiadająca na główną obiekcję B2B. Nikt na rynku jej nie ma.

**Eyebrow:** TWÓJ CZAS
**H2:** JEDEN DZIEŃ W MIESIĄCU. RESZTA JEST NASZA.

Layout: dwie kolumny. Lewa - poziomy wykres słupkowy podziału pracy. Prawa - lista.

**Wykres:** dwa słupki. `TY: [X] h` w kolorze `--accent`, `MY: [X] h` w `--surface-2` z obramowaniem. Wizualnie druzgocąca dysproporcja to jest cały przekaz.

**Lista po prawej - co jest po Twojej stronie:**
- Jeden dzień zdjęciowy w studiu
- Około [30] minut na akceptację konspektu
- Około [30] minut na uwagi do zmontowanych odcinków

**Pod spodem, mniejszym tekstem:**
> Wszystko poza tym - kalendarz, goście, sprzęt, montaż, rolki, opisy, publikacja - jest po naszej stronie. Jeśli chcesz mieć więcej kontroli, też da się to poukładać. Jeśli chcesz mieć jej mniej, też.

---

### 07 - Co dostajesz z jednego zjazdu

**Eyebrow:** JEDEN ZJAZD
**H2:** JEDEN DZIEŃ NA PLANIE, MIESIĄC CONTENTU

**Lead:**
> Nagrywamy blokiem. Zamiast czterech osobnych wizyt w studiu blokujesz jeden dzień i wychodzisz z materiałem na cały miesiąc.

Layout: 4 karty w rzędzie, każda z wielką liczbą.

| `[4]` | `[12]` | `[4]` | `[8]` |
|---|---|---|---|
| ODCINKI | ROLKI PIONOWE | OPISY I TRANSKRYPCJE | ZDJĘCIA Z SESJI |

Pod kartami tabela **co jest w cenie, a co dopłacasz** - dwie kolumny z ikonami. To bezpośrednia odpowiedź na największą pułapkę rynku: identycznie nazwane oferty znaczą co innego.

| W cenie | Dopłata |
|---|---|
| Nagranie, 3 kamery, realizator | Sound design i animacje |
| Montaż odcinka do [60] min | Odcinek dłuższy niż [60] min |
| Korekcja koloru i mastering audio | Koordynacja gości spoza Twojej sieci |
| Rolki pionowe z napisami | Dodatkowe rolki ponad pakiet |
| Opisy, tagi, transkrypcja | Zdjęcia produktowe |
| Publikacja na platformach | Kampania płatna |

---

### 08 - Formaty

**Eyebrow:** FORMATY
**H2:** CO MOŻEMY NAGRAĆ

Layout: 4 karty, w każdej miniatura ustawienia planu + specyfikacja.

| Format | Osoby | Kamery | Kadry | Sesja |
|---|---|---|---|---|
| **Wideopodcast** | 2 | 3 | 2x medium close-up + wide | [X] h |
| **Panel** | 3-4 | 4 | MCU na każdą osobę + wide | [X] h |
| **Solo / talking head** | 1 | 2 | medium shot + detal | [X] h |
| **Webinar i live** | 1-4 | 3 | realizacja na żywo, miks obrazu | [X] h |

Pod tabelą, mniejszym tekstem:
> Nagrywamy w ISO - każda kamera i każdy mikrofon na osobnej ścieżce. To znaczy, że w montażu da się uratować wszystko: kaszel, przejęzyczenie, dzwoniący telefon.

---

### 09 - Pakiety i cennik

**Eyebrow:** PAKIETY
**H2:** PAKIETY

**Lead:**
> Ceny są tutaj, bo nie mamy powodu ich chować. Poniżej jest wszystko, co wchodzi w każdy pakiet.

Layout: karta pilota na całą szerokość (wyróżniona obramowaniem `--accent`), pod nią 3 karty abonamentowe, środkowa oznaczona `NAJCZĘŚCIEJ WYBIERANY`.

**PILOT - `[X] zł`**
> Jeden odcinek od początku do końca, bez zobowiązań. Konsultacja formatu, nagranie, montaż, [3] rolki i rekomendacja, co dalej. Jeśli wchodzimy w serię, odliczamy tę kwotę od pierwszego miesiąca.

| | **START** | **SERIA** (rekomendowany) | **KANAŁ** |
|---|---|---|---|
| Cena | `[X] zł/mies.` | `[X] zł/mies.` | `[X] zł/mies.` |
| Odcinki | 2 | 4 | 8+ |
| Rolki pionowe | 6 | 12 | 24 |
| Opisy i transkrypcje | tak | tak | tak |
| Publikacja na platformach | - | tak | tak |
| Koordynacja gości | - | - | tak |
| Zdjęcia z sesji | - | tak | tak |
| Raport po publikacji | - | - | tak |
| Stały termin w kalendarzu | - | tak | tak |

Pod tabelą:
> Bez umów lojalnościowych. Okres wypowiedzenia: [1] miesiąc.
> Pojedynczy odcinek bez abonamentu: `[X] zł`.

**Uwaga do wypełnienia:** benchmark rynkowy to 949-990 zł za pojedynczy odcinek (Studio Makers, Three Dots) i 3200 / 6400 / 12 500 zł za abonamenty 2 / 4-6 / 8-12 odcinków (ArtBoyz). Poniżej tych progów nie mieści się nic poza montażem.

---

### 10 - Dlaczego my

**Eyebrow:** DLACZEGO MY
**H2:** SAMI TO ROBIMY

Layout: dwie kolumny. Lewa - tekst. Prawa - osadzony odcinek waszego podcastu lub zdjęcie z planu GSA.

**Treść:**
> [NAZWA/GSA] to nasz podcast. Nie jeden odcinek na pokaz, tylko [X] odcinków i [X] lat prowadzenia go tydzień po tygodniu.
>
> To znaczy, że wiemy rzeczy, których nie wie studio, które tylko wynajmuje salę: dlaczego gość odwołuje w ostatniej chwili, który fragment naprawdę wchodzi na rolkę, jak wygląda tytuł, który ktoś kliknie, i co się dzieje z odcinkiem w drugim i trzecim tygodniu po publikacji.
>
> Nie sprzedajemy Ci godzin w studiu. Sprzedajemy Ci to, czego sami się nauczyliśmy na własnym kanale.

---

### 11 - Studio

**Eyebrow:** STUDIO
**H2:** GDZIE TO POWSTAJE

Layout: galeria - jedno duże zdjęcie (8 kolumn) + siatka 4 mniejszych. Obok blok danych.

**Blok danych (mono labelki + wartości):**
- POWIERZCHNIA: `[X] m2`
- WYSOKOŚĆ: `[X] m`
- MAKS. OSÓB NA PLANIE: `[X]`
- REŻYSERKA: `[TAK / NIE]`
- KONFIGURACJE PLANU: `[X]`

**Zaplecze (ikony w rzędzie):** garderoba · charakteryzatornia · kuchnia · klimatyzacja · parking

**Dojazd:**
> `[ADRES]`. `[X]` minut pieszo od `[metro/przystanek]`, `[X]` miejsc parkingowych na miejscu.

Konkurencja mierzy dojazd w minutach i wypisuje numery autobusów. To działa, bo znosi realną obiekcję.

---

### 12 - Specyfikacja techniczna

**Eyebrow:** SPRZĘT
**H2:** SPRZĘT

Akordeon, domyślnie zwinięty, żeby nie przytłaczał. Otwierają go ci, którzy porównują oferty - i właśnie dla nich musi tu być komplet modeli.

- **Obraz:** `[X]x [model kamery]`, obiektywy `[modele]`, switcher `[model]`, rejestracja ISO na osobnych ścieżkach
- **Dźwięk:** `[X]x [model mikrofonu]`, interfejs `[model]`, rejestrator `[model]`, mastering
- **Światło:** `[X]x [model]`, schemat 3-punktowy, standaryzowany dla wszystkich osób na planie
- **Dodatki:** prompter `[X]"`, monitor podglądowy, TV `[X]"` na grafiki
- **Formaty wyjściowe:** 4K i 1080p poziom, 1080x1920 pion, mp3, transkrypcja `.srt` i `.txt`

**Zasada:** tu wpisujemy wyłącznie to, co realnie macie. Klienci porównują modele, a rozbieżność wychodzi na pierwszym nagraniu.

---

### 13 - Zespół

**Eyebrow:** ZESPÓŁ
**H2:** KTO PRZY TYM PRACUJE

Przy abonamencie klient kupuje ludzi, nie sprzęt. Karty: zdjęcie, imię i nazwisko, rola, jedno zdanie.

Minimum: kto prowadzi projekt, kto realizuje na planie, kto montuje.

---

### 14 - Opinie

**Eyebrow:** OPINIE
**H2:** CO MÓWIĄ

3 karty: cytat, imię i nazwisko, funkcja i firma, opcjonalnie zdjęcie. Anonimowe gwiazdki nie działają - najlepsze studia w tej kategorii pokazują konkretne nazwiska z funkcjami.

Jeśli nie ma jeszcze opinii, sekcja wypada. Nie wstawiać wymyślonych.

---

### 15 - FAQ

**Eyebrow:** FAQ
**H2:** PYTANIA, KTÓRE PADAJĄ ZAWSZE

Akordeon, 10 pozycji:

1. Ile mojego czasu to realnie zajmuje w miesiącu?
2. Co jeśli nie mam pomysłu na format?
3. Kto wymyśla tematy i kto załatwia gości?
4. Do kogo należą pliki i materiały?
5. Ile trwa od nagrania do publikacji?
6. Co jeśli gość odwoła albo nagranie się nie uda?
7. Czy mogę zacząć od jednego odcinka?
8. Na jak długo się wiążę?
9. Czy zajmujecie się publikacją i opisami?
10. Skąd wiem, że to działa - co mierzycie?

---

### 16 - Kontakt

**Eyebrow:** KONTAKT
**H2:** ZACZNIJMY OD ROZMOWY

Layout: dwie kolumny. Lewa - formularz. Prawa - dane kontaktowe, zdjęcie zespołu, mapa.

**Formularz kwalifikujący** (nie kalendarz rezerwacji studia - to inny model):
- Imię i nazwisko
- Firma
- E-mail, telefon
- `Na jakim jesteś etapie?` - select: mam pomysł / mam podcast i chcę go przenieść / chcę zacząć, ale nie wiem od czego
- `Ile odcinków miesięcznie?` - select: 1-2 / 3-4 / 5+ / nie wiem
- Wiadomość
- Checkbox RODO

**Obietnica pod przyciskiem:**
> Odpowiadamy w ciągu [24] godzin roboczych. Pierwsza rozmowa jest bezpłatna i trwa około 30 minut.

---

### 17 - Stopka

4 kolumny: logo i jedno zdanie / nawigacja / usługi (linki do podstron) / kontakt i adres z mapą.

Dół: NIP `[X]`, polityka prywatności, regulamin, polityka anulacji, social.

---

## CZĘŚĆ III - PODSTRONY I SEO

Ta część była szkicem i została zastąpiona przez trzy osobne dokumenty, zbudowane po analizie danych Senuto i weryfikacji blogów konkurencji:

- **[SITEMAP-I-TRESCI.md](SITEMAP-I-TRESCI.md)** - model 8 warstw treści, pełna sitemap z rozpisaną zawartością każdej zakładki, konwencje URL, linkowanie wewnętrzne
- **[PLAN-SEO-AEO-GEO.md](PLAN-SEO-AEO-GEO.md)** - on-page, techniczne, mapa schema, lokalne SEO Warszawa, GEO generatywne i monitoring cytowań w AI
- **[30-ARTYKULOW.md](30-ARTYKULOW.md)** - 30 artykułów w 6 klastrach z frazami, priorytetami i wzorcem artykułu
- **[FAQ-BAZA.md](FAQ-BAZA.md)** - 36 pytań w 7 grupach, gotowych pod `FAQPage`

Najważniejsze zmiany wobec pierwotnego szkicu:

1. **Zakres zawężony do 3 filarów:** wideopodcast, rolki/shorty/talking head, nagrania szkoleniowe i kursy online. Webinary i transmisje live wypadły z oferty, więc `/webinary-i-transmisje-live` nie powstaje.
2. **Doszły dwie strony, których nie było w szkicu:** `/sprzet/` (pełna specyfikacja, nikt na rynku tego nie ma) i `/faq/` jako osobny URL pod AEO.
3. **`/studio/` dostaje trzy podstrony aranżacji** na wzór `/space/[nazwa]` u Studio Miś.
4. **Bez stron pod dzielnice** - wolumen zerowy, a Google traktuje je jak doorway pages.

### Techniczne

- Statyczny HTML albo Astro. Bez CMS-a na start.
- `Schema.org`: `LocalBusiness` + `Service` + `FAQPage` + `VideoObject` przy odcinkach
- Open Graph z kadrem ze studia
- Lighthouse: wideo w hero z `preload="none"` i posterem, obrazy w `webp` z `loading="lazy"`, fonty lokalnie z `font-display: swap`
- Formularz: `[FormSubmit / własny endpoint]`
- Analityka: GA4 + zdarzenia na kliknięcie CTA, wysłanie formularza i odtworzenie odcinka

---

## CZĘŚĆ IV - BRIEF FOTOGRAFICZNY

Strona stoi na zdjęciach. Poniżej reguły wyprowadzone z analizy kadrów Studio Miś, które są na tym rynku najlepsze, złożone z ciemną, kinową paletą decku GSA. To nie są dwa sprzeczne kierunki - ich kadry są ciepłe i ciemne po bokach, dokładnie jak ciemne slajdy Waszego decku.

### Reguły kadru

1. **Frontalnie i symetrycznie.** Ściana tła równolegle do matrycy, punkt zbiegu na środku kadru. Żadnych ujęć z ukosa - to jest znak rozpoznawczy tanich zdjęć wynajmowych.
2. **Jeden mocny element w centrum.** Podświetlone koło, ekran, panel akustyczny, lampa - coś, na czym kadr się trzyma. Jeśli scenografia takiego elementu nie ma, trzeba go dobudować przed sesją zdjęciową.
3. **Zero ludzi na zdjęciach przestrzeni.** Ludzie są w kadrach z nagrania i w sekcji zespołu. Przestrzeń fotografujemy pustą, jak wnętrze do katalogu.
4. **Światło w kadrze.** Lampy i podświetlenia mają być widoczne jako element scenografii, nie tylko oświetlać. To buduje wrażenie, że przestrzeń świeci sama.
5. **Sufit i osprzęt zostają w kadrze.** Czarna konstrukcja, zawieszone lampy, mikrofony na wysięgnikach. To odróżnia studio od ładnego salonu.
6. **Ciemne krawędzie, jaśniejszy środek.** Naturalna winieta prowadząca wzrok. Zgodna z poświatą z ciemnych slajdów decku.
7. **Jeden dominujący kolor na aranżację.** Każde ustawienie planu ma być rozpoznawalne po kolorze na miniaturze wielkości znaczka pocztowego.
8. **Jeden format we wszystkich kaflach.** Rekomendacja: `16:9` dla kart odcinków (zgodnie z kartami gości w decku) i `3:2` dla kadrów przestrzeni.

### Lista ujęć do sesji

**Przestrzeń (bez ludzi), na każdą aranżację planu:**
- 1x kadr główny, frontalny, symetryczny, na wysokości oczu siedzącej osoby
- 1x kadr szeroki pokazujący sufit i osprzęt
- 1x detal: mikrofon, lampa, faktura tła
- 1x kadr z pozycji kamery - dokładnie to, co zobaczy widz w gotowym odcinku

**Plan w akcji (z ludźmi):**
- 1x nagranie z boku, widoczne kamery, światło i dwie osoby przy mikrofonach
- 1x realizator przy monitorach w reżyserce
- 1x szeroki kadr całego planu z góry albo z tyłu

**Do sekcji zespołu:**
- portrety wycięte z tła, na ciemnym - jak Oskar na okładce decku. Nie kadrowane prostokąty.

**Do kart odcinków:**
- klatki wprost z nagrań, `16:9`, kadr medium close-up rozmówcy - dokładnie jak karty gości w decku GSA

### Czego unikać

- Zdjęć z ukosa i „na luzie" telefonem
- Pustych, jasnych, przesadnie doświetlonych kadrów - to zabija kinowy charakter, który macie w decku
- Kolażu z wielu różnych sesji o niespójnym balansie bieli. Jedna sesja, jeden fotograf, jedna obróbka
- Stocku. Ani jednego zdjęcia stockowego na tej stronie

---

## CZĘŚĆ V - CZEGO BRAKUJE, ŻEBY TO ZBUDOWAĆ

Bez pozycji 1-3 strona nie ma czym przekonywać.

1. **3-6 gotowych materiałów wideo** do sekcji 04 - to jest jedyna przewaga, której konkurencja nie ma
2. **Zdjęcia studia** - szeroki plan, detal sprzętu, plan podczas nagrania, zaplecze
3. **Realna specyfikacja sprzętu** - modele i liczby
4. Nazwa i logo studia oraz decyzja, czy działa pod marką GSA
5. Adres, czas dojścia od metra, liczba miejsc parkingowych
6. Metraż, wysokość, pojemność, czy jest osobna reżyserka
7. Ceny pakietów albo widełki
8. Realny czas dostawy: surówka i zmontowany odcinek
9. Zdjęcia zespołu i role
10. Opinie od pierwszych klientów - do zebrania od razu po pierwszych realizacjach
