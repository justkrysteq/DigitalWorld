# Import
import pygame as pg
import pygame_gui as gui
import random
# from Swiat import Swiat

# Klasa Game - kontener gry
class Game:
    def __init__(self):
        # Inicjalizacja okna
        pg.init()
        pg.display.set_caption("Wirtualny Świat - NA, KS, SW")

        # Ustawienia okna
        self.screen = pg.display.set_mode((525, 630))
        self.manager = gui.UIManager((525, 630))

        # Przypisanie klasy Swiat
        # self.swiat = Swiat() # FIXME!!!!!!

        # Rysowanie siatki 20x20
        self.table = [[None for _ in range(20)] for _ in range(20)]
        
        for i in range(20):
            for j in range(20):
                button_rect = pg.Rect(i * 26, j * 26, 25, 25)
                button = gui.elements.UIButton(relative_rect=button_rect, text=" ", manager=self.manager)
                self.table[i][j] = button

        # Rysowanie guzików
        self.next_round_button = gui.elements.UIButton(relative_rect=pg.Rect(10, 530, 150, 60), text="Wykonaj Turę", manager=self.manager)
        self.save_button = gui.elements.UIButton(relative_rect=pg.Rect(185, 530, 150, 60), text="Zapisz Świat", manager=self.manager)
        self.load_button = gui.elements.UIButton(relative_rect=pg.Rect(355, 530, 150, 60), text="Wczytaj Swiat", manager=self.manager)

    # Wykonania nowej rundy
    def next_round(self):
        self.swiat.wykonajTure()

    # Zapis świata
    def save_world(self):
        pass

    # Wczytanie świata
    def load_world(self):
        pass

    # Main loop gry
    def run(self):
        clock = pg.time.Clock()
        running = True
        
        while running:
            time_delta = clock.tick(60) / 1000.0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.USEREVENT:
                    if event.user_type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.next_round_button:
                            self.next_round()
                            print("next tura")
                        elif event.ui_element == self.save_button:
                            self.save_world()
                            print("zapisaned")
                        elif event.ui_element == self.load_button:
                            self.load_world()
                            print("wczytaned")
                self.manager.process_events(event)
                
            self.manager.update(time_delta)
            self.screen.fill((0, 0, 0))
            self.manager.draw_ui(self.screen)

            pg.display.update()

# Uruchamianie gry
if __name__ == "__main__":
    app = Game()
    app.run()
