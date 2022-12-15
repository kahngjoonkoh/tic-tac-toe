import tkinter as tk
from tkinter import font
import win32ui

from tictactoe import Board


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()

        self.title("Tic-Tac-Toe")
        self.geometry("450x450")
        self.resizable(False, False)

        self.board = Board()
        self.btns = []

        FONT = font.Font(family="Arial", size=15)
        CELL_WIDTH = 150
        for y in range(0, 3):
            for x in range(0, 3):
                sq = x+ 3*y + 1
                btn = tk.Button(self, text="", font=FONT, relief="groove",
                              command=lambda i=sq: self.make_board_move(i))
                self.btns.append(btn)
                btn.place(x=CELL_WIDTH*x, y=CELL_WIDTH*y, height=CELL_WIDTH, width=CELL_WIDTH)

    def make_board_move(self, sq):
        try:
            self.board.makemove(sq)
            if self.board.turn() == "X":
                self.btns[sq - 1].config(text="X")
            else:
                self.btns[sq - 1].config(text="O")

            game_ended = self.board.check_game_ended()
            if game_ended[0]:
                if game_ended[1] == "O":
                    win32ui.MessageBox("Game Ended: O Wins", "TicTacToe")
                elif game_ended[1] == "X":
                    win32ui.MessageBox("Game Ended: X Wins", "TicTacToe")
                elif game_ended[1] == "Draw":
                    win32ui.MessageBox("Game Ended: Draw", "TicTacToe")
        except KeyError:
            win32ui.MessageBox("Invalid Move", "TicTacToe")



if __name__ == "__main__":
    app = App()
    app.mainloop()
