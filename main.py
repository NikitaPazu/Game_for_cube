import pygame

from Sprites.Enemy_SpaceShip import Enemy_Spaceship
from Sprites.Spacehip import Spaceship
import file_utils


config = file_utils.read_config_json()

pygame.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 60)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)

Spaceship = Spaceship()
Enemy_Spacehip = Enemy_Spaceship()
Spaceship_group = pygame.sprite.Group()
Enemy_spaceship_group = pygame.sprite.Group()
Spaceship_group.add(Spaceship)
Enemy_spaceship_group.add(Enemy_Spaceship)





# clock = pygame.time.Clock()
running = True

# while running:
#     clock.tick(config['framerate'])
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             obj = car.to_dict()
#             file_utils.write_json(obj)
#             running = False
#     car_group.update()

screen.fill(config['colors']['white'])
Spaceship_group.add(Spaceship)

pygame.display.flip()

pygame.quit()