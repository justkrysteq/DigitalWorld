from abc import ABC
from Organizm import Organizm
from random import randint

class Roslina(ABC, Organizm):
    def akcja(self):
        # Określa akcję rośliny - możliwość rozmnażania się z pewnym prawdopodobieństwem
        prawdopodobienstwo = randint(0, 100)
        if prawdopodobienstwo > 97:
            # wolna_pozycja = self.swiat.losuj_wolne_pole(self.pozycja) # wolna pole 
            ...

    def kolizja(self, organizm):
        # Rozstrzyga kolizję z innym organizmem

        if organizm.get_sila() < self.sila:
            self.swiat.usun_organizm(organizm)  # Do defa to
        else:
            self.swiat.usun_organizm(self)
            self.swiat.ruch_organizmu(organizm, self.get_pozycja())