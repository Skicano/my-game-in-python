class Settings:
    """Klasa gdje spremamo sve postavke za igru."""

    def __init__(self):
        """Inicijaliziramo nepromjenjive postavke."""
        # Prozor.
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (0, 153, 0)

        # Životi.
        self.hamster_limit = 3

        # Projektili.
        self.bananas_allowed = 1
        self.bananas2_allowed = 1
        self.bananas3_allowed = 1
        self.bananas4_allowed = 1

        # Kiša.
        self.rain_width = 3
        self.rain_height = 20
        self.rain_color = (0, 0, 255)
        self.rain_speed = 21
        self.rain_direction = 1

        # Koliko se igra ubrzava i score povecava.
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Promjenjive postavke.
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicijaliziramo postavke koje se mijenjaju kroz igru."""
        self.hamster_speed = 7.0
        self.banana_speed = 11.0
        self.monster_speed = 15.0

        # Smijer neprijatelja 1 je desno, -1 je lijevo.
        self.mob_direction = 1

        # Početna vrijednost svakog neprijatelja u scoreu.
        self.monster_points = 50

    def increase_speed(self):
        # Povećava brzinu i vrijednost neprijatelja.
        self.hamster_speed *= self.speedup_scale
        self.banana_speed *= self.speedup_scale
        self.monster_speed *= self.speedup_scale

        self.monster_points = int(self.monster_points * self.score_scale)
