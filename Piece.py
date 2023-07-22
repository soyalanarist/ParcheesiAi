class Piece:
    def __init__(self):
        self.is_in_play = True
        self.is_in_jail = True
        self.color = "out"
        self.step = "out"

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location
    
    def take_out_of_jail(self):
        self.is_in_jail = False

    def is_piece_in_jail(self):
        return self.is_in_jail
    
    def take_out_of_play(self):
        self.is_in_play = False
        self.location = "out"

    def is_piece_in_play(self):
        return self.is_in_play
    
    def move_piece(self, spaces):
        self.location += spaces

    