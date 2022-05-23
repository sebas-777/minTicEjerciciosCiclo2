def promedio(nota1:float,nota2:float,nota3:float):
    calificacion =(nota1 +nota2 +nota3) / 3
    print(f"el promedio de las notas es {calificacion}")
    
nota1 = float(input("Digite la nota numero 1 : "))  
nota2 = float(input("Digite la nota numero 2 : ")) 
nota3 = float(input("Digite la nota numero 3 : ")) 

promedio(nota1, nota2, nota3)