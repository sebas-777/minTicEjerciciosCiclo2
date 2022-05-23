from modulefinder import LOAD_CONST


def triangulo(base:float,lado:float,altura:float):
    perimetro = ( lado**3)
    area = (base*altura)/2
    return"El permietro del triangulo es {}, el area de trinagulo es {}".format(perimetro, area)  

base = float  ( input ( "Digite el la base : ") )
lado = float ( input ( "Digite el lado : ") )
altura = float ( input ( "Digite la  altura : ") )

print(triangulo(base, lado, altura))