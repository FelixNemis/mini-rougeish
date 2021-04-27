from constants import *

from offset import OffsetGroup
from sprite import BasicSprite

class TileMap:
    def __init__(self):
        #self.chunks = {}

        self.tiles = {}

        self.sprite_container = OffsetGroup()

        #display is currently 200x150
        offset_x, offset_y = get_screen_center_offset()
        self.set_origin(offset_x, offset_y)

    def set_origin(self, x, y):
        self.x_origin = x
        self.y_origin = y
        self.sprite_container.set_camera_offset(x, y)

    def place_tile(self, x, y, visible=True, tile_img = 'floor'):
        self.clear_tile(x, y)
        if y not in self.tiles:
            self.tiles[y] = {}
        sp = BasicSprite(tile_img, visible)
        sp.set_pos(x * 14, y * 14)
        self.sprite_container.add(sp)
        self.tiles[y][x] = sp

    def clear_tile(self, x, y):
        if y in self.tiles and x in self.tiles[y]:
            self.tiles[y][x].kill()
            del self.tiles[y][x]

    def get_tile(self, x, y):
        if y not in self.tiles or x not in self.tiles[y]:
            return False

        return self.tiles[y][x]
    
    def render(self, camera, surface):
        self.sprite_container.set_offset(camera)
        self.sprite_container.draw(surface)

