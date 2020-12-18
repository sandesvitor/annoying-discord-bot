class Game:

    def __init__(self):
        self.state = "INIT"

    def change_state(self, new_state):
        self.state = new_state

    def print_state(self):
        print(self.state)