# Importowanie potrzebnych modułów
from Swiat.Organizmy.Zwierze import Zwierze
from random import randint

# Klasa dla Lisa
class Lis(Zwierze):
    """Klasa odpowiedzialna za stworzenie Lisa"""

    # Podstawowe statystyki
    _sila = 3
    _inicjatywa = 7

    # Dobry węch: lis nigdy nie ruszy się na pole zajmowane przez organizm silniejszy niż on
    def akcja(self, all_positions: list[list[int]], *args) -> None:
        """Metoda wykonująca unikalną akcję dla Lisa"""

        if not self._omit_akcja:
            available_positions = [] # tu będą pozycje na których nie ma organizmu z większą siłą od lisa (czyli puste lub z mniejszą siłą)
            possible_positions = self.get_available_positions() # tu są wszystkie ruchy jakie mógłby wykonać
            for position in possible_positions:
                if position in all_positions and position is not None:
                    [x, y] = position
                    organizm = self._swiat._organizmy[y][x]

                    # Sprawdzanie czy organizm na tej pozycji na większą siłę niż lis, jeśli tak to się tam nie ruszy
                    if organizm is not None and self._sila >= organizm._sila:
                        available_positions.append(position)
                else:
                    available_positions.append(position)

            if len(available_positions) > 0:
                choose_position = randint(0, len(available_positions)-1)
                self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {self._position} przeszedł na pole {available_positions[choose_position]}, unikając ewentualnego zagrożenia")
                self._position = available_positions[choose_position]