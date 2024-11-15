from Swiat.Organizmy.Zwierze import Zwierze

class Mysz(Zwierze):
    sila = 1
    inicjatywa = 6

    def kolizja(self):
        pass  # moze uciec na sąsiednie pole, jeśli jest wolne, chyba że wrogiem jest żmija

