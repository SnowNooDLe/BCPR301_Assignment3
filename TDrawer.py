import math
from TIGr import AbstractDrawer
import turtle


class TDrawer(AbstractDrawer):
    def __init__(self):
        self.penlist = ["black", "red", "blue"]

    def select_pen(self, pen_num):
        turtle.pencolor(self.penlist[int(pen_num) - 1])

    def pen_down(self):
        turtle.pendown()

    def pen_up(self):
        turtle.penup()

    # Because for along and down, we dont wanna draw line while we are moving
    def go_along(self, along):
        # setX is changing X to certain value, so instead of doing that, we want to move from current to new by adding value, not to that coordinate
        # e.g., turtle is at (100, 200), if we do go_along 200, we want to be at (300, 200) not (200,200)
        currentX = turtle.xcor()
        if (turtle.isdown()):
            turtle.penup()
            turtle.setx(currentX + int(along))
            turtle.pendown()
        else:
            turtle.setx(currentX + int(along))

    def go_down(self, down):
        # Same idea to go_along
        currentY = turtle.ycor()
        if (turtle.isdown()):
            turtle.penup()
            turtle.sety(currentY + int(down))
            turtle.pendown()
        else:
            turtle.sety(currentY + int(down))

    def draw_line(self, direction, distance):
        # IF YOU WANT TO HAVE DYNAMIC DIRECTIONS YOU NEED TO UPDATE THIS CODE
        direction = int(direction)
        if direction == 90 or direction == 270:
            direction -= 90
        else:
            direction += 90
        distance = int(distance)
        turtle.seth(direction)
        if (turtle.isdown()):
            turtle.forward(distance)

    def draw_circle(self, size):
        turtle.circle(int(size))

    # for rectangle and triangle, unlike TKinter, they work based on where they are facing and remember previous move, not like TKinter resets where
    # they are facing everytime we move.
    def draw_rectangle(self, size):
        ourDirection = 0
        for i in range(4):
            self.draw_line(ourDirection, size)
            ourDirection += 90

    def draw_triangle(self, size):
        ourDirection = 0
        for i in range(3):
            self.draw_line(ourDirection, size)
            ourDirection -= 120

    def end(self):
        turtle.exitonclick()
