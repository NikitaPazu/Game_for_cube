# import random
# import math
#
# from pygame.sprite import Group
# from Sprites.MapSprite import Wall, Ground
#
# import Sprites.MapSprite
#
#
# def get_random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     return r, g, b
#
#
# def get_lenght(x1, y1, x2, y2):
#     x = (x1 - x2) ** 2
#     y = math.pow(y1 - y2, 2)
#     return math.sqrt(x + y)
#
#
# def generate_walls(__map):
#     count = 0
#
#     while count != 128:
#         x, y = random.randint(0, 31), random.randint(0, 31)
#         row = list(__map[y])
#         element = row[x]
#
#         if type(element) == Ground:
#             wall = Wall()
#             wall.rect = element.rect
#             count += 1
#             __map[y].remove(element)
#             __map[y].add(wall)