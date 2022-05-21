# Ciclo 1 Fundamentos de programación
# Reto 2:
# En el parque de diversiones “AVENTURAS EXTREMAS” se requiere implementar una función en la
# cual reciba como parámetro un diccionario, el cual va a tener las variables que a continuación se
# muestran:
# Nombre Tipo Descripción
# id_cliente int Código único que identifica al cliente
# nombre str Nombre del cliente
# edad int Edad cliente
# primer_ingreso boolean Primera vez que el cliente ingresa puede ser:
# True/False
# En la siguiente tabla se muestra la atracción y el valor de la boleta para cada una de ellas, en la cual
# los clientes podrán ingresar dependiendo de su edad, posteriormente el parque de atracciones ha
# decidido otorgar un descuento al valor de la boleta si cumple con el rango de edad y es la primera
# vez que el cliente ingresa.
# Atracción Valor de boleta Edad
# (años) Primer Ingreso Descuento
# X-Treme 20000 >18 años True 5% del valor de la boleta
# Carros
# chocones 5000 >=15 y
# <=18 True 7% del valor de la boleta
# Sillas
# voladoras 10000 >=7 y < 15 True 5% del valor de la boleta
# Esta función debe retornar un nuevo diccionario con las llaves nombre, edad, atracción,
# primer_ingreso, total_boleta y apto del cliente:
# • En donde apto tendrá como valor una variable booleana, será verdadera si su edad cumple con
# los rangos exigidos en la tabla anterior, en el caso contrario será falsa.
# • En el caso de atraccion y total_boleta, si no se cumple el rango de edades se le asignara un valor
# de ‘N/A’ a cada uno.
# • Si primer_ingreso es verdadero, el total_boleta será el valor de la boleta menos el descuento de
# lo contrario se pagará el valor neto de la boleta.
# Ejemplo:
# Id_cliente nombre edad primer_ingreso return
# 1
# Johana
# Fernandez 20 True {'nombre': 'Johana Fernandez', 'edad': 20, 'atraccion': 'X-Treme','apto':
# True, 'primer_ingreso': True, 'total_boleta': 19000.0}
# 1
# Johana
# Fernandez 20 False {'nombre': 'Johana Fernandez', 'edad': 20, 'atraccion': 'X-Treme','apto':
# True, 'primer_ingreso': False, 'total_boleta': 20000}
# 2
# Gloria
# Suarez 3 True {'nombre': 'Gloria Suarez', 'edad': 3, 'atraccion': 'N/A', 'apto':
# False,'primer_ingreso': True, 'total_boleta': 'N/A'}
# 3
# Tatiana
# Suarez 17 True {'nombre': 'Tatiana Suarez', 'edad': 17, 'atraccion': 'Carroschocones',
# 'apto': True, 'primer_ingreso': True, 'total_boleta':4650.0}
# 3
# Tatiana
# Suarez 17 False {'nombre': 'Tatiana Suarez', 'edad': 17, 'atraccion': 'Carroschocones',
# 'apto': True, 'primer_ingreso': False, 'total_boleta': 5000}
# 4
# Tatiana
# Ruiz 8 True {'nombre': 'Tatiana Ruiz', 'edad': 8, 'atraccion': 'Sillas voladoras','apto':
# True, 'primer_ingreso': True, 'total_boleta': 9500.0}
# 4
# Tatiana
# Ruiz 8 False {'nombre': 'Tatiana Ruiz', 'edad': 8, 'atraccion': 'Sillas voladoras','apto':
# True, 'primer_ingreso': False, 'total_boleta': 10000}

def cliente(informacion:dict)-> dict:   
    if informacion["edad"] >18:
        if informacion["primer_ingreso"] ==True:
            return {
                    'nombre': informacion["nombre"], 
                    'edad': informacion["edad"], 
                    'atraccion': 'X-Treme',
                    'apto':True, 
                    'primer_ingreso': True, 
                    'total_boleta': 19000.0
                 }
        else:
            return{
                    'nombre': informacion["nombre"], 
                    'edad': informacion["edad"], 
                    'atraccion': 'X-Treme',
                    'apto':True, 
                    'primer_ingreso': False, 
                    'total_boleta': 20000
                }
    elif informacion["edad"] >=15 and informacion["edad"] <= 18:
        if informacion["primer_ingreso"] == True:
            return{
                    'nombre': informacion["nombre"], 
                    'edad': informacion["edad"], 
                    'atraccion': 'Carros chocones', 
                    'apto': True, 
                    'primer_ingreso': True, 
                    'total_boleta':4650.0
                }
        else:
            return{
                'nombre': informacion['nombre'],
                 'edad': informacion['edad'], 
                'atraccion': 'Carros chocones', 
                'apto': True, 
                'primer_ingreso': False, 
                'total_boleta': 5000
               
               
                }
    elif informacion["edad"] >=7 and informacion["edad"] < 15:
        if informacion["primer_ingreso"] == True:
            return{
                    'nombre': informacion["nombre"], 
                    'edad': informacion["edad"], 
                    'atraccion': 'Sillas voladoras', 
                    'apto': True, 
                    'primer_ingreso': True, 
                    'total_boleta':9500.0
                }
        else:
            return{
                'nombre': informacion['nombre'],
                 'edad': informacion['edad'], 
                'atraccion': 'Sillas voladoras', 
                'apto': True, 
                'primer_ingreso': False, 
                'total_boleta': 10000
               
               
                } 
    else:
        return{
            'nombre': informacion['nombre'],
            'edad': informacion['edad'], 
            'atraccion': 'N/A', 
            'apto': False, 
            'primer_ingreso':  informacion['primer_ingreso'], 
            'total_boleta': 'N/A' 
               
               
             } 
        
            
informacion = {
    
    "Id_cliente":1,
    "nombre":"Johana Fernandez",
    "edad":15,
    "primer_ingreso":False,
    
}

print(cliente(informacion))