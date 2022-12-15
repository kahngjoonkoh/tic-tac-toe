import binascii

class Board:
    def __init__(self):
        self._o = [0, 0, 0,
                   0, 0, 0,
                   0, 0, 0]

        self._x = [0, 0, 0,
                   0, 0, 0,
                   0, 0, 0]

        self.win_conditions = [
            448, # 111000000
            56, # 000111000
            7, # 000000111
            273, # 100010001
            84, # 001010100
            292, # 100100100
            146, # 010010010
            73 # 001001001
        ]

        self._turn = 'O'

    def turn(self) -> str:
        return self._turn

    # sq should be in the range of 1 - 9
    def makemove(self, sq: int):
        if self.can_makemove(sq):
            if self._turn == 'O':
                self._o[sq-1] = 1
                self._turn = 'X'
            else:
                self._x[sq-1] = 1
                self._turn = 'O'
        else:
            raise KeyError #placeholder error. Invalid move.

    def can_makemove(self, sq: int) -> bool:
        if self.check_game_ended()[0] == True:
            return False
        if self._o[sq-1] == 1 or self._x[sq-1] == 1:
            return False
        else:
            return True

    def check_game_ended(self) -> (bool, str):
        temp_o, temp_x = self._to_int(self._o), self._to_int(self._x)
        for mask in self.win_conditions:
            if temp_o & mask == mask:
                return (True, "X")
            elif temp_x & mask == mask:
                return (True, "O")
        if (self._o.count(1) + self._x.count(1)) == 9:
            return (True, "Draw")
        else:
            return (False, "")

    @staticmethod
    def _to_int(l):
        val = 0
        for i, b in enumerate(l):
            val += 2**(8-i) * b
        return val
