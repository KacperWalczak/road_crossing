from turtle import Turtle
from playsound import playsound

LIMIT_OF_ROUNDS = 3
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        with open("highest_level.txt", 'r') as self.file:
            self.highest_level = int(self.file.read())
        self.color("black")
        self.goto(-90, 250)
        self.update_score()
        self.num_of_rounds = 0

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}  Highest Level: {self.highest_level}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.level += 1
        self.update_score()
        playsound('win.wav')

    def reset_board(self):
        if self.level > self.highest_level:
            self.highest_level = self.level
            with open("highest_level.txt", 'w') as self.file:
                self.file.write(str(self.highest_level))
        self.level = 1
        self.update_score()
        self.num_of_rounds += 1
        if self.num_of_rounds == LIMIT_OF_ROUNDS:
            self.game_over()
            return False
        else:
            playsound('over.wav')
            return True

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=('Courier', 50, 'normal'))
        playsound('over2.wav')



