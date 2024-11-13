from Roslina import Roslina

class Trawa(Roslina):
    sila = 0


class Mlecz(Roslina):
    sila = 0

    def akcja(self):
        pass  # trzy próby rozprzestrzeniania się w jednej turze


class WilczeJagody(Roslina):
    sila = 0

    def kolizja(self):
        pass  # zwierze, które zjadło tą roślinę ginie

#  Przynajmniej 1 klasa bazowa po której dziedziczy bezpośrednio (w tym samym pokoleniu) kilka klas pochodnych (konieczne na >=3pkt)
#  Wielokrotne wykorzystanie kodu (kod w klasie bazowej używany przez obiekty klas pochodnych) (konieczne na >=3pkt)
#  Nadpisywanie metody klasy bazowej wraz z wywołaniem jej w implementacji klasy pochodnej (konieczne na >=4pkt)