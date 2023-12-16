import pygame
import file_utils
import Sprites

from Sprites.Spacehip import Spaceship
from Sprites.Spaceship_bullet import Spaceship_bullet

from Sprites.Enemy_SpaceShip import Enemy_Spaceship
from Sprites.Enemy_space_ship_bullet import Enemy_Space_ship_bullet

from Sprites.Space import Space

config = file_utils.read_config_json()

bg = pygame.image.load("Sprites/Assets/space.jpg")

pygame.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 60)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)
Spaceship = Spaceship()
Enemy_Spaceship = Enemy_Spaceship()
# Spaceship_bullet = Spaceship_bullet()
Enemy_Space_ship_bullet = Enemy_Space_ship_bullet()
Space = Space("Sprites/Assets/Space.jpg",
              Sprites.Space)

Space_group = pygame.sprite.Group()
Spaceship_group = pygame.sprite.Group()
Enemy_spaceship_group = pygame.sprite.Group()

Spaceship_group.add(Spaceship)
# Spaceship_group.add(Spaceship_bullet)

Enemy_spaceship_group.add(Enemy_Spaceship)
# Enemdy_spaceship_group.add(Enemy_Space_ship_bullet)

Space_group.add(Space)

running = True

clock = pygame.time.Clock()
cooldown = 0
ticks = 0

while running:
    clock.tick(config['framerate'])
    ticks += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            obj = Spaceship.to_dict()
            file_utils.write_json(obj)
            running = False
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and ticks - cooldown >= 60:
        cooldown = ticks
        spaceship_bullet = Spaceship_bullet(x=Spaceship.rect.center[0])
        Spaceship_group.add(spaceship_bullet)

    pygame.display.flip()
    Spaceship_group.update(Spaceship, Spaceship_bullet)
    Enemy_spaceship_group.update(Enemy_Spaceship, Enemy_Space_ship_bullet)
    Space_group.update()
    screen.blit(Space.image, Space.rect)
    Spaceship_group.draw((screen))
    Enemy_spaceship_group.draw((screen))

# Spaceship_group.add(Spaceship)

pygame.display.flip()

pygame.quit()
clock = pygame.time.Clock()

# screen.fill(config['colors']['black'])  # вот это не работало (насколько я понял)
# Enemy_Spaceship.image, Enemy_Spaceship.rect
