class GameStats:
    """Pratimo statistiku za igru."""

    def __init__(self, hhh_game):
        """Inicijaliziramo statistiku"""

        self.setting = hhh_game.setting

        self.reset_stats()

        # Započni igru u neaktivnom stanju.
        self.game_active = False

        # High score se ne reseta i ako već postoji loada se.
        if not self.load_high_score():
            self.high_score = 0
        else:
            self.high_score = self.load_high_score()

    def reset_stats(self):
        """Inicijaliziramo statistiku koja se mijenja tokom igre."""
        self.hamsters_left = self.setting.hamster_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Loadamo naš trenutni high score iz filea."""
        try:
            with open("high_score.txt", 'r') as f:
                content = f.read()
                return int(content)
        except FileNotFoundError:
            print("First time playing so there is no save file yet.")
