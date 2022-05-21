# extraer una letra

fresa = "fruta"
letra = fresa[1]

print(letra)

# extraer la longitud de una cadena utilizando len

fruta = 'banana'
longitud = len(fruta)
print(longitud)

# extraer lo ultimo caracter de una cadena
ultimo = fruta[longitud - 1] 

print(ultimo)

# rebandas de string

s = 'montly phyton'

print(s[0:6])


print(s[3:])

print(s[:3])

fruta = "banana"

print(fruta[3:3])

saludo = 'hola mundo'
nuevo_saludo = 'j' + saludo[:1]
print(nuevo_saludo) 

# el operador in

var1 = 'a' 

var2 = 'banana'

print(var1 in var2)

var1 = 'ola'
var2 = 'orange'
print(var1 in var2)

# compador de string

palabra = "banana"

if palabra == "banana":
    print("las bananas son geniales")
