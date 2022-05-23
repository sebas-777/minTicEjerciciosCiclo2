def velocidad(tiempo:int, distancia:int):

    vel = distancia / tiempo
    return "la velocidades : {} metros/sgs".format(vel)


tiempo =  int( input(" Digite el tiempo en segundos: "))

distancia = int( input(" Digite el distancia en metros: "))

print(velocidad(tiempo,distancia))