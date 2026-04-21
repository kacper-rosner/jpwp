import unittest

# Zadanie 5 - Zrób kolejke na liście pythonowskiej
# możliwości jest dużo

class Queue:
    def __init__(self):
        # Zadanie 5a
        # Inicjalizacja listy jako kontenera na dane
        self.items = _______

    def is_empty(self):
        # Sprawdzenie, czy w kolejce są jakiekolwiek elementy
        return _______ == 0

    def enqueue(self, item):
        # Zadanie 5b
        # Dodanie elementu na koniec kolejki
        self.items._______(item)

    def dequeue(self):
        # Zadanie 5c
        # Usunięcie i zwrócenie pierwszego elementu (index 0)
        if self._______():
            print("Kolejka jest pusta!")
            return None
        return self.items._______(_______)

    def peek(self):
        # Zadanie 5d
        # Podejrzenie pierwszego elementu bez usuwania go
        if not self.is_empty():
            return self.items[_______]
        return None

    def size(self):
        return len(self.items)

    def display(self):
        """Wizualizacja kolejki w CLI."""
        print("\n--- KOLEJKA (Front po lewej) ---")
        if self.is_empty():
            print("[ Pusta ]")
        else:
            # Formatowanie: [A] <- [B] <- [C]
            representation = " <- ".join([f"[{item}]" for item in self.items])
            print(f"FRONT: {representation} :REAR")
        print(" ------------------------------- ")

class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        q = Queue()
        q.enqueue("Klient_1")
        q.enqueue("Klient_2")
        q.enqueue("Klient_3")
        
        self.assertEqual(q.peek(), "Klient_1")
        self.assertEqual(q.dequeue(), "Klient_1")
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        
        q.dequeue()
        q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertIsNone(q.dequeue())

if __name__ == '__main__':
    # Przykład interaktywny
    my_queue = Queue()
    my_queue.enqueue("Zadanie_A")
    my_queue.enqueue("Zadanie_B")
    my_queue.display()
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)