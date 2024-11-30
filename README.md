# DigitalWorld

A simple game created as a school project.

## 🎯 About

**DigitalWorld** is a simple simulator of a virtual world that consists of a two-dimensional grid of size NxN (default 20x20). In this world, simple life forms with different behaviors exist. The simulator is turn-based. In each turn, all organisms present in the world perform an action appropriate to their type. Some of them will move (animal organisms), while others will remain stationary (plant organisms). In case of a collision (when one organism occupies the same cell as another), one of the organisms wins by either killing (e.g., a wolf) the opponent or by running away (e.g., a mouse). The order of movement for organisms in a turn depends on their initiative. Animals with the highest initiative move first. In the case of animals with the same initiative, the order is determined by the rule of seniority (the older animal moves first). In the case of equal strength, the winner is the organism that initiated the attack. Upon starting the program, the grid displays each organism twice. The program window contains a field displaying information about the results of fights, plant consumption, and other events occurring in the world.

## 🚀 Getting Started
### Dependencies

* **Python** 3.12.0
* **pygame-ce** 2.5.2
* **pygame_gui** 0.6.12

### Installing

* Download ZIP
* Unpack

### Executing program

* Run **main.py**
