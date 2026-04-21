# Przed rozpoczęciem zadania, przetestuj działanie cuckoo hashing interaktywnie na stronie:
# https://www.lkozma.net/cuckoo_hashing_visualization/

# Zadanie 1
# Uzupełnij kod hashowania cuckoo. 
# Użyj testów do sprawdzenia poprawności działania

# W realizacji zadania proponujemy skupić się na zrozumieniu 
# działania struktury oraz użyteczności hash, nie na 
# specyfice języka Python

###############################################################333
# Zasady:
# 1. Insert duplikatu ma nie zadziałać
# 2. Insert obiektu o takim samym hashu ma dać nowy na miejsce w 
# kolejnej tabeli (jeśli pierwsza zajęta to do drugiej i na odwrót)
# 3. Priorytetyzuj (zacznij sprawdzanie od) tabelę nr. 1, później drugą itd.
# 4. Nowy hash wygeneruj podobnie jak wcześniejsze
# 5. Lookup zwraca boolean
# 6. Delete nic nie zwraca - jeśli nie znaleziono to wypisz w konsoli


import random
import unittest

class CuckooHashTable:
    def __init__(self, size=11, max_iterations=50):
        self.size = size
        self.max_iterations = max_iterations
        self.table1 = [None] * self.size
        self.table2 = [None] * self.size
        self.seed1 = random.randint(1, 1000)
        self.seed2 = random.randint(1, 1000)

        # Tworzymy dwie tablice i dwie funkcje hashujące
        
    def _hash1(self, key):
        return (hash(key) ^ self.seed1) % self.size

    def _hash2(self, key):
        return (hash(key) ^ self.seed2) % self.size

# Zadanie 1a - dodaj lookup i delete: 
# element może znajdować się w dwóch lokacjach: 
# tabeli pierwszej lub drugiej, na miejscach:

# table1[_hash1(key)] lub table2[_hash2(key)]

# twoja implementacja *musi* mieć skończony amortyzowany O(1) 
# czas wykonania
        
    def lookup(self, key):
        if self.table1[self._hash1(key)] == key:
            return ____ # True /  False
        if self.table2[self._hash2(key)] == key:
            return ____ # True /  False
        return _____ # True /  False

    def delete (self, key):
        idx1 = self._hash1(key)
        if self.table1[idx1] == key:
            self.table1[idx1] = ____  # usuń wartość
            return
        idx2 = self._hash2(key)
        if self.table2[idx2] == key:
            self.table2[idx2] = ____ # usuń wartość
            return
        print("Klucza nie znaleziono")

# Zadanie 1b - dodaj insert:

# jeśli na sprawdzanym miejscu w jednej tablicy jest już element,
# przesuń go do drugiej tablicy. 
# 
# Powtarzaj do momentu znalezienia 
# wolnego miejsca (dla uproszczenia zrób funkcją for)
# 
# (zobacz sam: linijka nr.2)
#
# Pamiętaj duplikat - nie dodajemy do tablicy

    def insert(self, key):
        if self.lookup(key):
            _______ # Wsk.: co jeśli duplikat ? Nic.

        curr_key = key
       
        # Odkomentuj po zrobieniu 1b, przed 1c - dodaj pętlę for wg. 1c.4
        # _______________________________________________
        pos1 = self._hash1(curr_key)
        if self.table1[pos1] is None:
            self.table1[pos1] = ______ # Co ma być wstawione
            return
        curr_key, self.table1[pos1] = self.table1[pos1], curr_key

        pos2 = self._hash2(curr_key)
        if self.table2[pos2] is None:
            self.table2[pos2] = ______ # co ma być wstawione 
            return
        curr_key, self.table2[pos2] = self.table2[pos2], curr_key

        # Odkomentuj po zrobieniu 1b, przed 1c
        
        # self.rehash()
        # self.insert(curr_key)

# Zadanie 1c - dodatkowe:
# zapobiegnij możliwości powstania pętli przy insercie, 
# 1 zmieniając funkcję hashującą
# 2 zwiększając rozmiar tablic
# 3 wsadzając ponownie wszystkie wartości do tablicy
# 4 niech triggerem rehashu będzie powtarzanie insertu 
# int(self.size * 0.5)
# (tak, to znaczy że musisz edytować funkcję insert)

    def rehash(self):
        old_elements = [x for x in self.table1 if x is not None]
        old_elements.extend([x for x in self.table2 if x is not None])
        
        self.size *= 2
        self.table1 = [None] * self.size
        self.table2 = [None] * self.size
        __________ = random.randint(1, 1000) # Wsk. 1c.1
        __________ = random.randint(1, 1000) # Wsk. 1c.1
        
        for key in old_elements:
            _______________
            # Wsk. 1c.3 - uzyj insert
    
# Koniec zadań, początek testów !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
class TestCuckooHashing(unittest.TestCase):
    def test_insert_and_lookup(self):
        ch = CuckooHashTable(size=5)
        ch.insert("A")
        ch.insert("B")
        ch.insert("C")
        seed1 = random.randint(1, 1000)
        seed2 = random.randint(1, 1000)
        ch.insert(ch._hash1)
        self.assertTrue(ch.lookup("A"))
        self.assertTrue(ch.lookup("B"))
        self.assertTrue(ch.lookup("C"))
        self.assertFalse(ch.lookup("D"))

    def test_delete(self):
        ch = CuckooHashTable(size=5)
        ch.insert("X")
        self.assertTrue(ch.lookup("X"))
        ch.delete("X")
        self.assertFalse(ch.lookup("X"))

    def test_duplicate_and_collision(self):
        # Test wstawiania tego samego klucza wielokrotnie
        ch = CuckooHashTable(size=10)
        ch.insert("Duplicate")
        ch.insert("Duplicate")
        
        # Sprawdzamy czy nie ma duplikatu w strukturze (powinien być jeden)
        count = sum(1 for x in ch.table1 if x == "Duplicate") + \
                sum(1 for x in ch.table2 if x == "Duplicate")
        self.assertEqual(count, 1)

        # Test "kolizji" hashy - w Cuckoo wymusza to przemieszczanie elementów
        # Wstawiamy dużo elementów do małej tablicy, aby wymusić walkę o te same sloty
        small_ch = CuckooHashTable(size=3, max_iterations=5)
        keys = ["Key1", "Key2", "Key3", "Key4", "Key5"]
        for k in keys:
            small_ch.insert(k)
        
        for k in keys:
            self.assertTrue(small_ch.lookup(k))

    def test_rehashing(self):
        ch = CuckooHashTable(size=2, max_iterations=2)
        for i in range(20):
            ch.insert(str(i))
            
        for i in range(20):
            self.assertTrue(ch.lookup(str(i)))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)