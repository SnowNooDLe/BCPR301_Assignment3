from tigr import AbstractDrawer
import turtle
# Alliah & Caitlyn


class TurtleDrawer(AbstractDrawer):

    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')
        turtle.pensize(pen_num)

    def pen_down(self):
        print('pen down')
        turtle.pendown()

    def pen_up(self):
        print('pen up')
        turtle.penup()

    def go_along(self, along):
        print(f'GOTO X={along}')
        turtle.goto(along, 0)

    def go_down(self, down):
        print(f'GOTO Y={down}')
        turtle.goto(0, down)

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction} degrees')
        if direction == 0:
            newDirection = 90
        if direction == 180:
            newDirection = 270
        if direction == 90:
            newDirection = 0
        if direction == 270:
            newDirection = 180
        turtle.seth(newDirection)
        turtle.forward(distance)

    def draw_circle(self, radius):
        turtle.circle(radius)
