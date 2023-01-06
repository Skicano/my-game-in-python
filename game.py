import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from hamster import Hamster
from monster import Monster
from banana import Banana
from banana2 import Banana2
from banana3 import Banana3
from banana4 import Banana4
from rain import Rain
from bush import Bush
from tree import Tree
from play_button import PButton
from quit_button import QButton
from controls import Controls
from background import Background
from monster2 import Monster2
from scoreboard import Scoreboard


class Game:
    """Klasa u kojoj gradimo igru."""

    def __init__(self):
        """Inicijaliziramo igru i njene assete."""
        pygame.init()

        # Postavke.
        self.setting = Settings()

        # Fullscreen.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height

        # Windowed.
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Ime na prozoru.
        pygame.display.set_caption("Love Is In The Air")

        # Vrijeme.
        self.clock = pygame.time.Clock()

        # Instance koje koristimo.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.background = Background(self)
        self.hamster = Hamster(self)
        self.bush = Bush(self)
        self.tree = Tree(self)
        self.controls = Controls(self)

        # Grupe.
        self.bananas = pygame.sprite.Group()
        self.bananas2 = pygame.sprite.Group()
        self.bananas3 = pygame.sprite.Group()
        self.bananas4 = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.monsters2 = pygame.sprite.Group()
        self.rains = pygame.sprite.Group()

        # Stvori grupe.
        self._create_mob()
        self._create_mob2()
        self._create_raining()

        # Tipke.
        self.play_button = PButton(self, "Play")
        self.quit_button = QButton(self, "Quit")

    def run_game(self):
        """Predstavlja glavni loop igre."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_rain()
                self.hamster.update_hamster_position()
                self._update_monsters()
                self._update_monsters2()
                self._update_bananas()
                self._update_bananas2()
                self._update_bananas3()
                self._update_bananas4()

            self.clock.tick()
            self._update_screen()

    def _check_events(self):
        """Respondaj na kontrole na mišu i tipkovnici."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_quit_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Događaj kad se pritisne tipka."""
        if event.key == pygame.K_RIGHT:
            self.hamster.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.hamster.moving_left = True
        elif event.key == pygame.K_UP:
            self.hamster.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.hamster.moving_bottom = True
        elif event.key == pygame.K_d:
            self._fire_bananas()
        elif event.key == pygame.K_a:
            self._fire_bananas2()
        elif event.key == pygame.K_w:
            self._fire_bananas3()
        elif event.key == pygame.K_s:
            self._fire_bananas4()
        elif event.key == pygame.K_SPACE:
            if self.stats.game_active is False:
                self.stats.game_active = True
            elif self.stats.game_active is True:
                self.stats.game_active = False
        elif event.key == pygame.K_ESCAPE:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.stats.reset_stats()
            self.monsters.empty()
            self.monsters2.empty()
            self.bananas.empty()
            self._create_mob()
            self.hamster.center_hamster()

    def _check_keyup_events(self, event):
        """Događaj kad se pusti tipka."""
        if event.key == pygame.K_RIGHT:
            self.hamster.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.hamster.moving_left = False
        elif event.key == pygame.K_UP:
            self.hamster.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.hamster.moving_bottom = False

    def _check_play_button(self, mouse_pos):
        """Započni novu igru kad se pritisne play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Resetaj statistike
            self.setting.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_hamsters()

            # Skrivamo cursor dok traje igra.
            pygame.mouse.set_visible(False)

        # Ukloni stare neprijatelje i projektile.
        self.monsters.empty()
        self.monsters2.empty()
        self.bananas.empty()

        # Stvori nove neprijatelje i smjesti playera.
        self._create_mob()
        self._create_mob2()
        self.hamster.center_hamster()

    def _check_quit_button(self, mouse_pos):
        """Zatvori igru kad se pritisne quit"""
        button_clicked = self.quit_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            sys.exit()

    def _fire_bananas(self):
        """Kreiraj novi projektil i dodaj ga u grupu projektila."""
        if len(self.bananas) < self.setting.bananas_allowed:
            new_banana = Banana(self)
            self.bananas.add(new_banana)

    def _update_bananas(self):
        """Updateaj položaj projektila i ukloni one van ekrana."""
        self.bananas.update()

        for banana in self.bananas.copy():
            if banana.rect.top >= self.screen.get_rect().bottom \
                    or banana.rect.bottom <= 0\
                    or banana.rect.right >= self.screen.get_rect().right \
                    or banana.rect.left <= 0:
                self.bananas.remove(banana)

        self._check_banana_monster_collisions()

    """Ponavljanje istog za svaki smjer projektila."""

    def _fire_bananas2(self):
        if len(self.bananas2) < self.setting.bananas_allowed:
            new_banana = Banana2(self)
            self.bananas2.add(new_banana)

    def _update_bananas2(self):
        self.bananas2.update()

        for banana in self.bananas2.copy():
            if banana.rect.top >= self.screen.get_rect().bottom \
                    or banana.rect.bottom <= 0\
                    or banana.rect.right >= self.screen.get_rect().right \
                    or banana.rect.left <= 0:
                self.bananas2.remove(banana)

        self._check_banana_monster_collisions()

    def _fire_bananas3(self):
        if len(self.bananas3) < self.setting.bananas_allowed:
            new_banana = Banana3(self)
            self.bananas3.add(new_banana)

    def _update_bananas3(self):
        self.bananas3.update()

        for banana in self.bananas3.copy():
            if banana.rect.top >= self.screen.get_rect().bottom \
                    or banana.rect.bottom <= 0\
                    or banana.rect.right >= self.screen.get_rect().right \
                    or banana.rect.left <= 0:
                self.bananas3.remove(banana)

        self._check_banana_monster_collisions()

    def _fire_bananas4(self):
        if len(self.bananas4) < self.setting.bananas_allowed:
            new_banana = Banana4(self)
            self.bananas4.add(new_banana)

    def _update_bananas4(self):
        self.bananas4.update()

        for banana in self.bananas4.copy():
            if banana.rect.top >= self.screen.get_rect().bottom \
                    or banana.rect.bottom <= 0\
                    or banana.rect.right >= self.screen.get_rect().right \
                    or banana.rect.left <= 0:
                self.bananas4.remove(banana)

        self._check_banana_monster_collisions()

    def _check_banana_monster_collisions(self):
        """Provjerava collision projekrila i neprijatelja."""
        collisions1 = pygame.sprite.groupcollide(self.bananas, self.monsters, True, True)
        collisions2 = pygame.sprite.groupcollide(self.bananas2, self.monsters, True, True)
        collisions3 = pygame.sprite.groupcollide(self.bananas3, self.monsters, True, True)
        collisions4 = pygame.sprite.groupcollide(self.bananas4, self.monsters, True, True)

        collisions5 = pygame.sprite.groupcollide(self.bananas, self.monsters2, True, True)
        collisions6 = pygame.sprite.groupcollide(self.bananas2, self.monsters2, True, True)
        collisions7 = pygame.sprite.groupcollide(self.bananas3, self.monsters2, True, True)
        collisions8 = pygame.sprite.groupcollide(self.bananas4, self.monsters2, True, True)

        """Ako se collision desi ažuriraj high score."""
        if collisions1:
            for monsters in collisions1.values():
                self.stats.score += self.setting.monster_points * len(monsters)
            self.sb.prep_score()
            self.sb.check_high_score()

        if collisions2:
            for monsters in collisions2.values():
                self.stats.score += self.setting.monster_points * len(monsters)
            self.sb.prep_score()
            self.sb.check_high_score()

        if collisions3:
            for monsters in collisions3.values():
                self.stats.score += self.setting.monster_points * len(monsters)
            self.sb.prep_score()
            self.sb.check_high_score()

        if collisions4:
            for monsters in collisions4.values():
                self.stats.score += self.setting.monster_points * len(monsters)
            self.sb.prep_score()
            self.sb.check_high_score()

        if collisions5:
            for monsters2 in collisions5.values():
                self.stats.score += self.setting.monster_points * len(monsters2)
            self.sb.prep_score()
            self.sb.check_high_score()

        if collisions6:
            for monsters2 in collisions6.values():
                self.stats.score += self.setting.monster_points * len(monsters2)
            self.sb.prep_score()
            self.sb.check_high_score()

        if collisions7:
            for monsters2 in collisions7.values():
                self.stats.score += self.setting.monster_points * len(monsters2)
            self.sb.prep_score()
            self.sb.check_high_score()

        if collisions8:
            for monsters2 in collisions8.values():
                self.stats.score += self.setting.monster_points * len(monsters2)
            self.sb.prep_score()
            self.sb.check_high_score()

        """Ako nema neprijatelja, ide se na iducu razinu."""
        if not self.monsters and not self.monsters2:
            self.bananas.empty()
            self.bananas2.empty()
            self.bananas3.empty()
            self.bananas4.empty()
            self._create_mob()
            self._create_mob2()
            self.setting.increase_speed()

    def _hamster_hit(self):
        """Ako je player pogođen smanjuju se životi i pozicije se resetaju."""
        if self.stats.hamsters_left > 1:
            # Smanji život i updateaj scoreboard.
            self.stats.hamsters_left -= 1
            self.sb.prep_hamsters()

            # Ukloni preostale neprijatelje i metke.
            self.monsters.empty()
            self.monsters2.empty()
            self.bananas.empty()
            self.bananas2.empty()
            self.bananas3.empty()
            self.bananas4.empty()

            # Ponovo postavi playera i neprijatelje.
            self._create_mob()
            self.hamster.center_hamster()

            # Pauza od pola sekunde.
            sleep(0.5)

        else:
            # Kad nestane života.
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_monster(self):
        """Kreiramo instancu neprijatelja i dodajemo ga u grupu neprijatelja."""
        monster = Monster(self)
        self.monsters.add(monster)

    def _update_monsters(self):
        """Ako neprijatelji dođu do ruba mijenjaju smijer kretanja."""
        self._check_mob_edges()
        self.monsters.update()

        """Ako se neprijatelj sudari s playerom, računa se da je pogođen."""
        if pygame.sprite.spritecollideany(self.hamster, self.monsters):
            self._hamster_hit()

    def _create_mob(self):
        """Kreiramo grupu neprijatelja."""
        for monster in range(5):
            self._create_monster()

    def _check_mob_edges(self):
        """Provjeravamo dali su neprijatelji dotakli rub prozora."""
        for monster in self.monsters.sprites():
            monster.check_edges()

    """Ponavlja se za drugi tip neprijatelja."""

    def _create_monster2(self):
        monster = Monster2(self)
        self.monsters2.add(monster)

    def _update_monsters2(self):
        self._check_mob2_edges()
        self.monsters2.update()

        if pygame.sprite.spritecollideany(self.hamster, self.monsters2):
            self._hamster_hit()

    def _create_mob2(self):
        for monster in range(5):
            self._create_monster2()

    def _check_mob2_edges(self):
        for monster in self.monsters2.sprites():
            monster.check_edges2()

    """Ponavlja se slično i za animaciju kiše koja pada."""

    def _update_rain(self):
        """Updateamo položaj kiše uz pomoć funkcija dolje."""
        self._check_rain_edges()
        self.rains.update()

        for rain in self.rains.copy():
            if rain.rect.top >= self.screen.get_rect().bottom:
                self.rains.remove(rain)

    def _create_rain(self, rain_number, row_number):
        """Kreiramo i pozicioniramo kišu."""
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width + 15 * rain_width * rain_number
        rain.rect.x = rain.x
        rain.y = rain_height + 5 * rain.rect.height * row_number
        rain.rect.y = rain.y
        self.rains.add(rain)

    def _create_raining(self):
        """Kreiramo kišu i računamo broj kapljica u jednome redu i stupcu."""
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size

        available_space_x = self.setting.screen_width - (2 * rain_width)
        number_rains_x = available_space_x // rain_width

        available_space_y = self.setting.screen_height - (3 * rain_height)
        number_rows = available_space_y // (2 * rain_height)

        # Zatim kreiramo kišu.
        for row_number in range(number_rows):
            for rain_number in range(number_rains_x):
                self._create_rain(rain_number, row_number)

    def _check_rain_edges(self):
        """Ako takne gornji ili donji rub prozora..."""
        for rain in self.rains.sprites():
            if rain.check_edges():
                self._change_rain_direction()
                break

    def _change_rain_direction(self):
        """...mijenja smjer."""
        for rain in self.rains.sprites():
            rain.rect.y -= self.setting.rain_speed
        self.setting.rain_direction *= -1

    def _update_screen(self):
        """Updateaj stvari na prozoru i prebaci ih na novi prozor."""

        # Nakon svakog loopa stvori novi prozor.
        self.screen.fill(self.setting.screen_color)
        self.background.draw_background()
        self.bush.draw_bush()
        self.tree.draw_tree()
        self.hamster.draw_hamster()
        self.monsters.draw(self.screen)
        self.monsters2.draw(self.screen)
        for banana in self.bananas.sprites():
            banana.draw_banana()
        for banana in self.bananas2.sprites():
            banana.draw_banana()
        for banana in self.bananas3.sprites():
            banana.draw_banana()
        for banana in self.bananas4.sprites():
            banana.draw_banana()
        for rain in self.rains.sprites():
            rain.draw_rain()

        # Prikaži score.
        self.sb.show_score()

        # Ako je igra pauzirana prikaži tipku play.
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.quit_button.draw_button()
            self.controls.draw_controls()

        # Vidljiv je samo najzadnji prozor..
        pygame.display.flip()


if __name__ == '__main__':
    # Pokreće igru.
    hhh = Game()
    hhh.run_game()
