class Player:
    def __init__(self, mark):
        self.mark = mark
        self.choices = []

    def make_choice(self, index, width):
        index_2d = [index//width, index % width]
        self.choices.append(index_2d)
