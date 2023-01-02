from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
HEIGHT=800
WIDTH=800
CONSTANT=10

screen=Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Gamee")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on =True
while(game_is_on):
    screen.update()
    time.sleep(0.2)
    snake.move()

    #Detect Collision with food
    if snake.head.distance(food)<20:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    #Detect Collision with wall
    if snake.head.pos()[0] <-(HEIGHT//2-CONSTANT) or snake.head.pos()[0] > (HEIGHT//2-CONSTANT) or snake.head.pos()[1] < -(WIDTH//2-CONSTANT) or snake.head.pos()[1] > (WIDTH//2-CONSTANT):
        scoreboard.game_over()
        game_is_on=False


    #Detect Collision with tail, if head colides with any segment on tail then -> game over

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            scoreboard.game_over()
            game_is_on=False





screen.exitonclick()