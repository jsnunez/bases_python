datos=[]
x=int(input("Cuantos datos ingresara?"))
for i in range(x):
    datos.append(float(input(f"Dato {i+1}: ")))

print(datos)
prom=sum(datos)/x
print(prom)
mayores=[name for name in datos if datos>prom]