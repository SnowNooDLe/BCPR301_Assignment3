import sys
from abc import ABCMeta, abstractmethod
from Reader import *
from Parser import *
from TKDrawer import *
from TXTDrawer import *
from TDrawer import *
from TKCmd import *
from PyGameDrawer import *
from TIGr import AbstractDrawer, AbstractParser, AbstractSourceReader


class Company(metaclass=ABCMeta):
    @abstractmethod
    def build_product(self, para):
        raise NotImplementedError

    def get_product_info(self, para):
        product = self.build_product(para)
        return product.do_use() if product is not None else None


class CompanyA(Company):
    def build_product(self, para):
        # if para == "Most popular one":
        #     return ProductA()
        # if para == "Most expensive one":
        #     return ProductB()
        # return None
        products = {"-TKCMD": CommandDrawer(),
                    "-TK": TKInterDrawer(),
                    "-T": TurtleDrawer(),
                    "-TXT": TextDrawer(),
                    "-P": PGDrawer()}
        try:
            return products[para]
        except KeyError:
            print("cannot create Product: " + para)
            return None
        except:
            print("Something is really going wrong!")
            raise


class Product(metaclass=ABCMeta):
    @abstractmethod
    def do_use(self):
        raise NotImplementedError


class CommandDrawer(Product):
    def do_use(self):
        return TKInterShell().cmdloop()


class TKInterDrawer(Product):
    def do_use(self):
        return Reader(Parser(TKDrawer()))


class TurtleDrawer(Product):
    def do_use(self):
        return Reader(Parser(TDrawer()))


class TextDrawer(Product):
    def do_use(self):
        return Reader(Parser(TXTDrawer()))


class PGDrawer(Product):
    def do_use(self):
        return Reader(Parser(PyGameDrawer()))


class Main():
    def main(self):
        outputs = []
        a_compay = CompanyA()
        if len(sys.argv) == 1:
            print(
                "You need to specify a CMD loop to enter, -TKCMD or "
                "you can specify a TEXT file and declare outputs with "
                "-TK for TKinter, -T for Turtle or -TXT for txt ouput..."
                "GOOD LUCK!")
        else:
            for arg in sys.argv:
                if arg in ['-TKCMD', '-TK', '-T', '-TXT', '-P']:
                    outputs.append(a_compay.get_product_info(arg))

            if len(outputs) == 0:
                outputs.append(a_compay.get_product_info("-TXT"))

            for output in outputs:
                output.go()
            sys.exit()


if __name__ == '__main__':
    main = Main()
    main.main()
