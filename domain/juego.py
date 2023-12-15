from domain.rejilla import Rejilla

class Juego:
    def __init__(self):
        self.rejilla = Rejilla()
        self.rejilla.__set_grid__()
        self.rejilla.__set_alive__()

    def __start__(self) -> None:
        print(self.rejilla.__to_str__())