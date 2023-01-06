import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """Klasa koja predstavlja jednu kap kiše."""

    def __init__(self, hhh_game):
        """Inicijaliziramo atribute za kišu."""
        super().__init__()

        self.screen = hhh_game.screen
        self.setting = hhh_game.setting
        self.screen_rect = hhh_game.screen.get_rect()
        self.color = hhh_game.setting.rain_color

        # Rect za kišu.
        self.rect = pygame.Rect(0, 0, self.setting.rain_width, self.setting.rain_height)

        # Smijer kretanja y.
        self.y = float(self.rect.y)

    def update(self):
        """Mijenja smijer ili poziciju kiše."""
        self.y += self.setting.rain_speed * self.setting.rain_direction
        self.rect.y = self.y

    def draw_rain(self):
        """Prikazuje kišu u prozoru."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        """Provjerava da li je kiša dotakla rub prozora."""
        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom:
            return True
