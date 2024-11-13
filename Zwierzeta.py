from Zwierze import Zwierze

class Wilk(Zwierze):
    sila = 9
    inicjatywa = 5


class Owca(Zwierze):
    sila = 4
    inicjatywa = 4


class Lis(Zwierze):
    sila = 3
    inicjatywa = 7

    def akcja(self):
        pass  # jesli pole na ktore chce sie ruszyc zawiera organizm z wieksza sila to tam nie wejdzie


class Mysz(Zwierze):
    sila = 1
    inicjatywa = 6

    def kolizja(self):
        pass  # moze uciec na sąsiednie pole, jeśli jest wolne, chyba że wrogiem jest żmija


class Skunks(Zwierze):
    sila = 5
    inicjatywa = 5

#  Przynajmniej 1 klasa bazowa po której dziedziczy bezpośrednio (w tym samym pokoleniu) kilka klas pochodnych (konieczne na >=3pkt)
#  Wielokrotne wykorzystanie kodu (kod w klasie bazowej używany przez obiekty klas pochodnych) (konieczne na >=3pkt)
#  Nadpisywanie metody klasy bazowej wraz z wywołaniem jej w implementacji klasy pochodnej (konieczne na >=4pkt)