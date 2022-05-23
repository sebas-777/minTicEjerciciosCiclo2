# 1. Diseñar un algoritmo que lea el peso de una persona en libras y devuelva su peso en kilogramo.

# Ingrese por favor  el peso en libras

# 1 libra equivale a 0.453592 kilogramos
# Divide la cantidad de libras entre 2,2046 si quieres usar la ecuación estándar.

print( "Por favor Ingrese su peso en Libras: ")
libras = float( input(  ))

pesoPersona = libras/2.2046 

print( "el peso  en kilogramos es: {}".format(pesoPersona))

