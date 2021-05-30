#Create the snake game!

#Create the snake body

#Move the snake

#Control the snake

#Detect collision with food

#Create a scoreboard

#Detect collision with wall

#Detect collision with tail


#Create snake game screen
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snakeboy = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snakeboy.up, "Up")
screen.onkey(snakeboy.down, "Down")
screen.onkey(snakeboy.left, "Left")
screen.onkey(snakeboy.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()   
    time.sleep(0.1)     
    snakeboy.move()
    
    #Detect collision with Food
    if snakeboy.head.distance(food) < 15:
        food.refresh()
        snakeboy.extend()
        scoreboard.increase_score()
    
    #Detect collision with Wall
    if snakeboy.head.xcor() > 280 or snakeboy.head.xcor() < -280 or snakeboy.head.ycor() > 280 or snakeboy.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False
    
    #Detect collision with Tail
    for segment in snakeboy.segments[1:]:
        if snakeboy.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()