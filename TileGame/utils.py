import pygame
import math

def rect_from_corners(corn1, corn2):
    xs = [corn1[0], corn2[0]]
    ys = [corn1[1], corn2[1]]
    left = min(xs)
    top = min(ys)
    bottom = max(ys)
    right = max(xs)
    width = right-left
    height = bottom-top
    return pygame.Rect(left,top, width, height)


def screen_pos_to_tile(pos, tile_size, offset):
    return (math.floor((pos[0] - offset[0]) / tile_size[0]),
                    math.floor((pos[1] - offset[1]) / tile_size[1]))