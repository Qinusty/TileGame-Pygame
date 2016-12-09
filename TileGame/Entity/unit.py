import pygame

from TileGame.World.grid import BLACK, RED, WHITE


class Unit:
    def __init__(self, tile_pos, tile_size, speed, speed_mod=1):
        self._speed = speed
        self._speed_mod = speed_mod
        self._x, self._y = (tile_pos[0]*tile_size[0], tile_pos[1]*tile_size[1])
        self._moving_to = None
        self._rect = pygame.Rect(self._x, self._y, 1, 1)
        self._selected = False

    def update(self):
        if self._moving_to is not None:
            self.move()

    def move_to(self, new_pos, tile_size):
        self._moving_to = (new_pos[0]*tile_size[0], new_pos[1]*tile_size[1])

    def move(self):
        move_dist = self._speed * self._speed_mod
        if self._x != self._moving_to[0]:
            distance_to = self._moving_to[0] - self._x
            if abs(distance_to) < move_dist:
                self._x = self._moving_to[0]
            else:
                if distance_to > 0:
                    self._x += move_dist
                elif distance_to < 0:
                    self._x -= move_dist
        if self._y != self._moving_to[1]:
            distance_to = self._moving_to[1] - self._y
            if abs(distance_to) < move_dist:
                self._y = self._moving_to[1]
            else:
                if distance_to > 0:
                    self._y += move_dist
                elif distance_to < 0:
                    self._y -= move_dist
        if self._x == self._moving_to[0] and self._y == self._moving_to[1]:
            self._moving_to = None

    def draw(self, surface, tile_size, offset):
        self._rect = pygame.Rect(self._x + int(tile_size[0]/4) + offset[0], self._y + int(tile_size[1]/4) + offset[1],
                           int(tile_size[0]/2), int(tile_size[1]/2))
        pygame.draw.rect(surface, WHITE, self._rect)
        if self._selected:
            pygame.draw.rect(surface, BLACK, self._rect, 5)
