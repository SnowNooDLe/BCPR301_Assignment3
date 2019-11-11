import math
from tkinter import *
from TIGr import AbstractDrawer


class TKDrawer(AbstractDrawer):

    def __init__(self):
        self.x = 512
        self.y = 512
        self.master = Tk()
        self.w = Canvas(self.master, width=1024, height=1024)
        self.w.pack()
        self.pen = "black"
        self.penDown = True
        self.penlist = ["black", "red", "blue"]

    def select_pen(self, pen_num):
        self.pen = self.penlist[int(pen_num) - 1]

    def pen_down(self):
        self.penDown = True

    def pen_up(self):
        self.penDown = False

    def go_along(self, along):
        self.x += int(along)

    def go_down(self, down):
        # based on normal x,y graph, going down (south is -y) to achieve this, unlike turtle, for PyGame and TKinter needs to minus the value.
        self.y -= int(down)

    def draw_line(self, direction, distance):
        direction = int(direction)
        distance = int(distance)
        if direction == 0 or direction == 180:
            direction += 180
        # as we only want to draw line when pen is down but if pen is up and wanna draw line, pen will be moved without leaving mark,
        # so still need to change coordinate, hence get new coords
        newCoords = self.getDestination(self.x, self.y, direction, distance)
        if (self.penDown):
            self.w.create_line(self.x, self.y, newCoords[0], newCoords[1], fill=self.pen)
        # replace current pen pos to new pos
        self.x = newCoords[0]
        self.y = newCoords[1]

    # Simple math calculation.
    def getDestination(self, currentX, currentY, direction, distance):
        direction = float(direction)
        # Compute the change in position
        delta_y = distance * math.cos(math.radians(direction))
        delta_x = distance * math.sin(math.radians(direction))
        # Add that to the existing position
        new_x = currentX + delta_x
        new_y = currentY + delta_y
        return new_x, new_y

    def draw_circle(self, size):
        ourDirection = 0
        for i in range(360):
            self.draw_line(ourDirection, int(size) / 10)
            ourDirection += 1

    def draw_rectangle(self, size):
        ourDirection = 0
        for i in range(4):
            self.draw_line(ourDirection, size)
            ourDirection += 90

    def draw_triangle(self, size):
        ourDirection = 120
        for i in range(3):
            self.draw_line(ourDirection, size)
            ourDirection += 120

    def end(self):
        print('we finished')
        mainloop()
