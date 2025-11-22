# -*- coding: utf-8 -*-
import random
from colorama import Fore, Style, init #Musiałem zdecydować się na colorama ponieważ podstawowy zapis kolorów w ANSI nie zawsze działa poprawnie.
init()



INFORMACJA = ""
KIER = [" A♥", " 2♥", " 3♥", " 4♥", " 5♥", " 6♥", " 7♥", " 8♥", " 9♥", "10♥", " J♥", " Q♥", " K♥"] # ♥
KARO = [" A♦", " 2♦", " 3♦", " 4♦", " 5♦", " 6♦", " 7♦", " 8♦", " 9♦", "10♦", " J♦", " Q♦", " K♦"] # ♦
PIK =  [" A♠", " 2♠", " 3♠", " 4♠", " 5♠", " 6♠", " 7♠", " 8♠", " 9♠", "10♠", " J♠", " Q♠", " K♠"] # ♠
TREFL =[" A♣", " 2♣", " 3♣", " 4♣", " 5♣", " 6♣", " 7♣", " 8♣", " 9♣", "10♣", " J♣", " Q♣", " K♣"] # ♣
LIBCZA_KOLUMN = 7
MAX_COFNIEC = 3
WARTOSC_KROLA = 13
POZIOM_LATWY = 1
POZIOM_TRUDNY = 2
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
PURPLE = Fore.MAGENTA
CYAN = Fore.CYAN
RESET = Fore.WHITE
KOPIA_1 = {}
KOPIA_2 = {}
KOPIA_3 = {}



def Reset(): #Resetuje wszystkie zmienne, aby można było grać od nowa.
    global TALIA_KART,KOLUMNY,KOLUMNY_UKRYTE,STOS_KARO,STOS_KIER,STOS_PIK,STOS_TREFL,KARTY_ZAPASOWE,ILE_KART_STOS_KARO,ILE_KART_STOS_KIER,ILE_KART_STOS_PIK,ILE_KART_STOS_TREFL,LICZBA_RUCHOW,IMIE,POZIOM_TRUDNOSCI,TALIA_AKTYWNA,NAZWY_WSZYSTKIEGO,LICZBA_AKTYWNYCH_KOPII
    KARTY_ZAPASOWE = 0
    ILE_KART_STOS_KIER = 0
    ILE_KART_STOS_KARO = 0
    ILE_KART_STOS_PIK = 0
    ILE_KART_STOS_TREFL = 0
    LICZBA_RUCHOW = 0
    IMIE = ""
    TALIA_KART = KIER + KARO + PIK + TREFL
    random.shuffle(TALIA_KART)
    KOLUMNY = [[] for _ in range(LIBCZA_KOLUMN)]
    KOLUMNY_UKRYTE = [[] for _ in range(LIBCZA_KOLUMN)]
    STOS_KIER = []
    STOS_KARO = []
    STOS_PIK = []
    STOS_TREFL = []
    POZIOM_TRUDNOSCI = 0
    TALIA_AKTYWNA = []
    NAZWY_WSZYSTKIEGO = ["KARTY_ZAPASOWE", "ILE_KART_STOS_KIER", "ILE_KART_STOS_KARO", "ILE_KART_STOS_PIK", "ILE_KART_STOS_TREFL","LICZBA_RUCHOW", "TALIA_KART", "KOLUMNY", "KOLUMNY_UKRYTE","STOS_KARO", "STOS_KIER", "STOS_PIK", "STOS_TREFL", "TALIA_AKTYWNA"]
    LICZBA_AKTYWNYCH_KOPII = 0



def Opcje(): #Menu główne, w którym można rozpocząć grę, zobaczyć zasady, opisy symboli kart lub przetasowaną talię.
    global INFORMACJA
    Reset()
    print(Style.BRIGHT)
    Wyczysc()
    Nazwa()
    Wskazowka()
    try:
        opcja = int(input(f"\n{GREEN}[1 = Rozpoczęcie gry] \n{YELLOW}[2 = Zasady gry] \n{RED}[3 = Opis symboli kart] \n{BLUE}[4 = Pokaż przykład przetasowanej talii]\n{PURPLE}[0 = Ustawienia]{RESET}\nOpcje: "))
    except ValueError:
        INFORMACJA = "Błędne dane wejściowe"
        Opcje()
    if opcja == 1:
        Poziom()
    elif opcja == 2:
        Wyczysc()
        Zasady()
        input("\nNaciśnij ENTER aby kontynuować: ")
        Opcje()
    elif opcja == 3:
        Wyczysc()
        Opis_symboli_kart()
        input("\nNaciśnij ENTER aby kontynuować: ")
        Opcje()
    elif opcja == 4:
        Wyczysc()
        Przetasowana_talia()
        input("\n\nNaciśnij ENTER aby kontynuować: ")
        Opcje()
    elif opcja == 0:
        Koniec()
    else:
        INFORMACJA = (f"Opcja numer: {opcja}, nie istnieje.")
        Opcje()



def Koniec(): #Menu końcowe, w którym można wyjść lub rozpocząć grę od nowa.
    global INFORMACJA
    Wyczysc()
    Wskazowka()
    try:
        opcja_koniec = int(input(f"\n{GREEN}[1 = Rozpocznij grę od nowa] \n{RED}[2 = Wyjdź] \n{YELLOW}[3 = Powrót do gry]{RESET} \nOpcje: "))
    except ValueError:
        INFORMACJA=("Błędne dane wejściowe")
        Koniec()
    if opcja_koniec == 1:
        Opcje()
    elif opcja_koniec == 2:
        print("\nAdiós")
        exit()
    elif opcja_koniec == 3:
        if POZIOM_TRUDNOSCI == 1 or POZIOM_TRUDNOSCI == 2:
            Wybor()
        else:
            INFORMACJA = "Obecnie nie ma zapisu, do którego można powrócić."
            Opcje()
    else:
        INFORMACJA = (f"Opcja numer: {opcja_koniec}, nie istnieje.")
        Koniec()



def Poziom(): #Menu wyboru poziomu trudnośći.
    global POZIOM_TRUDNOSCI, INFORMACJA, TRUDNOSC
    Wyczysc()
    Wskazowka()
    try:
        POZIOM_TRUDNOSCI = int(input(f"\n{GREEN}[1 = Łatwy (Dobiera się po 1 karcie)] \n{RED}[2 = Trudny (Dobiera się po 3 karty)]\n{PURPLE}[0 = Ustawienia]{RESET}\nWybierz poziom trudnośći: "))
    except ValueError:
        INFORMACJA = "Błędne dane wejściowe"
        Poziom()
    if POZIOM_TRUDNOSCI == POZIOM_LATWY:
        TRUDNOSC = 1
        INFORMACJA = ("Wybrano poziom Łatwy.")
        Kolumny()
        Wybor()
    elif POZIOM_TRUDNOSCI == POZIOM_TRUDNY:
        TRUDNOSC = 3
        INFORMACJA = ("Wybrano poziom Trudny.")
        Kolumny()
        Wybor()
    elif POZIOM_TRUDNOSCI == 0:
        Koniec()
    else:
        INFORMACJA = f"Opcja numer: {POZIOM_TRUDNOSCI}, nie istnieje."
        Poziom()



def Kolumny(): #Rozdaje talię, na kolumny i talie zapasową.
    liczba_kart_w_kolumnie=0
    for kolumna in range(LIBCZA_KOLUMN):
        liczba_kart_w_kolumnie+=1
        odkryta_karta=1
        for _ in range(liczba_kart_w_kolumnie):
            if odkryta_karta == 1:
                KOLUMNY[kolumna].append(TALIA_KART.pop(0))
                odkryta_karta -= 1
            elif odkryta_karta != 1:
                KOLUMNY_UKRYTE[kolumna].append(TALIA_KART.pop(0))



def HUD(): #Wyświetla aktualny stan gry: kolumny, talię, stosy, liczbę ruchów.
    Wyczysc()
    print(f"Karty:                   | Liczba ruchów: {LICZBA_RUCHOW}")
    Pokaz_kolumny()
    Pokaz_talie()
    print(f"Stos kier  |{RED+"♥"+RESET}|:",end = "")
    Pokaz_stos(STOS_KIER)
    print(f"Stos karo  |{RED+"♦"+RESET}|:",end = "")
    Pokaz_stos(STOS_KARO)
    print("Stos pik   |♠|:",end = "")
    Pokaz_stos(STOS_PIK)
    print("Stos trefl |♣|:",end = "")
    Pokaz_stos(STOS_TREFL)



def Stosy(): #Pozwala na przenoszenie kart na stosy końcowe.
    global INFORMACJA,LICZBA_RUCHOW,ILE_KART_STOS_KIER,ILE_KART_STOS_KARO,ILE_KART_STOS_PIK,ILE_KART_STOS_TREFL
    HUD()
    try:
        karta_kolumna = int(input("\nZ której kolumny przenieść kartę na stos (karta z talii = 8): "))
    except ValueError:
        INFORMACJA = "Błędne dane wejściowe"
        LICZBA_RUCHOW -= 1
        Wybor()
    if karta_kolumna <=0:
        INFORMACJA =f"Nie ma kolumny numer: {karta_kolumna}"
        Wybor()
    if karta_kolumna in range(LIBCZA_KOLUMN+1):
        if KOLUMNY[karta_kolumna-1]:
            karta = KOLUMNY[karta_kolumna-1][0]
        else:
            INFORMACJA = f"Kolumna {karta_kolumna} jest pusta."
            LICZBA_RUCHOW-=1
            Wybor()
    elif karta_kolumna == 8:
        if TALIA_AKTYWNA:
            karta = TALIA_AKTYWNA[-1]
        else:
            INFORMACJA = "Talia jest pusta."
            LICZBA_RUCHOW-=1
            Wybor()
    else:
        INFORMACJA = (f"Nie ma kolumny numer: {karta_kolumna}")
        LICZBA_RUCHOW -= 1
        Wybor()
    if karta[-1] == "♥":
        ILE_KART_STOS_KIER = Przenies_na_stos(karta,karta_kolumna,KIER,ILE_KART_STOS_KIER,STOS_KIER)
    elif karta[-1] == "♦":
        ILE_KART_STOS_KARO = Przenies_na_stos(karta,karta_kolumna,KARO,ILE_KART_STOS_KARO,STOS_KARO)
    elif karta[-1] == "♠":
        ILE_KART_STOS_PIK = Przenies_na_stos(karta,karta_kolumna,PIK,ILE_KART_STOS_PIK,STOS_PIK)
    elif karta[-1] == "♣":
        ILE_KART_STOS_TREFL = Przenies_na_stos(karta,karta_kolumna,TREFL,ILE_KART_STOS_TREFL,STOS_TREFL)
    if STOS_KIER == KIER and STOS_KARO == KARO and STOS_PIK == PIK and STOS_TREFL == TREFL:
        Wygrana()
    else:
        Wybor()
    


def Wybor(): #Główne menu, to tutaj gracz wybiera co chce zrobić z kartami.
    global INFORMACJA, LICZBA_RUCHOW
    HUD()
    Wskazowka()
    try:
        wybor = int(input(f"\n{GREEN}[1 = Przenieś kartę/zbiór] {YELLOW}[2 = Przenieś kartę na stos] {RED}[3 = Przetasuj kartę z talii] {CYAN}[4 = Dobierz kartę z talii] {BLUE}[5 = Cofnij] {PURPLE}[0 = Ustawienia]{RESET}\nJakie działanie wykonać: "))
    except ValueError:
        INFORMACJA = "Błędne dane wejściowe"
        Wybor()
    if wybor == 1:
        LICZBA_RUCHOW += 1
        Przenoszenie_kart()
    elif wybor == 2:
        LICZBA_RUCHOW += 1
        Stosy()
    elif wybor == 3:
        LICZBA_RUCHOW += 1
        Przetasuj_karte_z_talii()
    elif wybor == 4:
        LICZBA_RUCHOW += 1
        Dobierz_karte_z_talii()
    elif wybor == 5:
        Wczytaj_kopie()
        Wybor()
    elif wybor == 0:
        Koniec()
    else:
        INFORMACJA = f"Opcja numer: {wybor}, nie istnieje."
        Wybor()



def Karta(karta): #Przydziela kolor i wartość dla karty.
    if karta[-1] == "♥":
        kolor = "czerwony"
        wartosc = KIER.index(karta)+1
    elif karta[-1] == "♦":
        kolor = "czerwony"
        wartosc = KARO.index(karta)+1
    elif karta[-1] == "♠":
        kolor = "czarny"
        wartosc = PIK.index(karta)+1
    elif karta[-1] == "♣":
        kolor = "czarny"
        wartosc = TREFL.index(karta)+1
    return kolor, wartosc



def Przenoszenie_kart(): #Przenosi kartę/karty na podaną kolumnę, sprawdza czy karty spełniają warunki: naprzemienne kolory oraz wartości.
    global INFORMACJA, LICZBA_RUCHOW
    HUD()
    try:
        kolumna = int(input("\nZ której kolumny przenieść kartę: "))-1
    except ValueError:
        INFORMACJA = "Błędne dane wejściowe"
        LICZBA_RUCHOW -= 1
        Wybor()
    if kolumna >=LIBCZA_KOLUMN:
        INFORMACJA = f"Nie ma kolumny numer: {kolumna+1}"
        LICZBA_RUCHOW-=1
        Wybor()
    if not KOLUMNY[kolumna]:
        INFORMACJA = "Nie możesz przenieść niczego."
        LICZBA_RUCHOW-=1
        Wybor()
    if kolumna in range(LIBCZA_KOLUMN):
        if len(KOLUMNY[kolumna]) == 1:
            Naj_karta = 0
        else:
            try:
                Naj_karta = int(input(f"\nIle kart chcesz przenieść max({len(KOLUMNY[kolumna])}): ")) - 1
            except ValueError:
                INFORMACJA = "Błędne dane wejściowe"
                LICZBA_RUCHOW -= 1
                Wybor()
        if Naj_karta <= -1:
            INFORMACJA = "Nie możesz przenieść 0 kart."
            LICZBA_RUCHOW-=1
            Wybor()
        if Naj_karta+1 > len(KOLUMNY[kolumna]):
            INFORMACJA = f"Nie ma {Naj_karta+1} kart w kolumnie: {kolumna+1}"
            LICZBA_RUCHOW -= 1
            Wybor()
        try:
            cel = int(input(f"\nDo której kolumny przenieść karty: "))-1
        except ValueError:
            INFORMACJA = "Błędne dane wejściowe"
            LICZBA_RUCHOW -= 1
            Wybor()
        if cel in range(LIBCZA_KOLUMN):
            if cel != kolumna:
                kolor , wartosc = Karta(KOLUMNY[kolumna][Naj_karta])
                if KOLUMNY[cel]:
                    kolor_cel, wartosc_cel = Karta(KOLUMNY[cel][0])
                    if kolor == kolor_cel:
                        INFORMACJA = "Karty są w tym samym kolorze."
                        LICZBA_RUCHOW -= 1
                        Wybor()
                    elif wartosc+1 != wartosc_cel:
                        INFORMACJA = "Niewłaściwa wartość karty."
                        LICZBA_RUCHOW -= 1
                        Wybor()
                    elif kolor != kolor_cel and wartosc + 1 == wartosc_cel:
                        if Naj_karta > 0:
                            kolor_wczesniej, wartosc_wczesniej = Karta(KOLUMNY[kolumna][Naj_karta-1])
                            if kolor_wczesniej != kolor and wartosc_wczesniej +1 == wartosc:
                                Zapisz_kopie()
                                for i in range(Naj_karta, -1 , -1):
                                    KOLUMNY[cel].insert(0, KOLUMNY[kolumna].pop(i))
                                    if [] in KOLUMNY[cel]:
                                        KOLUMNY[cel].remove([])
                                Odkryj(kolumna+1)
                                Wybor()
                            else:
                                INFORMACJA = ("Błędne dane wejściowe")
                                LICZBA_RUCHOW -= 1
                                Wybor()
                        elif Naj_karta == 0:
                            Zapisz_kopie()
                            Przesun(cel+1,kolumna+1)
                            Odkryj(kolumna+1)
                            Wybor()
                elif not KOLUMNY[cel]:
                    if wartosc == WARTOSC_KROLA:
                        Zapisz_kopie()
                        for i in range(Naj_karta, -1 , -1):
                            KOLUMNY[cel].insert(0, KOLUMNY[kolumna].pop(i))
                            if [] in KOLUMNY[cel]:
                                KOLUMNY[cel].remove([])
                        Odkryj(kolumna+1)
                        Wybor()
                    else:
                        INFORMACJA = "Na puste miejsca można przenieść tylko kartę Króla."
                        LICZBA_RUCHOW -= 1
                        Wybor()
            else:
                INFORMACJA = f"Nie możesz przenieść karty z kolumny na tą samą kolumnę."
                LICZBA_RUCHOW -= 1
                Wybor()
        else:
            INFORMACJA = (f"Nie ma kolumny docelowej numer {cel+1}.")
            LICZBA_RUCHOW -= 1
            Wybor()
    else:
        INFORMACJA = (f"Nie ma kolumny numer {kolumna+1}.")
        LICZBA_RUCHOW -= 1
        Wybor()



def Pokoloruj(karta): #Koloruje karty ze znakiem KARO i KIER na czerwono, a dla PIK i TREFL zostawia normalny kolor.
    if karta[-1] == "♥" or karta[-1] == "♦":
        pokolorowana_karta = (f"[{RED+karta+RESET}]")
    else:
        pokolorowana_karta=(f"[{karta}]")
    return pokolorowana_karta



def Wyczysc(): #Wizualne oczyszczenie terminalu.
    print("\n" * 100)



def Nazwa(): #Tytuł gry zapisany w formacie ANSI Shadow.
    print(CYAN)
    print("██████╗  █████╗ ███████╗     ██╗ █████╗ ███╗   ██╗███████╗")
    print("██╔══██╗██╔══██╗██╔════╝     ██║██╔══██╗████╗  ██║██╔════╝")
    print("██████╔╝███████║███████╗     ██║███████║██╔██╗ ██║███████╗")
    print("██╔═══╝ ██╔══██║╚════██║██   ██║██╔══██║██║╚██╗██║╚════██║")
    print("██║     ██║  ██║███████║╚█████╔╝██║  ██║██║ ╚████║███████║")
    print("╚═╝     ╚═╝  ╚═╝╚══════╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝")
    print("                                                          ")
    print("██████╗ ██╗   ██╗    ███████╗██╗    ██╗████████╗███████╗  ")
    print("██╔══██╗╚██╗ ██╔╝    ╚══███╔╝██║    ██║╚══██╔══╝██╔════╝  ")
    print("██████╔╝ ╚████╔╝       ███╔╝ ██║ █╗ ██║   ██║   ███████╗  ")
    print("██╔══██╗  ╚██╔╝       ███╔╝  ██║███╗██║   ██║   ╚════██║  ")
    print("██████╔╝   ██║       ███████╗╚███╔███╔╝   ██║   ███████║  ")
    print("╚═════╝    ╚═╝       ╚══════╝ ╚══╝╚══╝    ╚═╝   ╚══════╝  ")
    print(RESET)
    print("")



def Zasady(): #Otwiera plik z zasdmi i je pokazuje.
    global INFORMACJA
    try:
        with open("zasady(rules).txt", "r", encoding="utf-8") as plik:
            zasady = plik.read()
            print(zasady)
    except FileNotFoundError:
        INFORMACJA = "W folderze brakuje pliku zasady.txt"
        Opcje()



def Wskazowka(): #Funkcja pokazująca informacje, jeśli jakaś jest.
    global INFORMACJA
    if INFORMACJA != "":
        print(f"\nWskazówka: {INFORMACJA}")
        INFORMACJA = ""



def Opis_symboli_kart(): #Przedstawia opis symboli kart, pokazuje losową kartę z talii.
    print("Opis symboli kart:")
    print(f"W talii znajdują się {len(TALIA_KART)} karty, po {int(len(TALIA_KART)/4)} z każdego rodzaju.\n")
    print(f"|{RED+"♥"+RESET}| Symbol przedstawiający kier.")
    print(f"|{RED+"♦"+RESET}| Symbol przedstawiający karo.")
    print("|♠| Symbol przedstawiający pik.")
    print("|♣| Symbol przedstawiający trefl.")
    print(f"\nTak wygląda przykładowa karta z talii: {Pokoloruj(random.choice(TALIA_KART))}")



def Przetasowana_talia(): #Pokazuje przykładowo przetasowaną talię.
    print("Przykładowo przetasowana talia: \n")
    n=0
    for karta in TALIA_KART:
        if n == 26:
            print("")
        print(Pokoloruj(karta), end="")
        n +=1



def Przesun(dodaje, usuwam): #Przenosi kartę z jednej kolumny do drugiej.
    KOLUMNY[dodaje-1].insert(0, KOLUMNY[usuwam-1].pop(0))
    if [] in KOLUMNY[dodaje-1]:
        KOLUMNY[dodaje-1].remove([])



def Odkryj(kolumna): #Odkrywa 1 zakrtyą kartę jeśli dana kolumna jest pusta.
    if not KOLUMNY[kolumna-1]:
        if KOLUMNY_UKRYTE[kolumna-1]:
            KOLUMNY[kolumna-1].insert(0, KOLUMNY_UKRYTE[kolumna-1].pop(0))
            if [] in KOLUMNY[kolumna-1]:
                KOLUMNY[kolumna-1].remove([])
    


def Pokaz_kolumny(): #Pokazuje wyrównane kolumny.
    for kolumna in range(LIBCZA_KOLUMN-1,-1,-1):
        print(f"Nie odsłonięte karty = {len(KOLUMNY_UKRYTE[kolumna])}",f"| Kolumna {kolumna+1}:",end="")
        for karta in KOLUMNY[kolumna][::-1]:
            print(Pokoloruj(karta), end="")
        print("")
    print("")



def Pokaz_stos(stos): #Pokazuje wyrównane stosy.
    for karty in stos:
        print(Pokoloruj(karty), end="")
    print("")



def Wygrana(): #Ekran końcowy zapisany w formacie ANSI Shadow, zapisanie wyników gracza, pokazanie rankingu.
    global LICZBA_RUCHOW,IMIE
    Wyczysc()
    print(GREEN)
    print("██╗    ██╗██╗   ██╗ ██████╗ ██████╗  █████╗ ██╗     ███████╗███████╗")
    print("██║    ██║╚██╗ ██╔╝██╔════╝ ██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝")
    print("██║ █╗ ██║ ╚████╔╝ ██║  ███╗██████╔╝███████║██║     █████╗  ███████╗")
    print("██║███╗██║  ╚██╔╝  ██║   ██║██╔══██╗██╔══██║██║     ██╔══╝  ╚════██║")
    print("╚███╔███╔╝   ██║   ╚██████╔╝██║  ██║██║  ██║███████╗███████╗███████║")
    print(" ╚══╝╚══╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ")
    print(RESET)
    IMIE = input(f"\nPodaj nazwę aby zapisać swój wynik {LICZBA_RUCHOW}: ").replace(","," ")
    Zapisz_wyniki(IMIE,LICZBA_RUCHOW)
    print("")
    Pokaz_ranking()
    input("\n\nNaciśnij ENTER aby kontynuować: ")
    Opcje()



def Zapisz_wyniki(imie, liczba_ruchow): #Zapisuje wynik gracza do pliku ranking.txt
    global WYBRANY_POZIOM_TRUDNOSCI
    try:
        with open("ranking.txt", "r+") as plik:
            plik.seek(0, 2)
            if POZIOM_TRUDNOSCI == 2: 
                WYBRANY_POZIOM_TRUDNOSCI="Trudny"
            elif POZIOM_TRUDNOSCI == 1: 
                WYBRANY_POZIOM_TRUDNOSCI="Łatwy"
            plik.write(f"\n{imie}, {liczba_ruchow}, {WYBRANY_POZIOM_TRUDNOSCI}")
    except FileNotFoundError:
        Wyczysc()
        input("Nie znaleziono pliku ranking.txt \n\nNiestety bez niego nie jesteś w stanie zapisać wyniku ani sprawdzić rankingu innych graczy.")
        Opcje()



def Pokaz_ranking(): #Pokazuje ranking graczy, zawiera wyróżnienie 1 miejsca oraz pokazuje miejsce które zdobył gracz.
    global RANKING
    tymczasowy_ranking=[]
    try:
        with open("ranking.txt", "r") as plik:
            zawartosc = plik.readlines()
            for linia in zawartosc:
                tymczasowa_wartosc = linia.strip().split(", ")
                if len(tymczasowa_wartosc) == 3:
                    tymczasowy_ranking.append(tymczasowa_wartosc)
            RANKING = sorted(tymczasowy_ranking, key=lambda x: int(x[1]))
            for miejsce in range(len(RANKING)):
                if miejsce == 0:
                    print(YELLOW+f"Miejsce {miejsce+1}. Liczba ruchów: [{RANKING[miejsce][1]}] --- |{RANKING[miejsce][0]}|, na poziomie: {RANKING[miejsce][2]}"+RESET)
                else:
                    print(f"Miejsce {miejsce+1}. Liczba ruchów: [{RANKING[miejsce][1]}] --- |{RANKING[miejsce][0]}|, na poziomie: {RANKING[miejsce][2]}")
            osoba = RANKING.index([IMIE, str(LICZBA_RUCHOW), WYBRANY_POZIOM_TRUDNOSCI])
            print(f"\nZajmujesz {osoba+1} miejsce w rankingu z ilością ruchów: {RANKING[osoba][1]}, na poziomie: {RANKING[osoba][2]}.")
    except FileNotFoundError:
        Wyczysc()
        input("Nie znaleziono pliku ranking.txt \nNiestety bez niego nie jesteś w stanie zapisać wyniku ani sprawdzić rankingu innych graczy.")
        Opcje()



def Przenies_na_stos(karta,karta_kolumna,znak,ile_znak, stos_znak): #Przenosi kartę na stos.
    global INFORMACJA,LICZBA_RUCHOW,KARTY_ZAPASOWE
    if znak.index(karta) == ile_znak:
        Zapisz_kopie()
        if karta_kolumna == 8:
            stos_znak.append(karta)
            ile_znak +=1
            TALIA_KART.remove(TALIA_AKTYWNA[-1]), TALIA_AKTYWNA.pop(-1)
            KARTY_ZAPASOWE- 1
        elif karta_kolumna in range(LIBCZA_KOLUMN+1):
            KOLUMNY[karta_kolumna-1].pop(0)
            Odkryj(karta_kolumna)
            ile_znak +=1
            stos_znak.append(karta)
    else:
        INFORMACJA = (f"Karta {Pokoloruj(karta)} nie spełnia wymogów!")
        LICZBA_RUCHOW -= 1
    return ile_znak



def Pokaz_talie(): #Pokazuje talię zapasowych kart.
    if TALIA_AKTYWNA:
        print("Talia:",end="")
        for karta in TALIA_AKTYWNA:
            print(Pokoloruj(karta), end="")
        print("")
        print("")
    elif TALIA_KART:    
        if not TALIA_AKTYWNA:
            Przetasuj_talie()
            Pokaz_talie()



def Przetasuj_talie(): #Tasuje talie zapasową według poziomu trudności.
    global INFORMACJA,KARTY_ZAPASOWE
    if KARTY_ZAPASOWE >= len(TALIA_KART):
        random.shuffle(TALIA_KART)
        KARTY_ZAPASOWE = 0
        if TALIA_KART:
            INFORMACJA = "Przetasowano talię."
            TALIA_AKTYWNA.clear()
            for _ in range(TRUDNOSC):
                if KARTY_ZAPASOWE != len(TALIA_KART):
                    TALIA_AKTYWNA.append(TALIA_KART[KARTY_ZAPASOWE])
                    KARTY_ZAPASOWE+=1
                else:
                    Wybor()
    elif KARTY_ZAPASOWE < len(TALIA_KART):
        for _ in range(TRUDNOSC):
            if KARTY_ZAPASOWE >= len(TALIA_KART):
                Wybor()
                break
            TALIA_AKTYWNA.append(TALIA_KART[KARTY_ZAPASOWE])
            KARTY_ZAPASOWE+=1 
        


def Przetasuj_karte_z_talii(): #Przesuwa karty w talii zapasowej.
    global INFORMACJA,LICZBA_RUCHOW
    Zapisz_kopie()
    if TALIA_KART:
        if POZIOM_TRUDNOSCI == 1:
            if len(TALIA_AKTYWNA) == 3:
                TALIA_AKTYWNA.pop(0)
            Przetasuj_talie()
            Wybor()
        if POZIOM_TRUDNOSCI == 2:
            print(TALIA_KART)
            TALIA_AKTYWNA.clear()
            Przetasuj_talie()
            Wybor()
    else:
        INFORMACJA = "Talia jest pusta."
        LICZBA_RUCHOW-=1
        Wybor()



def Dobierz_karte_z_talii(): #Pozwala na dobranie karty z talii.
    global INFORMACJA,LICZBA_RUCHOW, KARTY_ZAPASOWE
    HUD()
    if TALIA_AKTYWNA:
        kolor_karty, wartosc_karty = Karta(TALIA_AKTYWNA[-1])
    else:
        INFORMACJA = "Talia jest pusta."
        LICZBA_RUCHOW-=1
        Wybor()
    try:
        cel_przenoszenie = int(input(f"\nDo której kolumny chcesz przenieść kartę {Pokoloruj(TALIA_AKTYWNA[-1])}: "))
    except ValueError:
        INFORMACJA = "Błędne dane wejściowe"
        LICZBA_RUCHOW -= 1
        Wybor()
    if cel_przenoszenie in range(LIBCZA_KOLUMN+1):
        if KOLUMNY[cel_przenoszenie-1]:
            karta_cel = KOLUMNY[cel_przenoszenie-1][0]
            kolor_karty_cel, wartosc_karty_cel = Karta(karta_cel)
            if kolor_karty == kolor_karty_cel or  wartosc_karty >= wartosc_karty_cel or wartosc_karty_cel - 1 != wartosc_karty:
                INFORMACJA = (f"[{TALIA_AKTYWNA[-1]}] [{karta_cel}] Karty nie pasują do siebie.")
                LICZBA_RUCHOW -= 1
                Wybor()
            elif kolor_karty != kolor_karty_cel and wartosc_karty + 1 == wartosc_karty_cel:
                KARTY_ZAPASOWE-=1
                Dobierz(cel_przenoszenie)
        elif not KOLUMNY[cel_przenoszenie-1]:
            if wartosc_karty == WARTOSC_KROLA:
                KARTY_ZAPASOWE-=1
                Dobierz(cel_przenoszenie)
            else:
                INFORMACJA = ('Na puste miejsca można przenieść tylko kartę Króla.')
                LICZBA_RUCHOW -= 1
                Wybor()
    else:
        INFORMACJA = f"Nie ma kolumny numer {cel_przenoszenie}."
        LICZBA_RUCHOW -= 1
        Wybor()



def Dobierz(cel_przenoszenie): #Podfunkcja do Dobierz_karte_z_talii().
    Zapisz_kopie()
    KOLUMNY[cel_przenoszenie-1].insert(0, TALIA_AKTYWNA[-1]), TALIA_KART.remove(TALIA_AKTYWNA[-1]), TALIA_AKTYWNA.pop(-1)
    if [] in KOLUMNY[cel_przenoszenie-1]:
        KOLUMNY[cel_przenoszenie-1].remove([])
    Wybor()



def Zapisz_kopie(): #Zapisuje kopie wszystkich zmiennych, maksymalnie mogą być tylko 3, więc jeśli zapisuje się nową kopię, usuwana jest ta najstarsza.
    global LICZBA_AKTYWNYCH_KOPII,KOPIA_1,KOPIA_2,KOPIA_3
    if LICZBA_AKTYWNYCH_KOPII == 3:
        KOPIA_1 =  KOPIA_2.copy()
        KOPIA_2 =  KOPIA_3.copy()
        KOPIA_3.clear()
        LICZBA_AKTYWNYCH_KOPII-=1
    if LICZBA_AKTYWNYCH_KOPII == 0:
        KOPIA_1 = Zapisz()
        LICZBA_AKTYWNYCH_KOPII+=1
    elif LICZBA_AKTYWNYCH_KOPII == 1:
        KOPIA_2 = Zapisz()
        LICZBA_AKTYWNYCH_KOPII+=1
    elif LICZBA_AKTYWNYCH_KOPII == 2:
        KOPIA_3 = Zapisz()
        LICZBA_AKTYWNYCH_KOPII+=1



def Zapisz(): #Podfunkcja do Zapisz_kopie(), zapisuje kopie wszystkich zmiennych.
    aktualna_kopia = {
    nazwa: [elem[:] if isinstance(elem, list) else elem for elem in globals()[nazwa]]
    if isinstance(globals()[nazwa], list) else globals()[nazwa]
    for nazwa in NAZWY_WSZYSTKIEGO
    }
    return aktualna_kopia



def Wczytaj_kopie(): #Wczytuje kopię, w zależności od tego, jak daleko gracz chce się cofnąć.
    HUD()
    global INFORMACJA,KOPIA_1,KOPIA_2,KOPIA_3,LICZBA_AKTYWNYCH_KOPII,LICZBA_RUCHOW
    try:
        O_ILE_COFNAC = int(input(f"\nIle ruchów chcesz cofnąć (Dostępne: {LICZBA_AKTYWNYCH_KOPII}): "))
    except ValueError:
        INFORMACJA = "Błędne dane wejściowe"
        Wybor()
    if not O_ILE_COFNAC in range(MAX_COFNIEC,0,-1):
        INFORMACJA= f"Możliwe jest cofnięcie maksymalnie o {MAX_COFNIEC} ruchy."
        Wybor()
    elif O_ILE_COFNAC == 1:
        if KOPIA_3:
            Wczytaj(KOPIA_3)
            Wybor()
        elif KOPIA_2:
            Wczytaj(KOPIA_2)
            Wybor()
        elif KOPIA_1:
            Wczytaj(KOPIA_1)
            Wybor()
        else:
            INFORMACJA = "Nie można już się cofnąć."
            Wybor()
    elif O_ILE_COFNAC == 2:
        if KOPIA_3:
            if KOPIA_2:
                Wczytaj(KOPIA_2)
                KOPIA_3.clear()
                LICZBA_AKTYWNYCH_KOPII -= 1
                Wybor()
        elif KOPIA_1:
            INFORMACJA = "Cofnięto tylko o 1 ruch."
            Wczytaj(KOPIA_1)
            if KOPIA_2:
                INFORMACJA = ""
                KOPIA_2.clear()
                LICZBA_AKTYWNYCH_KOPII -= 1
            Wybor()
        else:
            INFORMACJA = "Nie można już się cofnąć."
    elif O_ILE_COFNAC == 3:
        if KOPIA_1:
            INFORMACJA = "Cofnięto tylko o 1 ruch."
            Wczytaj(KOPIA_1)
            if KOPIA_2:
                KOPIA_2.clear()
                LICZBA_AKTYWNYCH_KOPII -= 1
                INFORMACJA = "Cofnięto tylko o 2 ruchy."
            if KOPIA_3:
                KOPIA_3.clear()
                LICZBA_AKTYWNYCH_KOPII -= 1
                INFORMACJA = ""
            Wybor()
        else:
            INFORMACJA = "Nie można już się cofnąć."



def Wczytaj(kopia): #Podfunkcja do Wczytaj_kopie(), wczytuje kopie i ustawia wszystkie zmienne, jakie zostały w niej zapisane.
    global LICZBA_AKTYWNYCH_KOPII,LICZBA_RUCHOW,KOPIA_1,KOPIA_2,KOPIA_3
    for nazwa, dane in kopia.items():
        if isinstance(dane, list):
            globals()[nazwa] = [elem[:] if isinstance(elem, list) else elem for elem in dane]
        else:
            globals()[nazwa] = dane
    kopia.clear()
    LICZBA_RUCHOW -= 1
    LICZBA_AKTYWNYCH_KOPII -= 1







Opcje() #Uruchomienie gry.
