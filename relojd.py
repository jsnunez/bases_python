import math
t=float(input("Hora actual:"))
h=float(input("Cantidad de horas:"))
r=math.fmod(h,12)
ha=t+r 
print(r)
print(f"En {h} horas, el reloj marcara las {ha}")
##fdsfsad