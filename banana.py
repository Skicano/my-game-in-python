import pygame
from pygame.sprite import Sprite


class Banana(Sprite):
    """Klasa koja predstavlja projektil."""

    def __init__(self, hhh_game):
        """Stvaramo projekril na trenutnoj poziciji playera."""
        super().__init__()

        self.screen = hhh_game.screen
        self.setting = hhh_game.setting

        # Učitavamo sliku projektila i kreiramo njezin rect.
        self.image = pygame.image.load('images/heart3.gif')
        self.rect = self.image.get_rect()
        self.rect.center = hhh_game.hamster.rect.center
        # self.width = self.image.get_width()
        # self.height = self.image.get_height()
        # self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.x = float(self.rect.x)

    def update(self):
        """Mijenjamo poziciju projektila na prozoru."""
        self.x += self.setting.banana_speed
        self.rect.x = self.x

    def draw_banana(self):
        """Prikazujemo projektil na prozoru."""
        self.screen.blit(self.image, self.rect)
