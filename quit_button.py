import pygame.font


class QButton:

    def __init__(self, hhh_game, msg):
        """Inicijaliziramo atribute za quit tipku."""
        self.screen = hhh_game.screen
        self.screen_rect = self.screen.get_rect()

        # Dimenzije quit tipke.
        self.width, self.height = 200, 100
        self.button_color = (255, 0, 0)
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont("Comic_Sans_MS", 48)

        # Kreira quit tipku i pozicionira je gore desno.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        # Quit natpis na tipki.
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
