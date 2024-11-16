from Swiat.Organizmy.Roslina import Roslina


class Mlecz(Roslina):
    sila = 0

    def akcja(self):
        for i in range(3):  # 3 próby rozprzestrzeniania się
            super().akcja()
