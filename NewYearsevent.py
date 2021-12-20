from listagosci import lista
print()
print("Sylwester 2021/2022")
user_choice = -1

organizatorzy = ["Dawid Chryc, Maciek Bierówka , Kamil Szopa, Patryk Pindel"]
miejsce = ("Remiza Strażacka w Bogdanówce")



def show_gosci():
    lista_index = 1
    for nowaosoba in lista:
        print(nowaosoba + "[" + str(lista_index) + "]")
        lista_index +=1
def delete_osoba():
    lista_index = int(input("Podaj indeks osoby do usunięcia: "))

    if lista_index < 1 or lista_index > len(lista):
        print("Osoba z podanym indeksem nieistnieje.")
        return

    lista.pop(lista_index)
    print("Osoba została usunięta z listy gości!")
    print()

def save_lista_to_file():
    file = open("listagosci.txt", "w")
    for nowaosoba in lista:
        file.write(nowaosoba+"\n")
    file.close()

while user_choice != 7:
    if user_choice == 1:
        print(organizatorzy)
    print()
    if user_choice == 2:
        print(miejsce)
    print()
    if user_choice == 3:
        show_gosci()
        print()
    if user_choice == 4:
        nowaosoba = input("Wpisz imię i nazwisko osoby: ")
        lista.append(nowaosoba)
        print("Osoba została dodana do listy!")
        print()
    if user_choice == 5:
        delete_osoba()

    if user_choice == 6:
        save_lista_to_file()

    print("Podstawowe informacje: ")
    print()
    print("1. Lista organizatorów")
    print("2. Miejsce organizacji")
    print("3. Lista gości")
    print("4. Dodaj gościa")
    print("5. Usuń gościa")
    print("6. Zapisz zmiany do pliku")
    print("7. Wyjdź")
    print()


    user_choice = int(input("Wybierz liczbę: "))