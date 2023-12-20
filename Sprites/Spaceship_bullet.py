import time

from Sprites.Spacehip import *
import pygame
import file_utils

config = file_utils.read_config_json()


class Spaceship_bullet(pygame.sprite.Sprite):
    def __init__(self, *groups, x: int):
        super().__init__(*groups)

        self.images = [
            pygame.image.load("Sprites/Assets/spaceship_bullet.png")
        ]
        self.images = list(map(
            lambda x: pygame.transform.scale(
                pygame.transform.rotate(x, 180),
                (230 // 4, 266 // 5)
            ),
            self.images
        ))
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.center = (x, config['height'] // 1.4)

        self.speed = 0
    def update(self, *args, **kwargs):
        self.rect.y -= 9

        if self.rect.y < 0:
            self.kill()
        # key = pygame.key.get_pressed()
        # a = 100
        # if key[pygame.K_SPACE]:
        #     while a > 0:
        #         a -= 1
        #         self.rect.y -= 1.2
        #         time.sleep(0.000001)
        # if self.rect.y < -100:
        #     self.rect.center = (config['width'] // 2.01, config['height'] // 1.4)



    def to_dict(self):
        dictionary = {
            "x": self.rect.x,
            "y": self.rect.y,
        }
        return dictionary

    # pygame.image.load("./Assets/spaceship.png"),
    # # управление по Y
    # if key[pygame.K_w]:
    #     if self.speed < 20:
    #         self.speed += 1
    # elif self.speed > 0:
    #     self.speed -= 0.5
    # if key[pygame.K_SPACE]:
    #     if self.speed == 0:
    #         self.image = self.images[0]
    #     if self.speed != 0:
    #         self.image = self.images[1]
    #         self.speed -= 1 if self.speed > 0 else -1
    # if key[pygame.K_s] and self.speed <= 0:
    #     if self.speed > -5:
    #         self.speed -= 1
    # # управление по X
    # if key[pygame.K_a] and self.deg != 50:
    #     self.deg += 5
    # if key[pygame.K_d] and self.deg != -50:
    #     self.deg -= 5
    # self.deg = 50  # -50d <= 0 <= 50d
    # self.direction = ((0, 0), (0, 0))
    # self.old_deg = 0
    # self.calc_vector()

    # def calc_vector(self):
    #     self.direction = (self.rect.center,
    #                       (self.rect.center[0] + (self.deg if self.speed > 0 else 0),
    #                        self.rect.center[1] + abs(self.speed))
    #                       )
    #
    # def draw_vector(self, screen: pygame.Surface):
    #     pygame.draw.line(screen,
    #                      (255, 255, 255),
    #                      self.direction[:1],
    #                      self.direction[1:],
    #                      3)
    #     pygame.draw.arc(screen, (0, 255, 0), (
    #             self.rect.x + self.rect.width + (0 if self.deg >= 0 else self.deg),
    #             self.rect.center[1] - 200,
    #             abs(self.deg),
    #             100