try:
    import pygame as pg
    import pygame_gui as gui
    from Swiat.Swiat import Swiat
    from Swiat.Organizmy.Zwierzeta.Zwierzeta import Wilk, Owca, Lis, Mysz, Skunks
    from Swiat.Organizmy.Rosliny.Rosliny import Mlecz, Trawa, WilczeJagody

    # Klasa Game - kontener gry
    class Game:
        def __init__(self):
            # Inicjalizacja okna
            pg.init()
            pg.display.set_caption("Wirtualny Świat - NA, KS, SW")

            # Ustawienia okna
            self.screen = pg.display.set_mode((525, 630))
            self.manager = gui.UIManager((525, 630))
            try:
                self.manager.get_theme().load_theme('organizmy.json')
            except Exception as e:
                print(f"Error loading theme: {e}")

            # Rysowanie siatki 20x20
            self.N = 20
            self.table = [[None for _ in range(self.N)] for _ in range(self.N)]
            
            # for y in range(self.N):
            #     for x in range(self.N):
            #         button_rect = pg.Rect(x * 26, y * 26, 25, 25)
            #         button = gui.elements.UIButton(relative_rect=button_rect, text=" ", manager=self.manager, object_id=gui.core.ObjectID(class_id="@puste_pole"))
            #         self.table[y][x] = button

            # Przypisanie klasy Swiat
            self.swiat = Swiat(self.N) # FIXME!!!!!!

            # Rysowanie guzików
            self.next_round_button = gui.elements.UIButton(relative_rect=pg.Rect(10, 530, 150, 60), text="Wykonaj Turę", manager=self.manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            self.save_button = gui.elements.UIButton(relative_rect=pg.Rect(185, 530, 150, 60), text="Zapisz Świat", manager=self.manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            self.load_button = gui.elements.UIButton(relative_rect=pg.Rect(355, 530, 150, 60), text="Wczytaj Świat", manager=self.manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))

        def update_display(self):
            # Dictionary do przypisania odpowiednich nazw klasy stylów do klas organizmów
            class_to_name = {
                Wilk: "wilk",
                Owca: "owca",
                Lis: "lis",
                Mysz: "mysz",
                Skunks: "skunks",
                Trawa: "trawa",
                Mlecz: "mlecz",
                WilczeJagody: "wilcze_jagody"
            }

            # Wyświetlanie organizmów na podstawie tabeli organizmów z obiektu klasy Swiat
            organizmy = self.swiat.get_organizmy()
            for organizmY in range(len(organizmy)):
                for organizmX in range(len(organizmy[organizmY])):
                    # print("X:", organizmX, "Y:", organizmY)
                    class_name = class_to_name.get(type(organizmy[organizmY][organizmX])) # Przypisanie do zmiennej class_name nazwy klasy stylu z class_to_name jeśli organizm jest instancją zawartej tam klasy
                    if class_name:
                        self.add_button(organizmX, organizmY, class_name)
                        # print(self.table)
                    else:
                        self.remove_button(organizmX, organizmY) # FIXME

        # Wykonania nowej rundy
        def next_round(self):
            self.swiat.wykonajTure()
            self.update_display()

        # Zapis świata
        def save_world(self):
            pass

        # Wczytanie świata
        def load_world(self):
            pass

        # Wyświetlenie na planszy
        def add_button(self, x: int, y: int, classname: str, text: str=" "):
            self.table[y][x] = gui.elements.UIButton(relative_rect=pg.Rect(x * 26, y * 26, 25, 25), text=text, manager=self.manager, object_id=gui.core.ObjectID(class_id=f"@{classname}"))
        
        # Usuwanie z planszy
        def remove_button(self, x: int, y: int):
            self.table[y][x] = gui.elements.UIButton(relative_rect=pg.Rect(x * 26, y * 26, 25, 25), text=" ", manager=self.manager, object_id=gui.core.ObjectID(class_id="@puste_pole"))

        # Main loop gry
        def run(self) -> None:
            """
            Metoda uruchamiająca grę
            """
            clock = pg.time.Clock()
            running = True

            # Miejsce na testy
            self.swiat.dodajOrganizm(Owca, 0, 0)
            # print(self.swiat.organizmy[0][0])
            # self.swiat.dodajOrganizm(Trawa, 2, 0)
            # self.swiat.dodajOrganizm(Wilk, 4, 5)

            # Wyświetlenie początkowego stanu tabeli
            self.update_display()

            # Pętla gry
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
                                # self.swiat.organizmy[0][0].position
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
    try:
        if __name__ == "__main__":
            app = Game()
            app.run()
    except NameError as name:
        print()

except ModuleNotFoundError as module:
    print(f"Upewnij się, że masz wszystkie zależności oraz pliki, dlatego że: {module}")