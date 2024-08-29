import pygame
import random
from circleshape import CircleShape
from const import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen, color="white", center=self.position, radius=self.radius, width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            v1 = self.velocity.rotate(random.uniform(20, 30))
            v2 = self.velocity.rotate(-random.uniform(20, 30))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astr_1 = Asteroid(self.position.x, self.position.y, new_radius)
            astr_2 = Asteroid(self.position.x, self.position.y, new_radius)
            astr_1.velocity = v1 * 1.2
            astr_2.velocity = v2 * 1.2
