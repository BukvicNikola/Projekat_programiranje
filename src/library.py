class Library:
    def __init__(self):
        self.lista_objekata = []
    
    def dodaj_knjigu(self, book):
        self.lista_objekata.append(book)
        
    def ispis_knjiga(self):
        for object in self.lista_objekata:
            print(object.display_info())
    
    