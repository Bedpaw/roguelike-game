class Battle:
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster

    def print(self):
        print(self.monster.on_fight_message)

