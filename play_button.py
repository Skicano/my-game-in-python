import pygame.font


class PButton:
    """Klasa za play tipku."""

    def __init__(self, hhh_game, msg):
        """Inicijaliziramo atribute za play tipku."""
        self.screen = hhh_game.screen
        self.screen_rect = self.screen.get_rect()

        # Dimenzije play tipke.
        self.width, self.height = 200, 100
        self.button_color = (255, 0, 0)
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont("Comic_Sans_MS", 48)

        # Kreira play tipku i pozicionira je gore lijevo.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = self.screen_rect.topleft

        # Play natpis na tipki.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Pretvara natpis u sliku i centrira je na tipku."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Kreira sliku tipke na prozoru."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
