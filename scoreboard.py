from turtle import Turtle
ALIGHNMENT="center"
FONT=('Arial', 12, 'bold')
SCOREBOARD_LOCATION=(0,380)
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGHNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGHNMENT,font=FONT)