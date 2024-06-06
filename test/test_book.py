import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from book import Book

class Test_Book(unittest.TestCase):
    def test_dodavanje_naslova(self):
        b = Book("Bela griva", " ", 1959, " ")
        self.assertEqual(b.naziv, "Bela griva")

    def test_dodavanje_autora(self):
        b = Book("Bela griva", "Rene Gijo", 1959, " ")
        self.assertEqual(b.autor, "Rene Gijo")
    
    def test_dodavanje_godine_izdanja(self):
        b = Book("Bela griva", "Rene Gijo", 1959, " ")
        self.assertEqual(b.god_izdanja, 1959)

    def test_dodavanje_zanra(self):
        b = Book("Bela griva", "Rene Gijo", 1959, "Roman")
        self.assertEqual(b.zanr, "Roman")
        
    def test_displayinfo(self):
        b = Book("d", "d", 1959, "d")
        self.assertEqual(b.display_info(), "d, d, 1959, d")

if __name__ == '__main__':
   unittest.main()