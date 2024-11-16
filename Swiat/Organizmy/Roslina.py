from abc import ABC
from Swiat.Exceptions import LanuchedModuleException
from Swiat.Organizm import Organizm
from random import randint

class Roslina(Organizm, ABC):
    inicjatywa: int = 0
    def akcja(self):
        # Określa akcję rośliny - możliwość rozmnażania się z pewnym prawdopodobieństwem
        prawdopodobienstwo = randint(0, 100)
        if prawdopodobienstwo > 97:
            self.swiat.dodajOrganizm(self.__class__, self.get_new_position())

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