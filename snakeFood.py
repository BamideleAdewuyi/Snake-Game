# Make a food class for the snake game

# Import modules
import _tkinter

from turtle import Turtle

import random

# Food class will inherit from the Turtle class. See parentheses
class Food(Turtle):

    def __init__(self):
        # This calls the initialiser of the super class. In this case
        # the Turtle class. Now we can use all methods and attributes
        # of the Turtle class. So we can set the shape and say pen up etc
        super().__init__()
        self.shape("circle")
        self.up()
        # This resizes the turtle. Default is 20x20, so stretching
        # by 0.5 makes it 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # Need to randomise where it appears. Grid is 600x600
        # so we should make it appear between -280 and 280 on
        # both axes. Using refresh method that's defined below
        self.refresh()
    
    # Create a method for when the snake gets the food and the food
    # must therefore move to a new random location
    def refresh(self):
        # Need to randomise where it appears. Grid is 600x600
        # so we should make it appear between -280 and 280 on
        # both axes
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)