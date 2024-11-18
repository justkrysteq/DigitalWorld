from Swiat.Organizmy.Roslina import Roslina


class Mlecz(Roslina):
    sila = 0

    def akcja(self, all_positions: list[list[int]], *args):
        for _ in range(3):  # 3 próby rozprzestrzeniania się
            super().akcja(all_positions)
