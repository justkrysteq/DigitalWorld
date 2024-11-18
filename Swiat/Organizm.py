# Importowanie modułów
from abc import ABC, abstractmethod
from random import randint
from Swiat.Exceptions import LanuchedModuleException


# Klasa Organizm - kontener instniejących organizmów
class Organizm(ABC):
    """Główny kontener instniejących organizmów"""
    def __init__(self, pozycja: list[int], swiat: object, wiek: int=0, alive: bool=True, omit_akcja: bool=False):
        # self.sila = sila # to chyba nie ma sensu tutaj, choć w pliku jest napisane, żeby było
        # self.inicjatywa = inicjatywa
        
        # Tworzenie podstawowych pól
        self.position: list[int] = pozycja
        self.swiat: object = swiat
        self.wiek: int = wiek
        self.alive: bool = alive
        self.omit_akcja: bool = omit_akcja
        # Podstawowe pola
        # sila: int = 0 # statystka siły
        # inicjatywa: int = 0 # statystyka inicjatywy
        # polozenie: list[int] = [0, 0] # położenie (x, y) na siatce
        # świat - referencja do świata w którym znajduje się organizm

    # Pobieranie wszystkich możliwych ruchów
    def get_available_positions(self) -> list[list[int]]:
        """Metoda zwracająca wszystkie ruchy, które są możliwe dla organizmu na planszy"""
        N = self.swiat.get_N()
        available_positions = []
        if self.position[0] + 1 < N:
            available_positions.append([self.position[0] + 1, self.position[1]])
        if self.position[0] - 1 >= 0:
            available_positions.append([self.position[0] - 1, self.position[1]])
        if self.position[1] + 1 < N:
            available_positions.append([self.position[0], self.position[1] + 1])
        if self.position[1] - 1 >= 0:
            available_positions.append([self.position[0], self.position[1] - 1])
        if self.position[0] + 1 < N and self.position[1] + 1 < N:
            available_positions.append([self.position[0] + 1, self.position[1] + 1])
        if self.position[0] + 1 < N and self.position[1] - 1 >= 0:
            available_positions.append([self.position[0] + 1, self.position[1] - 1])
        if self.position[0] - 1 >= 0 and self.position[1] + 1 < N:
            available_positions.append([self.position[0] - 1, self.position[1] + 1])
        if self.position[0] - 1 >= 0 and self.position[1] - 1 >= 0:
            available_positions.append([self.position[0] - 1, self.position[1] - 1])

        # 1. x+1 👍
        # 2. x-1 👍
        # 3. y+1 👍
        # 4. y-1 👍
        # 5. x+1 y+1 👍
        # 6. x+1 y-1 👍
        # 7. x-1 y+1 👍
        # 8. x-1 y-1 👍
        return available_positions

    # Pobieranie nowych pozycji organizmów
    def get_new_position(self) -> list[int]:
        """Metoda odpowiedzialna za pobieranie nowych pozycji organizmów"""
        available_positions = self.get_available_positions()
        choose_position = randint(0, len(available_positions) - 1)
        return available_positions[choose_position]

    # Podstawowe abstrakcyjne metody do dziedziczenia
    @abstractmethod
    def akcja(self):
        """Metoda ustalająca zachowanie organizmu w trakcie tury"""
        pass

    @abstractmethod
    def kolizja(self):
        """Metoda ustalająca zachowanie organizmu w trakcie kolizji"""
        pass

    # @abstractmethod
    # def rysowanie(self):
    #     """
    #     Metoda powodująca narysowanie organizmu na siatce
    #     """
    #     pass

    def get_sila(self):
        """
        Metoda zwracająca siłę organizmu

        :Przykład użycia:
        >>> wilk.get_sila()
        9
        """
        return self.sila

    # def set_sila(self, new_sila):
    #     """
    #     Metoda ustawiająca inicjatywę organizmu

    #     :Przykład użycia:
    #     >>> wilk.set_inicjatywa(9)
    #     """
    #     self.sila = new_sila

    def get_inicjatywa(self) -> int:
        """
        Metoda zwracająca inicjatywę organizmu

        :Przykład użycia:
        >>> wilk.get_inicjatywa()
        5
        """
        return self.inicjatywa

    def set_inicjatywa(self, new_inicjatywa):
        """
        Metoda ustawiająca inicjatywę organizmu

        :Przykład użycia:
        >>> wilk.set_inicjatywa(5)
        """
        self.inicjatywa = new_inicjatywa

    def get_wiek(self):
        """
        Metoda zwracająca wiek organizmu

        :Przykład użycia:
        >>> wilk.get_wiek()
        3
        """
        return self.wiek

    # def set_wiek(self, new_wiek):
    #     """
    #     Metoda ustawiająca wiek organizmu

    #     :Przykład użycia:
    #     >>> wilk.set_wiek(5)
    #     """
    #     self.wiek = new_wiek

    def get_position(self) -> list[int]:
        """
        Metoda zwracająca pozycję organizmu

        :Przykład użycia:
        >>> wilk.get_position()
        [1, 2]
        """
        return self.position
    
    def get_alive(self) -> bool:
        """
        Metoda, która zwraca czy organizm jest żywy

        :Przykład użycia:
        >>> wilk.get_alive()
        True
        """
        return self.alive
    
    def get_omit_akcja(self) -> bool:
        """
        Metoda, która zwraca czy organizm jest w stanie pomijania akcji (potrzebne do rozmnażania)

        :Przykład użycia:
        >>> wilk.get_omit_akcja()
        True
        """
        return self.alive

    def set_position(self, new_pozycja: list[int]):
        """
        Metoda ustawiająca pozycję organizmu

        :Przykład użycia:
        >>> wilk.set_position(1, 2)
        """
        self.pozycja = new_pozycja


# Wyjątek w sytuacji, gdzie został uruchomiony moduł, zamiast głównego pliku
if __name__ == "__main__":
    try:
        raise LanuchedModuleException("Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")
    except LanuchedModuleException as e:
        print(e)