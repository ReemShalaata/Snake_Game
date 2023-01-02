import random
from turtle import Turtle
FOOD_POSITION_MAX=380
FOOD_POSITION_MIN=-380
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x=random.randint(FOOD_POSITION_MIN,FOOD_POSITION_MAX)
        random_y=random.randint(FOOD_POSITION_MIN,FOOD_POSITION_MAX)
        self.goto(random_x,random_y)