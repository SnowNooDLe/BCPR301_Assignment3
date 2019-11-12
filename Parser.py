from TIGr import AbstractParser


class ParentDrawLiner(object):
    def __init__(self, drawer, data):
        self.drawer = drawer
        self.data = data

    def draw_line(self):
        pass


class DrawLinerToNorth(ParentDrawLiner):
    def draw_line(self):
        return self.drawer.draw_line(0, self.data)


class DrawLinerToEast(ParentDrawLiner):
    def draw_line(self):
        return self.drawer.draw_line(90, self.data)


class DrawLinerToSouth(ParentDrawLiner):
    def draw_line(self):
        return self.drawer.draw_line(180, self.data)


class DrawLinerToWest(ParentDrawLiner):
    def draw_line(self):
        return self.drawer.draw_line(270, self.data)


class Parser(AbstractParser):
    def parse(self, raw_source):
        test = self.drawer
        for row in raw_source:
            self.command = row[0]
            try:
                self.data = row[1]
            except:
                self.data = 0
            try:
                if self.command == 'P':
                    self.drawer.select_pen(self.data)
                if self.command == 'D':
                    self.drawer.pen_down()
                if self.command == 'U':
                    self.drawer.pen_up()
                if self.command == 'N':
                    drawer = DrawLinerToNorth(self.drawer, self.data)
                    drawer.draw_line()
                if self.command == 'E':
                    drawer = DrawLinerToEast(self.drawer, self.data)
                    drawer.draw_line()
                if self.command == 'S':
                    drawer = DrawLinerToSouth(self.drawer, self.data)
                    drawer.draw_line()
                if self.command == 'W':
                    drawer = DrawLinerToWest(self.drawer, self.data)
                    drawer.draw_line()
                if self.command == 'X':
                    self.drawer.go_along(self.data)
                if self.command == 'Y':
                    self.drawer.go_down(self.data)
                if self.command == 'U':
                    self.drawer.pen_up()
                if self.command == 'C':
                    self.drawer.draw_circle(self.data)
                if self.command == 'R':
                    self.drawer.draw_rectangle(self.data)
                if self.command == 'T':
                    self.drawer.draw_triangle(self.data)
            except:
                print(f"The Command {self.command}: {self.data} could not run")
        try:
            self.drawer.end()
        except:
            print("Completed")
