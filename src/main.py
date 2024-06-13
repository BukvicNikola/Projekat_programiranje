import os
from library import Library
from book import Book
library = Library()
file_path = "fajl.txt"
temp_file_path = "fajltemp.txt"
unos = input("Sta zelite da radite (1-Za dodavanje knjige, 2-Za brisanje knjige, 3-Za menjanje informacija o knjigama, 4-Za prikaz svih knjiga): ")
if unos =="1":
    while True:
        print("Napisi informacije o knjizi.")
        naziv = input("Naziv: ")
        autor = input("Autor: ")
        god_izdanja = input("Godina izdanja: ")
        zanr = input("Zanr: ")
        book = Book(naziv, autor, god_izdanja, zanr)
        library.add_book(book)
        code = input("Ako zelite da prekinete upis knjiga pritisnite x ako ne bilo sta drugo")
       
        with open("fajl.txt", "a") as file:
            for object in library.books:
                file.write(object.__str__() + "\n")

        if code == "x":
            break
    
elif unos == "2":
    print("NAPIŠITE ODGOVARAJUĆE INFORMACIJE KNJIGE KOJU ŽELITE DA OBRIŠETE")
    naslov = input("NASLOV: ")
    autor = input("AUTOR: ")
    godina_izdavanja = input("GODINA IZDAVANJA: ")
    žanr = input("ŽANR: ")
    knjiga = Book(naslov, autor, godina_izdavanja, žanr)
    with open("fajl.txt", "r") as file:
        lines = file.readlines()
            
    with open("fajltemp.txt", "w") as temp_file:
        for line in lines:
            if line.strip() != knjiga.__str__().strip():
                temp_file.write(line)
    os.replace(temp_file_path, file_path)

elif unos == "3":
    print("Napisi informacije o knjizi koju zelite da izmenite.")
    naziv = input("Naziv: ")
    autor = input("Autor: ")
    god_izdanja = input("Godina izdanja: ")
    zanr = input("Zanr: ")
    book = Book(naziv, autor, god_izdanja, zanr)

    print("Napisi informacije o izmenjenoj knjizi.")
    naziv1 = input("Naziv: ")
    autor1 = input("Autor: ")
    god_izdanja1 = input("Godina izdanja: ")
    zanr1 = input("Zanr: ")
    book1 = Book(naziv1, autor1, god_izdanja1, zanr1)

    with open("fajl.txt", "r") as file:
        lines = file.readlines()
    
    lines = [book1.__str__() + '\n' if book.__str__() in line else line for line in lines]
    with open("fajl.txt", "w") as file:
        file.writelines(lines)

    

elif unos == "4":
    kriterjum = input("Po cemu zelite da pretrazujete knjige: ")
    key_word = input("Kljucna rec za pretragu: ")
    results = library.Pretrazi_knjigu(kriterjum, key_word)
    print("Rezultati pretrage: ")
    for result in results:
        print(result)