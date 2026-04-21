import unittest

# Zadanie 4 - zrób stos na liście pythonowskiej
# możliwości jest dużo, zadanie bardziej otwarte od 1,2,3

class Stack:
    def __init__(self):
        # Zadanie 4a
        # Inicjalizacja pustego magazynu danych
        self.items = _______

    def is_empty(self):
        # Sprawdzenie czy stos nie zawiera elementów
        return _______ == 0

    def push(self, item):
        # Zadanie 4b
        # Dodanie elementu na koniec listy (szczyt stosu)
        self.items._______(item)

    def pop(self):
        # Zadanie 4c
        # Usunięcie i zwrócenie ostatniego elementu
        if self._______():
            print("Stos jest pusty!")
            return None
        return self.items._______()

    def peek(self):
        # Zadanie 4d
        # Podejrzenie ostatniego elementu bez usuwania go
        if not self.is_empty():
            return self.items[_______]
        return None

    def size(self):
        return len(self.items)

    def display(self):
        
        print("\n--- STOS (Góra na górze) ---")
        if self.is_empty():
            print("[ Pusty ]")
        else:
            for item in reversed(self.items):
                print(f"| {item:^7} |")
            print(" ----------- ")

class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        s = Stack()
        s.push(10)
        s.push(20)
        s.push(30)
        
        self.assertEqual(s.peek(), 30)
        self.assertEqual(s.pop(), 30)
        self.assertEqual(s.size(), 2)
        self.assertFalse(s.is_empty())
        
        s.pop()
        s.pop()
        self.assertTrue(s.is_empty())
        self.assertIsNone(s.pop())

if __name__ == '__main__':
    # Przykład działania z wizualizacją
    my_stack = Stack()
    for x in ['A', 'B', 'C']:
        my_stack.push(x)
    my_stack.display()
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)