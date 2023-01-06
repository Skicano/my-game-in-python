import pygame.image


class Bush:
    """Klasa koja predstavlja grmove u igri."""

    def __init__(self, hhh_game):
        """Inicijaliziramo atribute za grmove."""
        super().__init__()

        self.screen = hhh_game.screen
        self.setting = hhh_game.setting
        self.screen_rect = hhh_game.screen.get_rect()

        # Učitavamo sliku i kreiramo rect za svaki grm.
        self.image = pygame.image.load('images/bush.gif')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop

        self.image_2 = self.image.copy()
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_bush(self):
        """Prikazuje dva grma na prozoru."""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image, self.rect_2)
