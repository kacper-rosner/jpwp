#######  Robiąc zadania można pominąć do 13 linijki ########

# W razie problemów patrz na: https://www.cs.emory.edu/~cheung/Courses/253/Syllabus/Map/skip-list-impl.html

# Uwaga - to zadanie może, ale nie musi opierać się na losowości
# Na zasadzie różnych dodatkowych struktur, możemy lepiej lub gorzej
# określać algorytmy dokładania nowych węzłów

# Odpowiadając na wstępne pytanie: drzewa czerwono czarne są również
# efektywne, ale według wielu mogą być mniej efektywne przy wielodostępie
# Są natomiast na pewno bardziej  obciążające pamięciowo

# Zadanie 3 

# W tej implementacji (jest wiele)
# każdy węzeł skip listy ma cztery wskaźniki, klucz i wartość
# Struktura jest umiarkowanie ciężka do zaimplementowania

# Może ci się nie udać zrobić zadania bez linku (linijka nr. 3). Jest tam pseudokod i implementacja w Javie



import random

NEG_INF = float("-inf")
POS_INF = float("inf")

class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.up = None
        self.down = None
        self.next = None
        self.prev = None
     
        # Zadanie 3a
class SkipList:
    def __init__(self):
        # Tworzymy bazową strukturę z nodeami na poziomie 0
        self.head = Node(________) # wstaw tutaj wartość klucza (zobacz link)
        self.tail = Node(________) # wstaw tutaj wartość klucza (zobacz link)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.n = 0 # liczba elementów
        self.h = 0 # aktualna wysokość

    def search(self, key):
    
        # Zadanie 3b
        # Znajdź węzeł o danym kluczu lub największy mniejszy od klucza
        
        
        p = self.head # Wskazówka: w analogiczny sposób poruszaj się po nodeach
        while True:
            # Uzupełnij: Idź w prawo tak długo jak następny klucz <= szukany
            while p.next.key <= key:
                p = p._____
            # Uzupełnij: Jeśli możesz, zejdź w dół
            if p.down is not None:
                p = p._____
            else:
                break
        return p 
    # Zwraca mniejszy (nie ma w zbiorze) 
    # lub równy szukanemu (jest w zbiorze) klucz węzła

    def insert(self, key, value=None):
        
        # Zadanie 3c - ciężkie, ale nic bez niego nie sprawdzisz
        
        # Uwaga - na tym zadaniu możesz spędzić bardzo dużo czasu.
        # Jeśli źle podepniesz wskaźniki, możesz je stracić na zawsze
        
        # Pamiętaj by upewniać się, że posiadasz wskaźniki do odpowiednich nodeów,
        # ma znaczenie, w jakiej kolejności będziesz je podmieniać
        
        # 0. Przypdaek, gdy klucz już jest w liście
        p = self.search(key)
        
        # Jeśli klucz już istnieje, zaktualizuj wartość i zakończ
        if p.key == key:
            p.value = __________ # Wsk.: odp. jest bardzo nasuwająca się
            return
        
        # 1. Wstaw nowy węzeł (key, value) na najniższym poziomie za p
        
        # Wsk.: Pamiętaj, że jeśli nie znaleziono wartości, 
        # to p jest najbliższym z lewej strony obecnym w liście kluczem
        q = Node(key, value)
        
        # podmień potrzebne wskaźniki (powinny być 4 zmiany) 
        q.prev = ________
        q.next = p.______
        p.next.prev = _______
        p.next = _______
        
        # 2. Wykonaj pętlę "rzutu monetą" dla tworzenia wieży
        
        i = 0
        while random.random() < 0.5: # powtórz losową ilość razy
        
        # Jak pamiętasz, na samej górze musi być jeden pusty wiersz,
        # Oznacza to, że jeśli bieżący poziom >=self.h, trzeba zwiększyć self.h o jeden
        # Zaimplementuj:
        # - sprawdzenie warunku, zwiększenie self.h
        # - stworzenie nowego heada i taila listy (2x new Node)
        # - odpowiednie podpięcie nowych węzłych i 
        # starych węzłów self.head i self.tail (4 zmiany)
        # - zmień stare węzły head i tail na nowe (2 zmiany)
            if i >= self.h:
                self.h += 1
                new_head = Node(_______) # Wskazówka - jak wyżej
                new_tail = Node(_______) # Wskazówka - jak wyżej
                
                new_head.next = new_tail
                new_tail.prev = new_head
                
                new_head.down = ________
                new_tail.down = ________
                self.head.up = new_head
                self.tail.up = new_tail
                
                self.head = ________
                self.tail = ________
       
        # 3. Wykonaj tworzenie wieży
        
        # Upewniłeś/aś się że jest wystarczająco warstw. '
        # Teraz zacznij tworzyć wieżę
        
        # a. Zacznij od elementu p. Idź w lewo, dopóki nie znajdziesz 
        # elementu, który ma niepusty wskaźnik w górę
            while p.up is None:
                p = p.________
                
        # b. Jeśli taki znalazłeś, to idź raz do góry i 
        # zmień p na tego, na którym teraz jesteś
            p = p.up
            
        # c. Stwórz nowy węzeł nad wstawionym wcześniej nodem q 
        # i go podepnij zewsząd - powinno być 6 zmian
        # Nowostworzony węzeł nie powinien mieć żadnej wartości, Node(k, None)
            e = Node(key, None)
            
            # Podepnij nowy node
            e.prev = ______
            e.next = p.______
            e.down = ________
            
            # Podepnij stare nodey do nowego
            p.next.prev = ______
            p.next = ______
            q.up = _______
        
        
        
            q = e
            i += 1
            
        self.n += 1  # Zwiększenie licznika elementów
        return None

    
    # koniec zadań, dalej tylko kod testów i printu !!!!!!!!!!!!!!!!!
    
    
    def display(self):
        # Wizualizuje strukturę Skip Listy w CLI z zachowaniem wyrównania wież.
        print(f"\n--- Skip List (Wysokość: {self.h}, Elementów: {self.n}) ---")
        
        all_keys = []
        curr = self.head
        while curr.down:  # Zejdź na sam dół
            curr = curr.down
        
        temp = curr
        while temp:
            all_keys.append(temp.key)
            temp = temp.next

        level_ptr = self.head
        current_h = self.h
        
        while level_ptr:
            keys_on_level = {}
            node_ptr = level_ptr
            while node_ptr:
                keys_on_level[node_ptr.key] = True
                node_ptr = node_ptr.next
            
            # Buduj linię poziomu
            row = f"L{current_h:02d}: "
            for key in all_keys:
                if key in keys_on_level:
                    if key == NEG_INF: label = "-oo"
                    elif key == POS_INF: label = "+oo"
                    else: label = str(key)
                    
                    row += f"[{label:^4}]"
                else:
                    row += "      " # Puste miejsce (odstęp)
                
                if key != all_keys[-1]:
                    row += "--"
            
            print(row)
            
            if level_ptr.down:
                connectors = "     "
                for key in all_keys:
                    if key in keys_on_level and key in self._get_keys_at_level(level_ptr.down):
                        connectors += "  |   "
                    else:
                        connectors += "      "
                    if key != all_keys[-1]: connectors += "  "
                print(connectors)

            level_ptr = level_ptr.down
            current_h -= 1
        print("-" * len(row))

    def _get_keys_at_level(self, start_node):
        """Metoda pomocnicza do sprawdzania kluczy na danym poziomie."""
        keys = {}
        curr = start_node
        while curr:
            keys[curr.key] = True
            curr = curr.next
        return keys
    
    
if __name__ == "__main__":
    sl = SkipList()
    
    # Jeśli chcesz, wstaw tu swoje wartości
    test_data = [10, 30, 2, 15, 25, 40, 50, 1]
    for val in test_data:
        sl.insert(val, f"Data-{val}")
        
    sl.display()