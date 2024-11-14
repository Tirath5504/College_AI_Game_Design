# AI Tom and Jerry Game

## Overview

AI Predator and Prey is an interactive game where the player controls the prey (Jerry) and tries to evade the predator (Tom) for 30 seconds. The predator uses A* pathfinding algorithm to chase the prey when within range, creating an engaging chase-and-escape experience.

## Features

- **AI Predator**: Tom uses A* algorithm for intelligent pursuit
- **Player-Controlled Prey**: Control Jerry using arrow keys
- **Dynamic Obstacles**: Randomly generated obstacles for added challenge
- **Survival Timer**: 30-second survival challenge
- **Interactive UI**: Start screen with countdown and end game results
- **Grid-Based Movement**: Strategic movement system on a NetworkX grid

## Prerequisites

- Python 3.x
- Pygame library
- NetworkX library

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

1. Run the game:
   ```bash
   python game.py
   ```

2. Use arrow keys to control Jerry and evade Tom for 30 seconds to win!

## Game Components

### Game Flow
1. **Start Screen**
   - Game title and instructions
   - Countdown timer
   - Control explanations

2. **Main Gameplay**
   - Grid-based movement system
   - Real-time predator pursuit
   - Obstacle navigation
   - 30-second survival timer

3. **End Screen**
   - Victory message (30-second survival)
   - Defeat message (caught by predator)

### Technical Implementation

#### Grid System
- NetworkX-based 2D grid
- Randomly generated obstacles
- Four-directional movement (up, down, left, right)

#### AI Behavior
- A* pathfinding algorithm for predator movement
- Dynamic path recalculation
- Range-based pursuit initiation

#### Player Controls
- **↑**: Move up
- **↓**: Move down
- **←**: Move left
- **→**: Move right

## Requirements File

Create a `requirements.txt` with:
```
pygame==2.4.0
networkx==3.0
```

## Game Mechanics

### Predator (Tom)
- Uses A* pathfinding for intelligent pursuit
- Continuously updates path to prey
- Triggers game over on contact

### Prey (Jerry)
- Player-controlled movement
- Cannot pass through obstacles
- Must survive for 30 seconds

### Obstacles
- Randomly generated on game start
- Block movement for both characters
- Create strategic escape opportunities

## Tips for Players

1. Use obstacles strategically for evasion
2. Keep moving to avoid being cornered
3. Watch the timer while planning escape routes
4. Stay aware of Tom's pathfinding behavior

## Technical Notes

- Game uses NetworkX for grid management and pathfinding
- Pygame handles rendering and input
- A* algorithm ensures efficient predator pursuit
- Grid-based collision detection system
