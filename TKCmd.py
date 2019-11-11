import cmd, sys, math, re
from tkinter import *
from TKDrawer import *
from TIGr import AbstractDrawer, AbstractParser, AbstractSourceReader


class TKInterShell(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to the TKinter shell.   Type help or ? to list commands.\n'
        self.drawer = TKDrawer()
        self.prompt = '(TKinter) '
        self.update()

    def do_selectpen(self, arg):
        'Select the pen: PENCOLOR 1, 2 or 3, 1 is BLACK, 2 is RED and 3 is BLUE'
        self.drawer.select_pen(*parse(arg))
        self.update()

    def do_penup(self, arg):
        'Pen up'
        self.drawer.pen_up()
        self.update()

    def do_pendown(self, arg):
        'Pen down'
        self.drawer.pen_down()
        self.update()

    def do_go_along(self, arg):
        'Move along to certain value (User input)'
        self.drawer.go_along(*parse(arg))
        self.update()

    def do_go_down(self, arg):
        'Move down to certain value (User input)'
        self.drawer.go_down(*parse(arg))
        self.update()

    def do_draw_line(self, arg):
        'Move to distance mush in direction'
        self.drawer.draw_line(*parse(arg))
        self.update()

    def do_draw_circle(self, arg):
        'Draw a circle with size of User input'
        self.drawer.draw_circle(*parse(arg))
        self.update()

    def do_draw_rectangle(self, arg):
        'Draw a rectangle with size of User input'
        self.drawer.draw_rectangle(*parse(arg))
        self.update()

    def do_draw_triangle(self, arg):
        'Draw a triangle with size of User input'
        self.drawer.draw_triangle(*parse(arg))
        self.update()

    def do_bye(self, arg):
        """Stop recording, close the tkinter window, and exit:  BYE"""
        print('Thank you for using tkinter')
        self.drawer.master.destroy()
        return True

    def update(self):
        self.drawer.w.update()


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))
