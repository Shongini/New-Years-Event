from listagosci import lista
print("\nSylwester 2021/2022")
user_choice = -1

miejsce = ("Remiza Strażacka w Bogdanówce")


def show_gosci():
    lista_index = 1
    plik = open("listagosci.py", "r")
    plik.readable()
    for nowaosoba in lista:
        print("[" + str(lista_index) + "]", nowaosoba)
        lista_index += 1
    plik.close()

def pokaz_organizatorow():
    organizatorzy_index = 1
    plik = open("listaorganizatorow.txt", "r")
    plik.readable()
    for linia in plik:
        print("[" + str(organizatorzy_index) + "]",linia)
        organizatorzy_index +=1
    plik.close()

def delete_osoba():
    lista_index = int(input("Podaj indeks osoby do usunięcia: "))

    if lista_index < 1 or lista_index > len(lista):
        print("Osoba z podanym indeksem nieistnieje.")
        return

    lista.pop(lista_index)
    print("Osoba została usunięta z listy gości!\n")


def save_lista_to_file():
    plik = open("listagosci.txt", "w")
    for nowaosoba in lista:
        plik.write(nowaosoba)
    print("Lista gości zaaktualizowana pomyślnie.\n")
    plik.close()

def zaplata():
    plik = open("zaplatazasylwestra.py", "r")
    if plik.readable():
        for line in plik:
            print(line)

def zawartoscceny():
    plik = open("zawartoscsylwestracena.txt", "r")
    if plik.readable():
        for line in plik:
            print(line)

def ograniczeniewiekowe():
    wiek = input("Podaj swoja date urodzenia: ")
    ilosclat = (2021 - int(wiek))
    if ilosclat >= 18:
                print("Posiadasz wymagany wiek.")
    else:
                print("Jesteś za młody, żeby do nas przyjść.")

while user_choice != 11:

    if user_choice == 1:
        pokaz_organizatorow()
    if user_choice == 2:
        print(miejsce)
    if user_choice == 3:
        show_gosci()
    if user_choice == 4:
        nowaosoba = input("Wpisz imię i nazwisko osoby: ")
        lista.append(nowaosoba)
        print("Osoba została dodana do listy!\n")
    if user_choice == 5:
        delete_osoba()
    if user_choice == 6:
        save_lista_to_file()
    if user_choice == 7:
        zaplata()
    if user_choice == 8:
        print("Koszt imprezy to 120zł/osobę.")
    if user_choice == 9:
        zawartoscceny()
    if user_choice == 10:
        ograniczeniewiekowe()
    if user_choice > 11:
        print("Brak informacji pod podanym podpunktem, podaj inną wartość!")


    print("\nPodstawowe informacje: \n")
    print("1. Lista organizatorów")
    print("2. Miejsce organizacji")
    print("3. Lista gości")
    print("4. Dodaj gościa")
    print("5. Usuń gościa")
    print("6. Zapisz listę gości do pliku tekstowego")
    print("7. Informacje o zapłatach")
    print("8. Cena sylwestra")
    print("9. Zawartość ceny")
    print("10. Ograniczenia wiekowe")
    print("11. Wyjdź\n")



    user_choice = int(input("Wybierz liczbę: "))






