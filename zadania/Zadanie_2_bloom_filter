import hashlib
import unittest

# Pomoc : https://www.jasondavies.com/bloomfilter/
# Zadanie 2 - proste
# Uzupełnij kod probabilistycznego filtru Blooma. 

# Prawdopodobieństwo na powtórzenie się tych samych
# elementów w tablicy jest tym mniejsze, im większa jest C(num_hashes, size) 
# i im mniej pokrywają się funkcje hashujące (tu: poza naszą kontrolą)

# Pamiętaj o tym, że dwie funkcje hashujące mogą zwracać ten sam bit
# dla tego samego słowa

class BloomFilter:
    def __init__(self, size=100, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * self.size

    def _get_hashes(self, key):
        hashes = []
        for i in range(self.num_hashes):
            # Używamy ziarna i, aby każda funkcja była inna
            hash_val = int(hashlib.md5((str(key) + str(i)).encode()).hexdigest(), 16)
            hashes.append(hash_val % self.size)
        return hashes

    def insert(self, key):
        # Zadanie 2a - dodaj insert:
        # Policz które bity musisz ustawić na jeden, 
        # żeby zaprezentować, że coś jest w zbiorze i je zmień na 1. 
        
        # Nie twórz żadnego faktycznego zbiornika na dane, tylko 
        # korzystaj ze stworzonego bit_aray
        
        indices = self.__________(key) # uzupełnij nazwę funkcji do hashów (jest wyżej)
        for idx in indices:
            self.bit_array[idx] = ____ # 0/1

    def lookup(self, key):
        # Zadanie 2b - dodaj lookup
        # Sprawdź czy bity, które odpowiadają za konkretną rzecz są prawdziwe
        # Może generować fałszywe poztywy
        """Zwraca True jeśli element może być w zbiorze, False jeśli na pewno go nie ma."""
        
        #Zobacz co się dzieje na linku u góry, gdy wpiszesz 'qadfkjnskaasddfasdfasfasdasddasdasdasdasdddadf gm'
        # - nie zawsze są 3 bity odpalane przy wpisaniu znaku
        indices = self._get_hashes(key)
        for idx in indices:
            if self.bit_array[idx] == 0:
                return _______ # True / False
        return _________# True / False

# koniec zadań !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class TestBloomFilter(unittest.TestCase):
    def test_insertion_and_retrieval(self):
        """Sprawdza, czy dodane elementy są poprawnie wykrywane."""
        bf = BloomFilter(size=100, num_hashes=3)
        bf.insert("Python")
        bf.insert("Gemini")
        
        self.assertTrue(bf.lookup("Python"))
        self.assertTrue(bf.lookup("Gemini"))

    def test_no_false_negatives(self):
        """Weryfikuje, że filtr nigdy nie zwraca False dla istniejącego elementu."""
        bf = BloomFilter(size=50, num_hashes=5)
        words = ["test1", "test2", "test3"]
        for w in words:
            bf.insert(w)
            
        for w in words:
            self.assertTrue(bf.lookup(w), f"Błąd: Nie znaleziono klucza {w}, który został wstawiony!")

    def test_absence(self):
        """Sprawdza, czy filtr poprawnie informuje o braku elementu (przy odpowiednim rozmiarze)."""
        bf = BloomFilter(size=1000, num_hashes=3)
        bf.insert("A")
        self.assertFalse(bf.lookup("B"))

    def test_overlapping_hashes_internal(self):
        """
        Weryfikuje zachowanie, gdy funkcje hashujące zwracają ten sam bit (kolizja wewnętrzna).
        Wspomniane w komentarzu zadania: 'nie zawsze są 3 bity odpalane'.
        """
        bf = BloomFilter(size=100, num_hashes=10)
        # Pobieramy hashe dla prostego klucza
        hashes = bf._get_hashes("CollisionTest")
        unique_hashes = set(hashes)
        
        bf.insert("CollisionTest")
        
        # Sprawdzamy czy liczba ustawionych bitów odpowiada liczbie UNIKALNYCH hashy
        bits_set = sum(bf.bit_array)
        self.assertEqual(bits_set, len(unique_hashes))

    def test_false_positive_demonstration(self):
        """
        Demonstruje wystąpienie False Positive przy bardzo małym rozmiarze tablicy.
        To nie jest błąd kodu, lecz cecha struktury.
        """
        bf = BloomFilter(size=5, num_hashes=3)
        bf.insert("Pierwszy")
        bf.insert("Drugi")
        
        # Przy tak małej tablicy (5 bitów) i 2 słowach (6 ustawień), 
        # większość bitów będzie wynosić 1, co wywoła fałszywy pozytyw dla nowego słowa.
        result = bf.lookup("Trzeci")
        print(f"\n[Info] Wynik dla 'Trzeci' (nie dodawany): {result}")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)