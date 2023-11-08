from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])


