# DigitalWorld

A pygame game created as a school project.

## 🎯 About

**DigitalWorld** is a simulator of a virtual world, represented as a two-dimensional grid of size NxN (default 20x20). Within this environment, various life forms with distinct behaviors interact and reproduce. The simulation operates on a turn-based system, where, in each cycle, every organism performs an action based on its type. Animal organisms typically move, while plant organisms remain stationary. 

Collisions occur when two organisms occupy the same cell. In such cases, one organism prevails, either by eliminating the opponent (e.g., a wolf attacking a prey) or by fleeing (e.g., a mouse escaping a predator). The movement order is determined by the initiative of the organisms, with those having the highest initiative acting first. In the event that multiple animals share the same initiative, the sequence is further resolved based on seniority, where the older organism moves first. In instances where two organisms are equally strong, the winner is decided by the initiator of the conflict.

Upon program initialization, the simulator spawns two organisms of each type. These organisms are positioned on the grid at random locations. Additionally, the program window features a dedicated field that provides real-time updates on events such as combat outcomes, plant consumption, and other significant occurrences within the world.

Furthermore, DigitalWorld allows users to save the current state of the world to a file, preserving the positions and statuses of all organisms. This saved state can later be loaded, enabling users to resume simulations from a previous point in time or analyze the progression of the ecosystem over multiple sessions.

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
