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

font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)
Spaceship = Spaceship()
enemy_spaceship = Enemy_Spaceship()
# Spaceship_bullet = Spaceship_bullet()
Enemy_Space_ship_bullet = Enemy_Space_ship_bullet()
Space = Space("Sprites/Assets/Space.jpg",
              Sprites.Space)

Space_group = pygame.sprite.Group()
Spaceship_group = pygame.sprite.Group()
Enemy_spaceship_group = pygame.sprite.Group()

Spaceship_group.add(Spaceship)
# Spaceship_group.add(Spaceship_bullet)

Enemy_spaceship_group.add(enemy_spaceship)
# Enemdy_spaceship_group.add(Enemy_Space_ship_bullet)

Space_group.add(Space)

running = True

clock = pygame.time.Clock()
cooldown = 0
ticks = 0
score = 0

while running:
    clock.tick(config['framerate'])
    ticks += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            obj = Spaceship.to_dict()
            file_utils.write_json(obj)
            running = False
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and ticks - cooldown >= 25:
        cooldown = ticks
        spaceship_bullet = Spaceship_bullet(x=Spaceship.rect.center[0])
        Spaceship_group.add(spaceship_bullet)

    hits = pygame.sprite.groupcollide(Spaceship_group, Enemy_spaceship_group, True, True)
    if hits:
        Enemy_spaceship_group.remove(enemy_spaceship)
        enemy_spaceship = Enemy_Spaceship()
        Enemy_spaceship_group.add(enemy_spaceship)
        score += 1
    if score >= 10:
        pygame.quit()


    Spaceship_group.update(Spaceship, Spaceship_bullet)
    Enemy_spaceship_group.update(enemy_spaceship, Enemy_Space_ship_bullet)
    Space_group.update()

    Score_render = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(Space.image, Space.rect)
    Spaceship_group.draw((screen))
    Enemy_spaceship_group.draw((screen))
    screen.blit(Score_render, (10, 10))
    pygame.display.flip()

# Spaceship_group.add(Spaceship)

pygame.quit()

