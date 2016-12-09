import pygame



class Tile:
    def __init__(self, colour, size):
        self._col = colour
        self._size = size

    def draw(self, surface, x, y, offset):
        rect = pygame.Rect(x*self._size[0] + offset[0],
                           y*self._size[1] + offset[1],
                           self._size[0], self._size[1])
        surface.fill(self._col, rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 1)
