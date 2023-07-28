# Import modules
import _tkinter
from turtle import Turtle

# This inherits from the Turtle class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Hide this as we do not want to see an actual turtle
        self.hideturtle()
        # Make white
        self.color("white")
        # Pull the pen up
        self.up()
        # Send turtle to top of screen
        self.goto(0, 270)
        # Create a score variable
        self.score = 0
        # Write score at top of screen
        self.update_score()
    
    # Method for writing the score on screen
    def update_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=('Courier New', 20, 'normal'))
        
    # Method for increasing the score
    def increase_score(self):
        # Add one to the score when this is called
        self.score += 1

        # Clear the writing and add the new message
        self.clear()
        self.update_score()
    
    # Method to be called when game is over
    def game_over(self):
        # Text is written in centre of screen
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=('Courier New', 20, 'normal'))