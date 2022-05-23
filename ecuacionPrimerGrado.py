# Realice un programa para hallar la X en la siguimente ecuacion de primer  10 + X = 24 

# Se debe ingresar el primer valor y el ultimo 
# Nos debe retornar la ecuacion solucionada

def ecuacion(num1:int,num2:int):
    
    x = num2 - num1
    
    print (f"la solucion a la ecuacion de primer grado {num1} + x = {num2}, por lo tanto X es =  {x}")
    

num1 = int( input(" ingrese el primer numero: "))
num2 = int( input(" ingrese el segundo numero: "))

ecuacion(num1,num2)