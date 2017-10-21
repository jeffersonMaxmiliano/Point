from model import *

def main (args=[]):

    def __add__():
        p1 = Point(2, 2)
        p2 = Point(3, 4)
        return ("Novo ponto x: "+str(p1.x + p2.x) +" Novo ponto x: " +str(p1.y + p2.y))

    def __str__():
        resultado = str(__add__())
        return resultado
    a=__str__()
    return a
if __name__ == '__main__':
     print(main())