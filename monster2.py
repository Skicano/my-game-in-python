import pygame
from pygame.sprite import Sprite
import random


class Monster2(Sprite):
    """Klasa koja predstavlja neprijatelja."""

    def __init__(self, hhh_game,):
        """Inicijaliziramo neprijatelja i njegovu start poziciju."""
        super().__init__()

        self.screen = hhh_game.screen
        self.setting = hhh_game.setting
        self.screen_rect = hhh_game.screen.get_rect()

        # Loadamo sliku neprijatelja i stvaramo njezin rect.
        self.pos = pygame.math.Vector2(150, 550)
        self.dir = pygame.math.Vector2(random.random(), random.random())

        self.image = pygame.image.load('images/elephant.gif')
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y))).inflate(-90, -40)

        # Startaj lijevo u sredini prozora.
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def reflect(self, NV):
        """Odbijanje od rubova prozora."""
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))

    def update(self):
        """Mijenja poziciju neprijatelja."""
        self.pos += self.dir * self.setting.monster_speed
        self.rect.center = round(self.pos.x), round(self.pos.y)

    def check_edges2(self):
        """Provjerava da li je neprijatelj dotakao rub prozora."""
        if self.rect.left <= 0:
            self.reflect((1, 0))
        if self.rect.right >= 1920:
            self.reflect((-1, 0))
        if self.rect.top <= 0:
            self.reflect((0, 1))
        if self.rect.bottom >= 1080:
            self.reflect((0, -1))
