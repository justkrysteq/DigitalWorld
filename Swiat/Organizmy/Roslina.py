from abc import ABC
from Swiat.Exceptions import LanuchedModuleException
from Swiat.Organizm import Organizm
from random import randint


class Roslina(Organizm, ABC):
    inicjatywa: int = 0

    def akcja(self):
        # Określa akcję rośliny - możliwość rozmnażania się z pewnym prawdopodobieństwem (daliśmy 3%)
        prawdopodobienstwo = randint(0, 100)
        if prawdopodobienstwo > 97:
            available_positions = []
            possible_positions = self.get_available_positions()
            all_positions = self.swiat.get_all_positions()
            for position in possible_positions:
                if position not in all_positions:
                    available_positions.append(position)

            # Roślina rozmnaża się tylko, gdy jest na to miejsce 😎
            if len(available_positions) > 0:
                choose_position = randint(0, len(available_positions)-1)
                self.swiat.dodajOrganizm(self.__class__, available_positions[choose_position])
                print(f"{self.__class__.__name__} na polu {self.position} rozprzestrzenił się, tworząc {self.__class__.__name__} na polu {available_positions[choose_position]}")

    def kolizja(self, organizm, previous_position):
        pass
        # Rozstrzyga kolizję z innym organizmem

        # if organizm.get_sila() < self.sila:
        #     self.swiat.usun_organizm(organizm)  # Do defa to
        # else:
        #     self.swiat.usun_organizm(self)
        #     self.swiat.ruch_organizmu(organizm, self.get_pozycja())


if __name__ == "__main__":
    try:
        raise LanuchedModuleException("Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")
    except LanuchedModuleException as e:
        print(e)