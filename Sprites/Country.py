import pygame


class Country:
    def __init__(self, name: str):
        self.__name = name
        self.people = 20
        self.sicked = 0
        self.koef_e = 0.9
        self.polygon = [
            [0, 0], [1, 1]
        ]

    def update(self):
        self.sicked += 2

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(
            screen,
            pygame.Color(255, 255, 255),
            self.polygon
        )

        percent_sicked = int(0.0456 * 255)

        pygame.draw.polygon(
            screen,
            pygame.Color(255, 0, 0, percent_sicked),
            self.polygon
        )

        # отрисовать аэропорт