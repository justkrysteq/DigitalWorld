from Swiat.Organizmy.Zwierze import Zwierze


class Lis(Zwierze):
    sila = 3
    inicjatywa = 7

    def akcja(self):
        super().akcja()
        # jesli pole na ktore chce sie ruszyc zawiera organizm z wieksza sila to tam nie wejdzie
