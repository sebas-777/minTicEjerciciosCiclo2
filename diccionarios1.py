# funcion para calcular los promedios de 4 notas

def promediosNotas(nota1,nota2,nota3,nota4):
    promedios = round( (nota1 + nota2 + nota3 + nota4) /4, 2)
    return promedios

notas = "las notas de juanito son:{}".format(3.0,4.5,2.6,1.0)
print(promediosNotas(notas)  )