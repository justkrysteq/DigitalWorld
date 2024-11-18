# Importowanie potrzebnych modułów
from Swiat.Organizmy.Zwierze import Zwierze

# Klasa dla Myszy
class Mysz(Zwierze):
    """Klasa odpowiedzialna za stworzenie Myszy"""
    # Podstawowe statystyki
    sila = 1
    inicjatywa = 6

    # def kolizja(self, organizm: object, previous_position: list[int]):
    #     super().kolizja()
    #     pass  # moze uciec na sąsiednie pole, jeśli jest wolne, chyba że wrogiem jest żmija
