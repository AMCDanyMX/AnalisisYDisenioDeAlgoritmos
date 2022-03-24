import math

numero = int(input())
redondeado = round(numero)

redondeado_abajo = math.floor(numero)
redondeado_arriba = math.ceil(numero)
print("Redondeado con round: {}".format(redondeado))
print("Redondeado con floor (hacia abajo): {}".format(redondeado_abajo))
print("Redondeado con ceil (hacia arriba): {}".format(redondeado_arriba))
