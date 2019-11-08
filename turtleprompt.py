from turtledrawer import TurtleDrawer
from Parser import IntegerParser
from cmd import Cmd
from writer import *


class TurtlePrompt(Cmd):
    results = Writer("TurtleDrawer_Result.txt")
    welcome = "Welcome to Turtle Shell"
    prompt = '(turtle)'
    file = None

    def do_P(self, arg):
        """Select Pen:  P 10"""
        self.results.writeToFile("Selected pen", arg)
        data = IntegerParser.parse(self, arg)
        TurtleDrawer.select_pen(self, data)

    def do_U(self, arg):
        """Pen Up : U"""
        self.results.writeToFile("Pen is up")
        TurtleDrawer.pen_up(self)

    def do_D(self, arg):
        """Pen Down : D"""
        self.results.writeToFile("Pen is down")
        TurtleDrawer.pen_down(self)

    def do_X(self, arg):
        """Go Along : X 100"""
        self.results.writeToFile("Go Along : X ", arg)
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.go_along(self, command)

    def do_Y(self, arg):
        """Go Down : Y 100"""
        self.results.writeToFile("Go Along : Y", arg)
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.go_down(self, command)

    def do_N(self, arg):
        """Draw line 0 degrees : N 100"""
        self.results.writeToFile("Draw line 0 degrees : N", arg)
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_line(self, 0, command)

    def do_E(self, arg):
        """Draw line 90 degrees : E 100"""
        self.results.writeToFile("Draw line 90 degrees : E", arg)
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_line(self, 90, command)

    def do_S(self, arg):
        """Draw line 120 degrees : S 100"""
        self.results.writeToFile("Draw line 120 degrees : S", arg)
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_line(self, 180, command)

    def do_W(self, arg):
        """Draw line 270 degrees : W 100"""
        self.results.writeToFile("Draw line 270 degrees : W", arg)
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_line(self, 270, command)

    def do_square(self, arg):
        """Draw Square"""
        self.results.writeToFile("Drawing a square")
        command = IntegerParser.parse(self, arg)
        directions = [0, 90, 180, 270]
        for i in directions:
            TurtleDrawer.draw_line(self, i, command)

    def do_circle(self, arg):
        """Draw Circle"""
        self.results.writeToFile("Drawing a circle")
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_circle(self, command)

    def do_Exit(self, arg):
        """Exit Turtle CMD"""
        self.results.writeToFile("End program, Bye")
        print("Bye")
        return True
