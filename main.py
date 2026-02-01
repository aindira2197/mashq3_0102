class Game:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} o‘yini boshlandi")


class OnlineGame(Game):
    def __init__(self, name, players):
        super().__init__(name)
        self.players = players

    def info(self):
        print(f"O‘yin: {self.name}, O‘yinchilar: {self.players}")


game = OnlineGame("PUBG", 100)
game.start()
game.info()
