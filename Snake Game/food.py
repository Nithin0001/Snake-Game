from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("#dd4124")
        self.speed("fastest")
        self.shapesize(0.7, 0.7)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-620, 620)
        random_y = random.randint(-340, 340)
        self.goto(random_x, random_y)
