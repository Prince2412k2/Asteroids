import pygame
from const import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for items in drawable:
            items.draw(screen)
        for items in updatable:
            items.update(dt)
        for items in asteroid:
            if items.collision(player):
                print("Game Over!!")
            for bullet in shots:
                if items.collision(bullet):
                    bullet.kill()
                    items.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
