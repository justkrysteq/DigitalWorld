import Zwierze

class Wilk(Zwierze):
    sila = 9
    inicjatywa = 5

class Owca(Zwierze):
    sila = 4
    inicjatywa = 4

class Lis(Zwierze):
    sila = 3
    inicjatywa = 7
    
    def akcja():
        pass # jesli pole na ktore chce sie ruszyc zawiera organizm z wieksza sila to tam nie wejdzie

class Mysz(Zwierze):
    sila = 1
    inicjatywa = 6
    
    def kolizja():
        pass # moze uciec na sąsiednie pole, jeśli jest wolne, chyba że wrogiem jest żmija

class Skunks(Zwierze):
    sila = 5
    inicjatywa = 5