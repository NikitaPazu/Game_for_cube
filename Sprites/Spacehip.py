import pygame
import file_utils



config = file_utils.read_config_json()


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.images = [
            pygame.image.load("Sprites/Assets/spaceship.png")
        ]
        self.images = list(map(
            lambda x: pygame.transform.scale(
                pygame.transform.rotate(x, 0),
                (256 // 4, 316 // 4)
            ),
            self.images
        ))
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.center = (config['width'] // 2, config['height'] // 1.5)

        self.speed = 0
        # self.deg = 50  # -50d <= 0 <= 50d
        # self.direction = ((0, 0), (0, 0))
        # self.old_deg = 0
        # self.calc_vector()
    Spaceship_x = 0
    def update(self, *args, **kwargs):
        key = pygame.key.get_pressed()
        Spaceship_x = self.rect.center
        if key[pygame.K_a]:
            self.rect.x -= 10
        if key[pygame.K_d]:
            self.rect.x += 10


        if self.rect.x <= 0:
            self.rect.x += 255
        if self.rect.x >= 450:
            self.rect.x -= 255
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

    # pygame.image.load("./Assets/spaceship.png"),