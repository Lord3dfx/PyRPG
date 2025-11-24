<h1 align="center">PyRPG</h1>


### Current version: 0.1.1

This is a pet project I'm working on for fun.

Updates will be coming soon!

INSTALLING:

1. Clone repository:
```bash
git clone https://github.com/Lord3dfx/PyRPG
cd PyRPG
```
2. Install venv
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```
3.  dependecies
``` bash
pip install -r requirements.txt
```
4. Run project
```bash
python main.py
```
# Planned for v0.2:
Now it's time to focus on improving the game. Many bugs are due to my lack of experience in programming, so they will disappear over time.

In version 0.2, I plan to add more items (consumables, equipable items, artifacts), more unique monsters, more battle variety, and, of course, classes and races. But first of all, I will still focus on fixing bugs. 

## What's in v0.1.1:
- Fixed error with monster's position in dungeon. Now you will fight with right monster

## What's in v0.1.0:
- Added equipment for player! The only way to add equipable item is still debug menu, but soon they will be added as loot
- Added bonus stats for player. They calculate from equipable items
- Added armor for player. Now, monster damage is reduced by the player's armor amount.
- Now, if you die in the dungeon, you will lose all of your items
- Fixed bug with items' stacking
- Fixed bug with player HP, when it was below zero and player was still alive
- Fixed bugs with monsters' damage
- Rework "player's dead" function
- fixed some minor bugs

## What's in v0.0.3:
- Upgrade dungeon generation, now it's may have from 1 to 5 options
- Now added some traps and mimic chests in dungeon, be careful
- Fixed some minor and major bugs

## What's in v0.0.2:
- Reworked Player's class
- Correct leveling for player
- Fixed some minor bugs  

## What's in v0.0.1:
- Player creation with name and race selection
- Traveling through dungeons (needs improvement)
- Fighting monsters
- Gaining XP and leveling up
- Debug menu (will be disabled in future versions)

