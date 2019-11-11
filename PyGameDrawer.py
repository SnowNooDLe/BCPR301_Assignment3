import sys
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import math
import pygame
from pygame.locals import *
# https://stackoverflow.com/questions/9815995/read-console-input-using-pygame
# http://programarcadegames.com/python_examples/f.php?file=snake.py
from TIGr import AbstractDrawer


class PyGameDrawer(AbstractDrawer):
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 1024, 1024
        self.screen = pygame.display.set_mode(self.size)
        self.x = self.width // 2
        self.y = self.height // 2
        # Because this is a dictionary,
        self.colours = {'white': (255, 255, 255),
                        'black': (0, 0, 0),
                        'red': (255, 0, 0),
                        'blue': (0, 0, 255)}
        # making an array that has values, so can be return to call whitin dictionary
        self.penlist = ['black', 'red', 'blue']
        self.penColour = self.colours['black']
        self.screen.fill(self.colours['white'])
        self.penDown = True

    def select_pen(self, pen_num):
        self.penColour = self.colours[self.penlist[int(pen_num) - 1]]

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
        # doesnt matter whether pen is down or not, if this method is called, will still need to get new coords as pen will be moved
        # except depends on the situation, may draw the line or not
        newCoords = self.getDestination(self.x, self.y, direction, distance)
        if (self.penDown):
            pygame.draw.line(self.screen, self.penColour, [int(self.x), int(self.y)], newCoords, 1)
        self.x = newCoords[0]
        self.y = newCoords[1]
        pygame.display.flip()

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
        # Adding int for both self.x and y as depends on what we drew before, x and y value can be float
        pygame.draw.circle(self.screen, self.penColour, [int(self.x), int(self.y)], int(size))
        pygame.display.flip()

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
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                # updating the canvas
                pygame.display.flip()
