import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = 0
        self.font = pygame.font.SysFont("freesanbold.ttf", 50)

    def draw(self, screen):
        text = self.font.render(f"{self.score}", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1200, 80)
        screen.blit(text, textRect)

    def increse(self):
        self.score += 1
