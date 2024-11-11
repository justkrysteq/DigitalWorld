from Roslina import Roslina


class Trawa(Roslina):
    sila = 0
    img = "img/trawa.png"


class Mlecz(Roslina):
    sila = 0
    img = "img/mlecz.png"

    def akcja(self):
        pass  # trzy próby rozprzestrzeniania się w jednej turze


class WilczeJagody(Roslina):
    sila = 0
    img = "img/wilcze_jagody.png"

    def kolizja(self):
        pass  # zwierze, które zjadło tą roślinę ginie
