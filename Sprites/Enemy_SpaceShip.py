import random
import time
import pygame
import file_utils

config = file_utils.read_config_json()


class Enemy_Spaceship(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.images = [
            pygame.image.load("Sprites/Assets/enemy_space_ship.png")
            ]
        self.images = list(map(
            lambda x: pygame.transform.scale(
                pygame.transform.rotate(x, 0),
                (256 // 4, 350 // 5)
            ),
            self.images
        ))
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.center = (random.randint(1, 450), config['height'] // 8)

        self.speed = 0
        self.direction = ((0, 0), (0, 0))
        # self.calc_vector()

    def update(self, *args, **kwargs):
        # key = pygame.key.get_pressed()
        self.speed = random.randint(0, 11)
        # управление по X
        # a = random.randint(1, 1000)
        a = random.random()
        if a > 0.5:
            self.rect.x -= self.speed
        if a <= 0.5:
            self.rect.x += self.speed

        if self.rect.x < 0:
            a = random.random()
            if a < 0.5:
                self.rect.x -= 0
            if a > 0.5:
                self.rect.x += 20

        if self.rect.x > 450:
            a = random.random()
            if a < 0.5:
                self.rect.x += 0
            if a > 0.5:
                self.rect.x -= 20

    # def calc_vector(self):
    #     self.direction = (self.rect.center,
    #                       (self.rect.center[0] + (self.deg if self.speed > 0 else 0),
    #                        self.rect.center[1] + abs(self.speed))
    #                       )

    def draw_vector(self, screen: pygame.Surface):
        pygame.draw.line(screen,
                         (255, 255, 255),
                         self.direction[:1],
                         self.direction[1:],
                         3)
        # pygame.draw.arc(screen, (0, 255, 0), (
        #         self.rect.x + self.rect.width + (0 if self.deg >= 0 else self.deg),
        #         self.rect.center[1] - 200,
        #         abs(self.deg),
        #         100
        # ), math.pi if self.deg > 0 else 1.5 * math.pi, 0 if self.deg < 0 else 1.5 * math.pi)
        # pygame.draw.arc(screen, (0, 255, 0), (
        #     self.rect.x + (0 if self.deg >= 0 else self.deg),
        #     self.rect.center[1]- 200,
        #     abs(self.deg),
        #     100
        # ), math.pi if self.deg > 0 else 1.5 * math.pi, 0 if self.deg < 0 else 1.5 * math.pi)

    def to_dict(self):
        dictionary = {
            "x": self.rect.x,
            "y": self.rect.y,
        }
        return dictionary

    # pygame.image.load("./assets/enemy_space_ship.png.png"),