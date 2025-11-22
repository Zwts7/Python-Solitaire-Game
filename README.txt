Sposób uruchomienia:

Wypakuj zawartość pliku 16-18_Python_Marcin_Radzewicz.rar w dogodne dla siebie miejsce, w środku pliku powinien znajdować się tylko folder o nazwie: 16-18_Python_Marcin_Radzewicz, to w nim znajdują się wszystkie pliki, należy sprawdzić czy pliki w folderze działają poprawnie(otworzyć, zobaczyć czy nie są puste, zamknąć bez zapisywania).

v

Otwórz nowo wypakowany folder i upewnij się, że są tam pliki: 
- Pasjans.py
- ranking.txt
- README.txt
- zasady.txt
- requirements.txt

v

Upewnij się, że masz zainstalowanego Python'a (wersja na której testowałem program: 3.13.3)(W wierszu poleceń napisz polecenie: python).

v 2 metody uruchomienia samego programu:

=====================

1.v

Otwórz terminal w folderze projektu (opcja1: Używając wiersz poleceń, przejdź do tego folderu komendą cd | opcja2: Mając otwarty folder, w którym znajduje się projekt, w ścieżce fizycznej należy wpisać CMD, wiersz poleceń powinien otworzyć się z lokalizacją w tym folderze).

1.v

W wierszu poleceń z otwartą lokalizacją folderu projektu wpisujemy polecenie:

1.v

python Pasjans.py

=====================

2.v

Uruchom program Pasjans.py w aplikacji umożliwiającej edycję i uruchamianie kodu Pythona, takiej jak Visual Studio Code (VSC) lub inny edytor z obsługą Pythona.

2.v

W wybranej aplikacji uruchom program w terminalu.

=====================

Instrukcja rozgrywki:

Gra uruchamia się w trybie konsolowym i wyświetla menu opcji:

[1] Rozpoczęcie gry
[2] Zasady gry
[3] Opis symboli kart
[4] Wyświetl przetasowaną talię
[0] Ustawienia

Należy wpisać wybraną opcję według przypisanej do niej cyfry np. [1] "Rozpoczęcie gry".
Opcja "Ustawienia" pojawia się wiele razy, to w niej możemy opuścić grę lub zacząć ją od nowa.

Tryb gry:
Gra posiada dwa poziomy trudności: 

-Łatwy - Na tym poziomie dobiera się tylko po 1 karcie do talii.
-Trudny - Na tym poziomie dobiera się po 3 karty do talii.

Po rozpoczęciu gry widoczny jest interfejs z kolumnami kart i stosem.

Gracz może wykonywać akcje, wybierając z menu:

[1] Przenieś kartę lub zbiór kart między kolumnami
[2] Przenieś kartę na stos docelowy
[3] Przetasuj kartę z talii
[4] Dobierz kartę z talii
[5] Cofnij ruch (max 3 ruchy)
[0] Ustawienia (zakończenie / restart)

Sterowanie:
Wszystko odbywa się przez wpisywanie cyfr i zatwierdzanie Enterem.

Komunikaty błędów/wskazówki wyświetlane są automatycznie po nieprawidłowym ruchu.

Gra kończy się wygraną, gdy wszystkie karty zostaną przeniesione na stosy końcowe.

Gracz może przegrać, jeżeli nie będzie już możliwych ruchów, wtedy pozostaje nam tylko poddanie się.

=====================