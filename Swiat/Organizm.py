# Importowanie modułów
from abc import ABC, abstractmethod
from random import randint


# Klasa Organizm - kontener instniejących organizmów
class Organizm(ABC):
    """Główny kontener instniejących organizmów"""

    def __init__(self, pozycja: list[int], swiat: object, wiek: int=0, alive: bool=True, omit_akcja: bool=False):
        
        # Tworzenie podstawowych pól
        self._position: list[int] = pozycja
        self._swiat: object = swiat
        self._wiek: int = wiek
        self._alive: bool = alive
        self._omit_akcja: bool = omit_akcja

    # Pobieranie wszystkich możliwych ruchów
    def get_available_positions(self) -> list[list[int]]:
        """Metoda zwracająca wszystkie ruchy, które są możliwe dla organizmu na planszy"""

        N = self._swiat.get_N()
        available_positions = []
        if self._position[0] + 1 < N:
            available_positions.append([self._position[0] + 1, self._position[1]])
        if self._position[0] - 1 >= 0:
            available_positions.append([self._position[0] - 1, self._position[1]])
        if self._position[1] + 1 < N:
            available_positions.append([self._position[0], self._position[1] + 1])
        if self._position[1] - 1 >= 0:
            available_positions.append([self._position[0], self._position[1] - 1])
        if self._position[0] + 1 < N and self._position[1] + 1 < N:
            available_positions.append([self._position[0] + 1, self._position[1] + 1])
        if self._position[0] + 1 < N and self._position[1] - 1 >= 0:
            available_positions.append([self._position[0] + 1, self._position[1] - 1])
        if self._position[0] - 1 >= 0 and self._position[1] + 1 < N:
            available_positions.append([self._position[0] - 1, self._position[1] + 1])
        if self._position[0] - 1 >= 0 and self._position[1] - 1 >= 0:
            available_positions.append([self._position[0] - 1, self._position[1] - 1])

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

    def get_sila(self) -> int:
        """
        Metoda zwracająca siłę organizmu

        :Przykład użycia:
        >>> wilk.get_sila()
        9
        """

        return self._sila

    def get_inicjatywa(self) -> int:
        """
        Metoda zwracająca inicjatywę organizmu

        :Przykład użycia:
        >>> wilk.get_inicjatywa()
        5
        """

        return self._inicjatywa

    def set_inicjatywa(self, new_inicjatywa) -> None:
        """
        Metoda ustawiająca inicjatywę organizmu

        :Przykład użycia:
        >>> wilk.set_inicjatywa(5)
        """

        self._inicjatywa = new_inicjatywa

    def get_wiek(self) -> int:
        """
        Metoda zwracająca wiek organizmu

        :Przykład użycia:
        >>> wilk.get_wiek()
        3
        """

        return self._wiek

    def get_position(self) -> list[int]:
        """
        Metoda zwracająca pozycję organizmu

        :Przykład użycia:
        >>> wilk.get_position()
        [1, 2]
        """

        return self._position
    
    def get_alive(self) -> bool:
        """
        Metoda, która zwraca czy organizm jest żywy

        :Przykład użycia:
        >>> wilk.get_alive()
        True
        """

        return self._alive
    
    def get_omit_akcja(self) -> bool:
        """
        Metoda, która zwraca czy organizm jest w stanie pomijania akcji (potrzebne do rozmnażania)

        :Przykład użycia:
        >>> wilk.get_omit_akcja()
        True
        """

        return self._alive

    def set_position(self, new_pozycja: list[int]) -> None:
        """
        Metoda ustawiająca pozycję organizmu

        :Przykład użycia:
        >>> wilk.set_position(1, 2)
        """

        self._position = new_pozycja