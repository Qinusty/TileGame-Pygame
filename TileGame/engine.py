import pygame
import math

from TileGame.World.camera import Camera

from TileGame.Entity.unit import Unit
from TileGame.World.grid import Grid, DARKGRAY
from TileGame.utils import rect_from_corners, screen_pos_to_tile
from TileGame.UI.overlay import Overlay


class Engine:
    def __init__(self, window_width, window_height, num_cols, num_rows):
        self._game_obj = pygame.init()
        self._tick_rate = 60
        self._window_size = (window_width, window_height)
        self._keys = pygame.key.get_pressed()
        self._clock = pygame.time.Clock()
        self._caption = "Default Engine! [ %0.2f fps ]"
        pygame.display.set_mode(self._window_size, pygame.DOUBLEBUF|pygame.HWSURFACE)
        pygame.display.set_caption(self._caption % 0)
        self._surface = pygame.display.get_surface()
        self._quit = False

        self._camera = Camera()

        self._left_click_at = None
        self.overlay = Overlay()
        self._grid = Grid((window_width, window_height), num_rows, num_cols)
        self._tile_size = self._grid._tile_size
        self._units = set()
        self._selected_units = set()

        unit_speed = max(self._tile_size) / self._tick_rate
        self._units.add(Unit((0, 0), self._tile_size, unit_speed))
        self._units.add(Unit((8, 7), self._tile_size, unit_speed, 2.5))

    def event_loop(self):
        self._keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self._keys[pygame.K_ESCAPE]:
                self._quit = True

            # ALL MOUSE BUTTON EVENTS
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # LEFT CLICK
                    if event.type == pygame.MOUSEBUTTONDOWN and self._left_click_at is None:  # no current selection
                        self._left_click_at = pygame.mouse.get_pos()
                    elif event.type == pygame.MOUSEBUTTONUP and self._left_click_at is not None:  # ongoing selection
                        rect = rect_from_corners(self._left_click_at, pygame.mouse.get_pos())
                        self.select_units_in_rect(rect)
                        self._left_click_at = None

                if event.button == 3:  # RIGHT CLICK
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.move_sel_units(screen_pos_to_tile(pygame.mouse.get_pos(),
                                                               self._tile_size, self._camera.get_offset()))

    def update(self):
        self._camera.update(self._keys)
        # update units
        for unit in self._units:
            unit.update()
            unit._selected = False
        for unit in self._selected_units:
            unit._selected = True
        self._grid.update(self._keys)

    def draw(self):
        self._grid.draw(self._surface, self._camera.get_offset())
        [unit.draw(self._surface, self._tile_size, self._camera.get_offset()) for unit in self._units]

        # selection rect #TODO: move to Overlay
        if self._left_click_at is not None:
            rect = rect_from_corners(self._left_click_at, pygame.mouse.get_pos())
            s = pygame.Surface(rect.size)
            s.fill(DARKGRAY)
            s.set_alpha(128)
            self._surface.blit(s, rect.topleft)

    def display_fps(self):
        pygame.display.set_caption(self._caption % self._clock.get_fps())

    def move_sel_units(self, new_tile):
        print("Click at: ", new_tile)
        for unit in self._selected_units:
            unit.move_to(new_tile, self._tile_size)

    def cycle(self):
        while not self._quit:
            self.event_loop()
            self.update()
            self.draw()
            self.display_fps()
            pygame.display.flip()
            self._clock.tick(self._tick_rate)

    def select_units_in_rect(self, sel_rect):
        if not self._keys[pygame.K_LSHIFT]:
            self._selected_units.clear()
        for unit in self._units:
            if sel_rect.colliderect(unit._rect):
                if unit in self._selected_units:
                    self._selected_units.remove(unit)
                else:
                    self._selected_units.add(unit)


if __name__ == '__main__':
    e = Engine(1200, 800, 10, 10)
    e.cycle()