# Import potrzebnych modułów
from abc import ABC
from Swiat.Exceptions import LanuchedModuleException
from Swiat.Organizm import Organizm
from random import randint


# Klasa Roslina - kontener wszystkich Roślin
class Roslina(Organizm, ABC):
    """Klasa odpowiedzialna za przechowywanie wszystkich Roślin"""
    inicjatywa: int = 0

    # Wykonanie akcji roślin
    def akcja(self, all_positions: list[list[int]], *args):
        # Określa akcję rośliny - możliwość rozmnażania się z pewnym prawdopodobieństwem (daliśmy 3%)
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
                self.swiat.dodajOrganizm(self.__class__, available_positions[choose_position])
                self.swiat.game.narratorLog(f"{self.__class__.__name__} na polu {self.position} rozprzestrzenił się, tworząc {self.__class__.__name__} na polu {available_positions[choose_position]}")

    # Kolizja dla roślin (puste, brak kolizji dla roślin)
    def kolizja(self, *args) -> None:
        pass

# Wyjątek w sytuacji, gdzie został uruchomiony moduł, zamiast głównego pliku
if __name__ == "__main__":
    try:
        raise LanuchedModuleException("Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")
    except LanuchedModuleException as e:
        print(e)