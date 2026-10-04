# Decyzje i dane - wrzesień 2026

Dokument nadrzędny wobec sierpniowych plików w tym katalogu. Tam, gdzie się rozjeżdżają, obowiązuje ten.

Stan wyjściowy: repo `kazekdaniel-lab/gsa-studio`, ostatni commit `0e0694f` z 11 sierpnia 2026. Lokalnie i na GitHubie identycznie, jedna gałąź `main`, podgląd na GitHub Pages. To jest najnowszy design i on jest podstawą dalszej pracy.

---

## 1. Cztery decyzje

| Temat | Decyzja | Co z tego wynika |
|---|---|---|
| Marka | GSA Studio, ale na **osobnej domenie** | Transfer autorytetu z podcastu zostaje, a treści studia nie konkurują w wynikach z treściami podcastowymi. Domena do ustalenia - w generatorze siedzi w jednej stałej `DOMENA` |
| Ceny | **Jak na stronie konkurencji**, do której odsyła brief | Strona ofertowa bez kwot, wycena na rozmowie, pytanie o koszt odbite w FAQ. Kwoty rynkowe wolno podawać w artykułach, bo to fakty o rynku, a nie nasz cennik |
| Zakres merytoryczny | **Pomagamy ułożyć, ale klient przychodzi z konkretem** | Nie obiecujemy, że wymyślimy za kogoś, o czym ma mówić. Układamy z jego wiedzy format, kolejność i plan. To jest osobna sekcja na stronie, nie przypis |
| Materiały | Odcinki GSA, zdjęcia studia i twarde dane **są po stronie klienta**; czego brakuje, to placeholder | Kadry wchodzą w gotowe sloty bez przebudowy układu |

### Rozwinięcie decyzji o zakresie

To jest jednocześnie najmocniejszy wyróżnik wobec konkurencji, więc warto go nazwać precyzyjnie.

Konkurent obiecuje: audyt, strategię, research tematów, filary treści i konspekty. Czyli że wymyśli za klienta, o czym ma mówić.

My mówimy inaczej: **z tego, co przyniesiesz, ułożymy format, kolejność i plan zjazdów. Nie wymyślimy za Ciebie, na czym się znasz.** Klient musi wejść z konkretem - wiedzą, sprawami z rynku, realnymi pytaniami klientów. Bez tego nie da się pracować po ludzku, a nie tylko formalnie.

Konsekwencja dla copy: żadnego „bierzemy na siebie tematy". Zamiast tego rozdzielone wprost: co przynosisz Ty, co układamy my.

---

## 2. Dane wyszukiwań - Senuto, wrzesień 2026

Pobrane bezpośrednio z API, baza polska (`country_id` 1). To jest korekta wobec planu sierpniowego, który opierał się na eksporcie wokół seeda „studio nagrań".

### Frazy, na których stoi biznes

| Fraza | Wyszukiwania /mies. | CPC |
|---|---|---|
| studio podcastowe warszawa | 320 | 34,53 zł |
| podcast studio | 260 | 6,77 zł |
| studio do podcastów | 70 | 4,08 zł |
| studio podcastowe warszawa cennik | 20 | 6,00 zł |
| produkcja wideo warszawa | 20 | 25,17 zł |
| podcast firmowy | 20 | 0 zł |

CPC 34,53 zł przy frazie głównej mówi więcej niż wolumen. Przy 320 wyszukiwaniach to jest najdroższe słowo w całej okolicy, bo za jednym zapytaniem stoi kontrakt, a nie ciekawość.

### Trzy ustalenia, które zmieniają plan

**1. Strona konkurencji, do której odsyła brief, nie jest stroną SEO.** Fraza „prowadzenie kanału youtube" nie ma w Senuto mierzalnego wolumenu. Cały klaster „youtube dla firm" to zapytania poradnikowe w rodzaju „jak założyć kanał na youtube" (1000/mies.), czyli ruch osób, które chcą zrobić to same. Komercyjne są tylko resztki: „agencje youtube" 30/mies., „agencja reklamowa youtube" 10/mies.

Wniosek: ich strona jest materiałem sprzedażowym, na który wchodzi się z reklamy, z maila albo z rozmowy. Nasza odpowiednia strona ma pełnić tę samą rolę, a ciężar SEO zostaje na frazie studiowej i na ogonie poradnikowym.

**2. „Rolki" to pułapka.** Samo słowo ma 40 500 wyszukiwań miesięcznie i dotyczy wrotek. „rolki dla dzieci" 9900, „rolki dla dziewczynki" 4400. Filar drugi nie może celować w „produkcja rolek warszawa", bo walczy z branżą sportową. Fraza musi zawierać kontekst: krótkie formy pionowe, shorty z podcastu, materiały na social media.

**3. Klaster nagraniowy jest poradnikowy, nie zakupowy.** „mikrofony do podcastów" 720/mies., „jak nagrać podcast" 260/mies., „jak nagrywać podcasty" 210/mies. To są ludzie, którzy chcą nagrywać sami. Dobry materiał na bloga i na cytowania w modelach, zły jako cel strony usługowej.

Dla porównania cała gałąź muzyczna: „studia nagraniowe" 2900, „studia nagraniowe warszawa" 1300, „studio nagrań warszawa" 1000, „sala prób warszawa" 480. Duży ruch, inny klient, nie wchodzimy - potwierdzenie decyzji z sierpnia.

**Czego nie udało się pobrać:** `get_questions` w Senuto zwraca zero wyników dla wszystkich naszych seedów. Baza pytań zostaje więc na tym, co mamy z researchu konkurencji i z `FAQ-BAZA.md`.

---

## 3. Konkurencja - co realnie ma na stronie

Źródło: `podcastwarszawa.pl/youtube-dla-firm` oraz sekcja cennika na ich stronie głównej, odczytane 20 września 2026.

**Ich cennik jest jawny, ale dotyczy wynajmu, nie prowadzenia kanału:**

| Pozycja | Cena |
|---|---|
| Wynajem studia do 2 albo 4 godzin | 1220 albo 1500 zł netto |
| Wynajem studia do 8 godzin | 2000 zł netto |
| Montaż odcinka do 60 minut | 900 zł netto |
| Trzy najlepsze fragmenty | 450 zł netto |

Wynajem tylko w blokach 2, 4 albo 8 godzin, dni robocze 9:00-17:00. Przy ofercie prowadzenia kanału kwoty nie ma - jest bezpłatna konsultacja 30 minut przez Calendesk i pytanie „Ile kosztuje współpraca?" w FAQ.

**Co mają mocnego:** liczby w pierwszym ekranie (15 lat, 200 tys. subskrybentów, ponad 1000 filmów, 100 m2 na Mokotowie), dwa imienne case studies z wynikiem, sekcja „to nie jest dobre rozwiązanie, jeśli", jednoznaczny podział odpowiedzialności, konkret ilościowy (4 długie filmy miesięcznie).

**Czego nie mają:** poziomów wejścia - jest jeden abonament albo nic. Brak specyfikacji technicznej. Brak informacji, jakie pliki klient dostaje. Strona zbudowana w Framerze wygląda jak każda druga strona zbudowana w Framerze.

**Czego nie udało się odczytać:** rozwinięć ich FAQ. Akordeon nie otwiera się skryptem, a treści nie ma w kodzie strony. Mam same pytania.

---

## 4. Co z tego wynika dla architektury

1. **Nowa strona flagowa `/prowadzenie-kanalu/`** - trzy poziomy wejścia zamiast jednego abonamentu. Rola sprzedażowa, nie ruchowa: link z maila, z rozmowy, z reklamy.
2. **Ciężar SEO zostaje** na `/` i `/produkcja-podcastow-warszawa/` pod frazę studiową oraz na blogu pod ogon poradnikowy.
3. **Filar drugi dostaje inną frazę** - bez samego słowa „rolki".
4. **Audyt w generatorze przestaje być zerojedynkowy.** Zamiast wycinać każde „zł" z całego serwisu, blokuje kwoty na stronach ofertowych i dopuszcza je w artykułach. Inaczej tekst „ile kosztuje nagranie wideopodcastu" nie ma czym rankować ani czego zacytować.

---

## 5. Czego brakuje do publikacji

Bez pozycji 1-3 strona nadal jest szkieletem, choćby była najlepiej zaprojektowana.

1. **Zdjęcia studia w Warszawie** - kadr główny, plan w akcji, aranżacje, detal sprzętu. Reguły kadru w `PROJEKT-STRONY.md`, część IV
2. **Twarde dane** - adres, metraż, wysokość, liczba osób na planie, dojście od metra, modele kamer i mikrofonów
3. **Domena docelowa** - jedna stała w `build.py`, zmiana w jednym miejscu
4. Telefon i e-mail kontaktowy
5. Opinie od pierwszych klientów, do zebrania po pierwszych realizacjach

Materiał wideo jest - 72 odcinki podcastu GSA z identyfikatorami YouTube. Wchodzą na stronę jako dowód.

---

## 6a. Zwrot wizualny i treściowy, październik 2026 (obowiązuje)

Kierunek „druk produkcyjny" z sekcji 6 jest **nieaktualny**. Został odrzucony razem z poprzednim, ciemnym. Obowiązuje:

| Element | Stan |
|---|---|
| Tło | `#FBFBF9`, ciche sekcje `#EDEEEA` |
| Tekst i pasma ciemne | `#15161A`, tekst drugorzędny `#54585C` |
| Jedyny kolor | `#0F3D32`, na ciemnym `#79D0B2`. **Zakaz palety GSA** (`#FF5900` i pochodne) |
| Linia | `#A6AAA3` 1 px, `#15161A` 2 px między sekcjami |
| Krój | General Sans (Fontshare, ITF FFL): nagłówki 500, tekst 400. JetBrains Mono wyłącznie na nazwy plików i sloty |
| Motyw | rozkład miesiąca: wąski odcinek dnia zdjęciowego i szeroki odcinek 30 dni, przez które ten materiał wychodzi |

Oś treści: **jeden dzień zdjęciowy daje materiał na cały miesiąc**. Publikacja nie jest główną wartością, bo przy pojedynczym odcinku i przy serii wrzuca klient. Własny kanał GSA (72 odcinki) stoi jako dowód kompetencji, nie jako główny argument. Rozstrzygnięcia: `USP-2026-10.md`, treść: `COPY-HERO-2026-10.md`.

---

## 6. Zwrot wizualny - 21 września 2026 (NIEAKTUALNE od 10.2026, patrz sekcja 6a)

Poprzedni kierunek (ciemna baza, jeden nasycony akcent, poświata radialna, ziarno, mono-nadtytuły, ciasny ujemny tracking) został **odrzucony jako AI slop**. Diagnoza nie była przeczuciem: ta estetyka, znana jako styl Linear / Vercel / Raycast, jest dziś domyślnym wyjściem generatorów kodu, bo dane treningowe z lat 2021-2024 przeważają w stronę landingów spod YC.

Sprawdzone znaczniki, które mieliśmy u siebie: krój tekstowy rozciągnięty do display, ciemne tło z poświatą, mono wersaliki jako nadtytuły, jeden promień i padding wszędzie, fade na każdej sekcji, puste ramki zamiast zdjęć.

### Nowy kierunek: druk produkcyjny

Baza to arkusz papieru, tusz jest akcentem. Strona ma wyglądać jak dokument produkcyjny, czyli jak to, co klient realnie od nas dostaje, a nie jak strona SaaS.

| Zasada | Wykonanie |
|---|---|
| Zero zaokrągleń | `*,*::before,*::after{border-radius:0}` bez wyjątków |
| Zero cieni i poświat | strukturę niesie kreska, nie rozmycie |
| Papier jako baza | `.light` to arkusz, `.canvas` to pasmo w tuszu, `.dark` to drugi ton arkusza |
| Jeden kolor | stempel `#B03A00` na papierze, `#FF5900` na tuszu |
| Szeryf tylko na display | Instrument Serif 400 na H1, H2 i liczby. Nigdy na przyciski, nawigację i treść |
| Ruch tylko tam, gdzie coś znaczy | jedno odsłonięcie przy wejściu w kadr, bez przesunięć |

### Kroje

| Rola | Krój | Uzasadnienie |
|---|---|---|
| Display | **Instrument Serif** 400 + kursywa | wybrany z trzech wariantów pokazanych obok siebie; waga 400 bez pogrubienia, bo elegancja siedzi w rysunku kroju, nie w grubości |
| Tekst | **Archivo** 400 / 500 / 600 | workhorse gazetowy, nie jest domyślnym wyborem generatorów |
| Warstwa techniczna | **JetBrains Mono** 500 / 800 | etykiety, dane, przyciski, metryka arkusza |

Plus Jakarta Sans usunięty z repo. Wszystkie kroje lokalnie w `assets/fonts/`, zero zapytań do zewnętrznych serwerów.

### Elementy, których generator sam nie zaproponuje

Pasek metryki arkusza w nagłówku, marginalia w bocznej kolumnie, dane liczbowe rozpisane jak w arkuszu dostawy, wykaz z wodzidłem z kropek, matryca zakresu jako księga z rzymskimi numerami kolumn, numeracja etapów rzymska w szeryfie, pasma poziomów rosnące wcięciem zamiast ciemnością.

### Kontrast po zmianie

Wszystkie pary przechodzą WCAG AA i są pilnowane w buildzie: tusz na papierze 16,81:1, tekst drugorzędny 9,12:1, stempel na papierze 4,68:1 i na drugim tonie arkusza 5,04:1, papier na tuszu 16,81:1, stempel jasny na tuszu 5,92:1. Kreska druku ma osobny próg 2,2:1, bo jest separatorem, a nie nośnikiem treści.

### Źródła diagnozy

- [925studios, AI Slop Web Design Guide 2026](https://www.925studios.co/blog/ai-slop-web-design-guide)
- [uxskill, why every AI-built site looks the same](https://uxskill.laithjunaidy.com/blog/ai-built-website-no-slop.html)
- [Studio Maydit, why your AI startup looks generic](https://studiomaydit.com/blog/why-your-ai-startup-looks-generic)
- [ui-ux-pro-max, 7 techniques against AI slop](https://ui-ux-pro-max-skill.com/blog/avoiding-ai-slop/)
- [Fireart, brutalist UX 2026](https://fireart.studio/blog/the-best-web-design-trends/)
