import pygame.image


class Controls:
    """Klasa za prikaz kontrola."""

    def __init__(self, hhh_game):
        """Inicijaliziramo atribute za prikaz kontrola."""
        self.screen = hhh_game.screen
        self.setting = hhh_game.setting
        self.screen_rect = hhh_game.screen.get_rect()

        # Učitavanje slike za kontrole.
        self.image = pygame.image.load('images/controls.jpg')
        self.rect = self.image.get_rect()

        # Pozicionira sliku u sredini prozora dolje.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_controls(self):
        """Prikazuje sliku kontrola na ekrenu."""
        self.screen.blit(self.image, self.rect)
