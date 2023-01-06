import pygame.image


class Background:
    """Klasa za pozadinsku sliku."""

    def __init__(self, hhh_game):
        """Inicijaliziramo atribute za pozadinsku sliku."""
        super().__init__()

        self.screen = hhh_game.screen
        self.setting = hhh_game.setting
        self.screen_rect = hhh_game.screen.get_rect()

        # Učitavamo sliku i kreiramo njezin rect.
        self.image = pygame.image.load('images/grass3.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect = self.screen_rect

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_background(self):
        """Postavljamo pozadinu na prozoru."""
        self.screen.blit(self.image, self.rect)
