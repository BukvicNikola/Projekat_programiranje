class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def Promeni_ime_knjige(self, stari_naslov, novi_naslov):
        for book in self.books:
            if book.naslov== stari_naslov:
                book.naslov = novi_naslov
                return
        print("Knjiga ne postoji.")



    def Obrisi_knjigu(self, naslov):
        for i, book in enumerate(self.books):
            if book.naslov == naslov:
                del self.books[i]
                return
        print("Knjiga ne postoji.")

    def Prikazi_knjigu(self):
        for book in self.books:
            print(book.display_info)

    def Pretrazi_knjigu(self, kriterijum, uslov):
        lista = []
        with open("listaknjiga.txt", "r") as file:
            for line in file:
                book_data = line.strip().split(", ")
                if kriterijum.lower() == "naslov" and uslov.lower() in book_data[0].lower():
                    lista.append(book_data)
                elif kriterijum.lower() == "autor" and uslov.lower() in book_data[1].lower():
                    lista.append(book_data)
                elif kriterijum.lower() == "godina_izdavanja" and uslov == book_data[2]:
                    lista.append(book_data)
                elif kriterijum.lower() == "zanr" and uslov.lower() in book_data[3].lower():
                    lista.append(book_data)
        return lista