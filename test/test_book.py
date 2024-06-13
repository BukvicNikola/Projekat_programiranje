import unittest
from book import Book  # Assuming your Book class is defined in a file named book.py

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        naslov = "Test Book"
        autor = "Test Autor"
        godina_izdanja = "1576"
        zanr = "roman"
        book = Book(naslov, autor, godina_izdanja, zanr)
        self.assertEqual(book.naslov, naslov)
        self.assertEqual(book.autor, autor)
        self.assertEqual(book.godina_izdanja, godina_izdanja)
        self.assertEqual(book.zanr, zanr)


    def test_book_str_method(self):
        naslov = "Test Book"
        autor = "Test Author"
        godina_izdanja = "1576"
        zanr = "roman"
        expected_output = f"Book: {naslov} by {autor}, Godina izdanja: {godina_izdanja}, Zanr: {zanr}"
        book = Book(naslov, autor, godina_izdanja, zanr)
        self.assertEqual(str(book), expected_output)

if __name__ == '__main__':
    unittest.main()