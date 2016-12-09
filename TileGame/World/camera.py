import pygame


class Camera:
    def __init__(self, scroll_speed=1, offset=(0,0)):
        self._offset_x, self._offset_y = offset
        self._scroll_speed = scroll_speed

    def update(self, keys):
        SCROLL_VAL = 1
        if keys[pygame.K_UP]:
            self._offset_y -= SCROLL_VAL
        if keys[pygame.K_DOWN]:
            self._offset_y += SCROLL_VAL
        if keys[pygame.K_LEFT]:
            self._offset_x -= SCROLL_VAL
        if keys[pygame.K_RIGHT]:
            self._offset_x += SCROLL_VAL

    def get_offset(self):
        return self._offset_x, self._offset_y