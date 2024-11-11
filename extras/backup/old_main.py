import pygame as pg
import pygame_gui as gui
import random

pg.init()
screen = pg.display.set_mode((400, 500))
manager = gui.UIManager((400, 500))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Digital World")

# Dodanie presetow kwadratow do planszy
py: int = 0 # okresla y dla poszczególnych kwadratów
plansza: list[object] = [] # tablica zawierajaca kwadraty
for i in range(20):
    px: int = 0 # okresla x dla poszczególnych kwadratów
    plansza.append([])
    for j in range(20):
        plansza[i].append(pg.Rect(px, py, 20, 20))
        px += 20
    py += 20

# Nowa tura
button = gui.elements.UIButton(relative_rect=pg.Rect((150, 425), (100, 50)), text='Nowa tura', manager=manager)

# Render
while running:
    td = clock.tick(60)/1000
    # Handling eventow
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Handle button click event 
        if event.type == gui.UI_BUTTON_PRESSED: 
            if event.ui_element == button:
                print("Button clicked!")
        
        manager.process_events(event)

    screen.fill("black") # wypelnienie ekranu czarnym tlem
    manager.update(td)
    manager.draw_ui(screen)
    
    # wyrysowanie planszy (nie trzeba tego robic)
    for i in range(len(plansza)):
        px = 0
        for j in plansza[i]:
            pg.draw.rect(screen, "white", j)
            # print(f"Drawed rect in position: {px}, {py}")
            px += 20
        py += 20

    xx = random.randint(0, 19)
    xy = random.randint(0, 19)
    pg.draw.rect(screen, "green", plansza[xx][xy])

    

    # flip() the display to put your work on screen
    pg.display.flip()

    # clock.tick(60)  # limits FPS to 60

pg.quit()