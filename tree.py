import pygame.image


class Tree:
    """Klasa koja predstavlja stabla u igri."""

    def __init__(self, hhh_game):
        """Inicijaliziramo atribute za stabla."""
        super().__init__()

        self.screen = hhh_game.screen
        self.setting = hhh_game.setting
        self.screen_rect = hhh_game.screen.get_rect()

        # Učitavamo sliku i kreiramo rect za svako stablo.
        self.image = pygame.image.load('images/tree.gif')
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft

        self.image_2 = self.image.copy()
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.topright = self.screen_rect.topright

        self.image_3 = self.image.copy()
        self.rect_3 = self.image_3.get_rect()
        self.rect_3.bottomleft = self.screen_rect.bottomleft

        self.image_4 = self.image.copy()
        self.rect_4 = self.image_4.get_rect()
        self.rect_4.bottomright = self.screen_rect.bottomright

        self.image_5 = self.image.copy()
        self.rect_5 = self.image_5.get_rect()
        self.rect_5.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_tree(self):
        """Prikazuje stabla na prozoru."""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image, self.rect_2)
        self.screen.blit(self.image, self.rect_3)
        self.screen.blit(self.image, self.rect_4)
        self.screen.blit(self.image, self.rect_5)
