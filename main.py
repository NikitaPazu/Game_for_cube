import pygame

from Sprites.Enemy_SpaceShip import Enemy_Spaceship
from Sprites.Spacehip import Spaceship
from Sprites.Enemy_space_ship_bullet import Enemy_Space_ship_bullet
from Sprites.Spaceship_bullet import Spaceship_bullet
import file_utils


config = file_utils.read_config_json()

pygame.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 60)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)

Spaceship = Spaceship()
Enemy_Spaceship = Enemy_Spaceship()
Spaceship_bullet = Spaceship_bullet()
Enemy_Space_ship_bullet = Enemy_Space_ship_bullet()


Spaceship_group = pygame.sprite.Group()
Enemy_spaceship_group = pygame.sprite.Group()


Spaceship_group.add(Spaceship)
Spaceship_group.add(Spaceship_bullet)

Enemy_spaceship_group.add(Enemy_Spaceship)
Enemy_spaceship_group.add(Enemy_Space_ship_bullet)



running = True

clock = pygame.time.Clock()

while running:
    clock.tick(config['framerate'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            obj = Spaceship.to_dict()
            file_utils.write_json(obj)
            running = False
    Spaceship_group.update()
    Enemy_spaceship_group.update()

screen.fill(config['colors']['white'])
# Spaceship_group.add(Spaceship)

pygame.display.flip()

pygame.quit()
clock = pygame.time.Clock()
