# Import modules
from turtle import Turtle, Screen
# List of starting positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Constants for directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # When initialised, create three segments
    def __init__(self):
        # List of segments
        self.segments = []
        # Create the snake
        self.create_snake()
        # Define the head of the snake as the first segment
        self.head = self.segments[0]
    
    def create_snake(self):
        # For each entry in STARTING_POSITIONS list, create a white square
        # and move it to that position
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Method for adding segments. Requires a position to add the segment to
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Method that adds a segment to the snake
    def extend(self):
        # We add a segment. The position is that of the last segment in the list
        self.add_segment(self.segments[-1].position())

    # Method for moving
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(20)
    
    # Methods for going up, down, left and right
    def up(self):
        # If the snake is going down, we should not be able to make it
        # go back on itself by going up and vice versa
        # Need these if statements to make game authentic
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)