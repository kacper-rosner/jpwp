import hashlib
import unittest

def get_sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

class Node:
    def __init__(self, value, left=None, right=None, version=0):
        self.value = value
        self.left = left
        self.right = right
        self.version = version
        self.hash = self._calculate_node_hash()

    def _calculate_node_hash(self):
        # Pobieramy hashe dzieci (jeśli istnieją)
        left_h = _______ if self.left else ""
        right_h = _______ if self.right else ""
        
        combined_data = str(self.value) + left_h + right_h
        return _______(combined_data) # shashuj

class VersionedMerkleTree:
    def __init__(self, root_value):
        # Magazyn wersji: {numer_wersji: obiekt_root}
        self.roots = {}
        self.current_version = 0
        
        # Tworzymy korzeń wersji 0
        initial_root = Node(root_value, version=_______)
        self.roots[0] = _______ # co ma być korzeniem, jaki Node

    def get_root(self, version=None):
        v = version if version is not None else self.current_version
        return self.roots.get(v)

    def update_root_value(self, new_value):
        """
        Tworzy nową wersję drzewa z nową wartością w korzeniu.
        W rzeczywistym Path Copying kopiowalibyśmy ścieżkę do liścia, 
        tutaj dla uproszczenia modyfikujemy korzeń, zachowując stare dzieci.
        """
        # 1. Zwiększ licznik wersji
        self.current_version += _______
        
        # 2. Pobierz poprzedni korzeń
        old_root = self.get_root(self.current_version - _______)
        
        # 3. Stwórz nowy węzeł (nowa wersja), który współdzieli dzieci ze starym
        new_root = Node(
            value = new_value,
            left = _______, # weź dzieci z old_root
            right = _______,
            version = _______ # aktualna wersja
        )
        
        self.roots[self.current_version] = new_root
        return new_root


# Koniec Zadań !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class TestMerkleVersioning(unittest.TestCase):
    def test_merkle_integrity(self):
        """Sprawdza, czy zmiana wartości powoduje zmianę hashu korzenia."""
        tree = VersionedMerkleTree("Stan_Poczatkowy")
        root0 = tree.get_root(0)
        initial_hash = root0.hash
        
        # Nowa wersja
        tree.update_root_value("Stan_Nowy")
        root1 = tree.get_root(1)
        
        self.assertNotEqual(initial_hash, root1.hash, "Hash powinien się zmienić!")
        self.assertEqual(root1.version, 1)

    def test_structural_sharing(self):
        """Sprawdza, czy stara wersja pozostaje nienaruszona (Persistent Data Structure)."""
        original_value = "A"
        tree = VersionedMerkleTree(original_value)
        old_root = tree.get_root(0)
        
        tree.update_root_value("B")
        
        # Wersja 0 powinna nadal istnieć i mieć starą wartość
        self.assertEqual(tree.get_root(0).value, original_value)
        self.assertEqual(tree.get_root(0).hash, old_root.hash)
        self.assertEqual(len(tree.roots), 2)

    def test_deterministic_hashing(self):
        """Dwa drzewa o tej samej strukturze i wartościach muszą mieć ten sam hash."""
        tree1 = VersionedMerkleTree("X")
        tree2 = VersionedMerkleTree("X")
        
        self.assertEqual(tree1.get_root(0).hash, tree2.get_root(0).hash)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)