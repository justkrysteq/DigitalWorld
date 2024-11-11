from Zwierze import Zwierze

class Wilk(Zwierze):
    sila = 9
    inicjatywa = 5
    img = "img/wolf.png"


class Owca(Zwierze):
    sila = 4
    inicjatywa = 4
    img = "img/owca.png"


class Lis(Zwierze):
    sila = 3
    inicjatywa = 7
    img = "img/fox.png"

    def akcja(self):
        pass  # jesli pole na ktore chce sie ruszyc zawiera organizm z wieksza sila to tam nie wejdzie


class Mysz(Zwierze):
    sila = 1
    inicjatywa = 6
    img = "img/mice.png"

    def kolizja(self):
        pass  # moze uciec na sąsiednie pole, jeśli jest wolne, chyba że wrogiem jest żmija


class Skunks(Zwierze):
    sila = 5
    inicjatywa = 5
    img = "img/skunks.png"