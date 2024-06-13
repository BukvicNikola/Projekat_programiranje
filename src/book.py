class Book:
    def __init__(self, naslov, autor, godina_izdanja, zanr):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        self.zanr = zanr

    def __str__(self):
        return f' {self.naslov} od {self.autor}, godine: {self.godina_izdanja}, zanra: {self.zanr}'
