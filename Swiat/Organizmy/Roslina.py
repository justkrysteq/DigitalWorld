# Import potrzebnych modułów
from abc import ABC
from Swiat.Organizm import Organizm
from random import randint


# Klasa Roslina - kontener wszystkich Roślin
class Roslina(Organizm, ABC):
    """Klasa odpowiedzialna za przechowywanie wszystkich Roślin"""

    _inicjatywa: int = 0

    # Wykonanie akcji roślin
    def akcja(self, all_positions: list[list[int]], *args) -> None:
        """Metoda wykonująca akcję dla rośliny"""

        # Możliwość rozmnażania się z pewnym prawdopodobieństwem (daliśmy 3%)
        prawdopodobienstwo = randint(0, 100)
        if prawdopodobienstwo > 97:
            available_positions = []
            possible_positions = self.get_available_positions()
            for position in possible_positions:
                if position not in all_positions:
                    available_positions.append(position)

            # Roślina rozmnaża się tylko, gdy jest na to miejsce 😎
            if len(available_positions) > 0:
                choose_position = randint(0, len(available_positions)-1)
                self._swiat.dodajOrganizm(self.__class__, available_positions[choose_position])
                self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {self._position} rozprzestrzenił się, tworząc {self.__class__.__name__} na polu {available_positions[choose_position]}")
            else:
                self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {self._position} nie dał rady się rozprzestrzenić")
        else:
            self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {self._position} nie dał rady się rozprzestrzenić")

    # Kolizja dla roślin (puste, brak kolizji dla roślin)
    def kolizja(self, *args) -> None:
        pass