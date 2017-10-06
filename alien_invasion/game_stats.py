import json

class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        self.load_score()

    def reset_stats(self):
        self.is_mouse_control = False
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_score(self, filename = "scores.json"):
        try:
            with open(filename) as file_obj:
                data_to_load = json.load(file_obj)
                self.high_score = int(data_to_load.get('high_score', 0))
        except FileNotFoundError:
            print("File with scores not found, create default higscore")
            self.high_score = 0

    def save_scrore(self, filename = "scores.json"):
        data_to_save = {}
        data_to_save['high_score'] = self.high_score

        with open(filename, 'w') as file_object:
            json.dump(data_to_save, file_object)
