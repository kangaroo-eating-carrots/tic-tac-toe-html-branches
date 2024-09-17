class Player:
    def __init__(self, mark):
        self.mark = mark
        self.choices = []
        self.score = 0

    def make_choice(self, index, width):
        index_2d = [index//width, index % width]
        self.choices.append(index_2d)

    def get_score(self):
        self.score += 1
