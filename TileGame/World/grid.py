#            R    G    B
import random

import math

import pygame

from TileGame.World.tile import Tile

WHITE    = (255, 255, 255)
DARKGRAY = ( 70,  70,  70)
BLACK    = (  0,   0,   0)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)

COLS = [ORANGE, RED, PURPLE, BLUE]

class Grid:
    def __init__(self, wh, num_cols, num_rows):
        self._width, self._height = wh
        self._tiles = []
        self._tile_size = math.ceil(self._width/num_cols), math.ceil(self._height/num_rows)
        self._offset_x = 0
        self._offset_y = 0
        for x in range(num_cols):
            col = []
            for y in range(num_rows):
                col.append(Tile(random.choice(COLS), self._tile_size))
            self._tiles.append(col)

    def shuffle_colours(self):
        for col in self._tiles:
            for tile in col:
                tile._col = random.choice(COLS)

    def update(self, keys):
        if keys[pygame.K_SPACE]:
            self.shuffle_colours()
        pass

    def draw(self, surface, offset):
        surface.fill(WHITE)
        for col in range(len(self._tiles)):
            for row in range(len(self._tiles[0])):
                self._tiles[col][row].draw(surface, col, row, offset)