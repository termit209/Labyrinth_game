# Labyrinth_game
Labyrinth_game_python

* Game flow:
  - Player's goal to find a treasure and leave the labyrinth.
  - Games starts after the labyrinth is generated.
  - Player start in a fron of exit with 3 health ponts.
  - PLayer win when the player leaves the labyrinth with a treasure through exit.
  - PLayer lose when the player loses all health points.
* Game objects:
  - Treasure.("T")
  - 5 wormholes, organized into a cyclic ordered set. Entering a wormhole moves the player into the next wormhole by index. Skipping a move while staying on the wormhole moves the player to the
  next wormhole.("H")
   - River. Has source and end. Location in a river moves the player 2 cells down a stream (maximum).("R")
   -Bear. Bear is NPC. Intearact with wormholes and river. Once bear and player step on the same cell, player becomes damaged(lose 1 health point).
* User commands:
  - Moving: "go up", "go down", "go left", "go right".
  - Skipping a turn: "skip".
  - Skip a turn and show map: "show map".