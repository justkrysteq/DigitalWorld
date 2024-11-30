# Importowanie potrzebnych modułów
from Swiat.Organizmy.Roslina import Roslina

# Klasa dla Mlecza
class Mlecz(Roslina):
    """Klasa odpowiedzialna za stworzenie Mlecza"""

    _sila = 0

    # Podejmuje trzy próby rozprzestrzeniania w jednej turze
    def akcja(self, all_positions: list[list[int]], *args) -> None:
        """Metoda wykonująca unikalną akcję dla Mlecza"""

        for _ in range(3):  # 3 próby rozprzestrzeniania się
            super().akcja(all_positions)