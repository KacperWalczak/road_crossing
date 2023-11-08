import time
from turtle import Screen
from player import Player
from car_manager import CarManager, CAR_INTENSITY
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.title("Crossing Turtle")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.up, "Up")
cars_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_manager.move()
    # checking if player touched the car
    for car in cars_manager.cars:
        if player.distance(car) < 30 and abs(car.ycor()) - abs(player.ycor()) < 20:
            game_is_on = False
            game_over = score_board.game_over()

    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        cars_manager.reset_position(CAR_INTENSITY + score_board.level * 5)
        score_board.score_up()


screen.exitonclick()
