from Swiat.Organizmy.Zwierze import Zwierze


class Lis(Zwierze):
    sila = 3
    inicjatywa = 7

    # Zależy jak jest zgodnie z najlepszymi praktykami programowania obiektowego

    # def __init__(self, pozycja, swiat, wiek = 0, alive = True, rozmnozyc = False):
    #     super().__init__(pozycja, swiat, wiek, alive, rozmnozyc)
    #     self.sila = 3
    #     self.inicjatywa = 7

    def akcja(self):
        super().akcja()
        # jesli pole na ktore chce sie ruszyc zawiera organizm z wieksza sila to tam nie wejdzie
