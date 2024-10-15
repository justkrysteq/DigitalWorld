import Roslina

class Trawa(Roslina):
    sila = 0

class Mlecz(Roslina):
    sila = 0
    
    def akcja():
        pass # trzy próby rozprzestrzeniania się w jednej turze

class WilczeJagody(Roslina):
    sila = 0
    
    def kolizja():
        pass # zwierze, które zjadło tą roślinę ginie