from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 300
CAR_INTENSITY = 5
Y_LIMIT = 12
Y_DISTANCE_BETWEEN_CARS = 20


class Car(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color(choice(COLORS))
        self.penup()
        self.shape('square')
        self.goto(x, y)
        self.shapesize(1, 2)

    def move(self):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())


class CarManager:
    def __init__(self):
        self.cars = []
        self.starting_cars(CAR_INTENSITY)

    def move(self):
        for i, car in enumerate(self.cars):
            car.move()
            if car.xcor() < - 330:
                car.goto(330, Y_DISTANCE_BETWEEN_CARS * randint(-Y_LIMIT, Y_LIMIT))

    def starting_cars(self, cars_num):
        for i in range(cars_num):
            new_car = Car(randint(-300, 300), Y_DISTANCE_BETWEEN_CARS * randint(-Y_LIMIT, Y_LIMIT))
            self.cars.append(new_car)

    def add_cars(self, cars_num):
        for i in range(cars_num):
            new_car = Car(300, Y_DISTANCE_BETWEEN_CARS * randint(-Y_LIMIT, Y_LIMIT))
            self.cars.append(new_car)

    def reset_position(self, intensity):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        self.starting_cars(intensity)

