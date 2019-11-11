from TIGr import AbstractDrawer


class TXTDrawer(AbstractDrawer):  
    def select_pen(self, pen_num):
        print(f'Pen: {pen_num}')

    def pen_down(self):
        print('Pen is Down')

    def pen_up(self):
        print('Pen is Up')

    def go_along(self, along):
        print(f'X:{along}')

    def go_down(self, down):
        print(f'Y:{down}')

    def draw_line(self, direction, distance):
        print(f'Drawing line of length {distance} at {direction} degrees')

    def draw_circle(self, size):
        print(f'Drawing circle of size {size}')

    def draw_rectangle(self, size):  # J
        print(f'Drawing rectangle of size {size}')

    def draw_triangle(self, size):  # M
        print(f'Drawing triangle of size {size}')

    def end(self):
        print('TXTReader is sleeping now')
