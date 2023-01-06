import pygame.font
from pygame.sprite import Group
from hamster import Hamster


class Scoreboard:
    """Klasa koja nam prikazuje score."""

    def __init__(self, hhh_game):
        """Inicijaliziramo atribute za scoreboard."""
        self.hhh_game = hhh_game
        self.screen = hhh_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = hhh_game.setting
        self.stats = hhh_game.stats

        # Postavke za font.
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont("Comic_Sans_MS", 72)

        # Slike za score.
        self.prep_score()
        self.prep_high_score()
        self.prep_hamsters()

        # File gdje spremamo i loadamo high score.
        self.filename = "high_score.txt"

    def prep_score(self):
        """Renderamo sliku za score."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Score se prikazuje u sredini na vrhu prozora.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = self.screen_rect.midtop

    def show_score(self):
        """Prikazuje živote, score i level na ekranu."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.hamsters.draw(self.screen)

    def prep_high_score(self):
        """Renderamo sliku za high score."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # High score se prikazuje gore desno na prozoru.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.topright = self.screen_rect.topright

    def check_high_score(self):
        """Loadamo stari high score ili ako postoji novi saveamo ga."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.save_high_score()

    def prep_hamsters(self):
        """Prikazuje koliko je ostalo života."""
        self.hamsters = Group()
        for hamster_number in range(self.stats.hamsters_left):
            hamster = Hamster(self.hhh_game)
            hamster.rect.x = 10 + hamster_number * hamster.rect.width
            hamster.rect.y = 10
            self.hamsters.add(hamster)

    def save_high_score(self):
        """Sprema naš high score."""
        with open(self.filename, 'w') as f:
            f.write(str(self.stats.high_score))
