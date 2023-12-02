# from pygame.sprite import Sprite
# from pygame import Surface
# import config
#
#
# class MapSprite(Sprite):
#     def __init__(self, color):
#         super().__init__()
#         self.image = Surface(
#             (config.CELL_SIZE, config.CELL_SIZE)
#         )
#         self.image.fill(color)
#         self.rect = self.image.get_rect()
#
#         self.is_wall = False
#         self.name = ""
#
#
# class Ground(MapSprite):
#     x = 0
#     y = 0
#
#     def __init__(self):
#         super().__init__(config.COLORS["Green"])
#         self.name = "Ground"
#         self.rect.x = Ground.x
#         self.rect.y = Ground.y
#         Ground.x += config.CELL_SIZE
#         if Ground.x == config.WIDTH:
#             Ground.x = 0
#             Ground.y += config.CELL_SIZE
#
#
# class Wall(MapSprite):
#     def __init__(self):
#         super().__init__((168, 74, 50))
#         self.name = "Wall"
#         self.is_wall = True