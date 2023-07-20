from Piece import Piece
from random import randint

class Player:
    def __init__(self, color):
        self.color = color
        self.in_play = True

        piece1 = Piece()
        piece2 = Piece()
        piece3 = Piece()
        piece4 = Piece()
        self.pieces = [piece1, piece2, piece3, piece4]

    def get_piece_out_of_jail(self, count):
        if count == 1:
            for piece in self.pieces:
                if piece.is_piece_in_jail():
                    piece.take_out_of_jail()

    def get_color(self):
        return self.color
    
    def roll_dice(self):
        return (randint(1, 6), randint(1, 6))

    def roll_die(self):
        return randint(1, 6)
    
    def check_if_two_or_more_pieces_in_play(self):
        count = 0
        for piece in self.pieces:
            if piece.is_piece_in_play():
                count += 1
        return count >= 2
    
    def roll(self):
        if self.check_if_two_or_more_pieces_in_play():
            return self.roll_dice()
        return self.roll_die()