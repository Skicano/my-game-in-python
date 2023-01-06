import pygame
from pygame.sprite import Sprite


class Hamster(Sprite):
    """Klasa koja predstavlja playera."""

    def __init__(self, hhh_game):
        """Inicijaliziramo playera i postavljamo ga na startnu poziciju."""
        super().__init__()

        self.screen = hhh_game.screen
        self.setting = hhh_game.setting
        self.screen_rect = hhh_game.screen.get_rect()

        # Loadamo sliku playera i stvaramo njezin rect.
        self.pos = pygame.math.Vector2(1800, 550)
        self.image = pygame.image.load('images/pig.gif')
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y))).inflate(-30, -30)

        # Startaj na centru prozora.
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Flag za movement.
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update_hamster_position(self):
        """Updateamo poziciju playera na prouoru (movement)."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.hamster_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.hamster_speed
        if self. moving_top and self.rect.top > 0:
            self.y -= self.setting.hamster_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.hamster_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_hamster(self):
        """Prikazuje playera na trenutnoj poziciji."""
        self.screen.blit(self.image, self.rect)

    def center_hamster(self):
        """Centrira playera na prozoru."""
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
