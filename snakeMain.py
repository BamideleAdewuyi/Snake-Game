# Import modules
from turtle import Turtle, Screen
import random
import time
from snake import Snake
from snakeFood import Food
from snakeScoreboard import Scoreboard
# Create 600 x 600 screen
screen = Screen()
screen.setup(width=600, height=600)

# Make background black
screen.bgcolor("black")

# Give window title
screen.title("Snake")

# Turn off tracer
screen.tracer(0)

# Create scoreboard
scoreboard = Scoreboard()

# Create snake
snake = Snake()

# Create food
food = Food()

# Call listen method so we can start controlling snake with arrows
screen.listen()

# Call onkey method to get program to listen for these keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Set variable for determining whether the game is still being played
game_is_on = True

while game_is_on:
    # Update the screen. This makes it so the snake moves as one piece
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collistion with 
    # If snake head is within 15 pixels of food 
    if snake.head.distance(food) < 15:

        # Update the score
        scoreboard.increase_score()
        # Food refreshes and appears somewhere else
        food.refresh()
        # Extend the snake
        snake.extend()
    
    # Detect collision with wall
    # If the head of the snake has an x/y coordinate of more than 280 or less
    # than -280, the game is over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    # Iterate through list of segments to check their distances, but make sure 
    # to pass over the first segment. So slice list to not include first element
    # of list
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()






# Make screen only exit when you click on it
screen.exitonclick()