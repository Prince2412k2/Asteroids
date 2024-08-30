import pygame
from const import *


class Healthbar(pygame.sprite.Sprite):
    def __init__(self) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.hp = 100
        self.colided_asteroids = []

    def draw(self, screen):
        pygame.draw.rect(screen, "red", pygame.Rect(30, 30, 2 * self.hp, 7))

    def bleed(self, obj):
        if obj not in self.colided_asteroids:
            self.colided_asteroids.append(obj)

            if obj.radius == ASTEROID_MIN_RADIUS:
                self.hp -= ASTEROID_MIN_RADIUS

            elif ASTEROID_MAX_RADIUS:
                self.hp -= ASTEROID_MAX_RADIUS

            else:
                self.hp -= 40
