import sys
from Reader import *
from Parser import *
from TKDrawer import *
from TXTDrawer import *
from TDrawer import *
from TKCmd import *
from PyGameDrawer import *
from TIGr import AbstractDrawer, AbstractParser, AbstractSourceReader


def main():
    outputs = []
    if len(sys.argv) == 1:
        print(
            "You need to specify a CMD loop to enter, -TKCMD or you can specify a TEXT file and declare outputs with -TK for TKinter, -T for Turtle or -TXT for txt ouput...GOOD LUCK!")
    else:
        for arg in sys.argv:
            if arg == '-TKCMD':
                TKInterShell().cmdloop()
                sys.exit()
            if arg == '-TK':
                outputs.append(Reader(Parser(TKDrawer())))
            if arg == '-T':
                outputs.append(Reader(Parser(TDrawer())))
            if arg == '-TXT':
                outputs.append(Reader(Parser(TXTDrawer())))
            if arg == '-P':
                outputs.append(Reader(Parser(PyGameDrawer())))
        if len(outputs) == 0:
            outputs.append(Reader(Parser(TXTDrawer())))
        for output in outputs:
            output.go()
        sys.exit()


if __name__ == '__main__':
    main()
