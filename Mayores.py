datos=[]
cont=0
x=int(input("Cuantos datos ingresara?"))
for i in range(x):
    datos.append(float(input(f"Dato {i+1}: ")))

prom=sum(datos)/x

for i in datos:
    if i>prom :
        cont=cont+1
print(f"{cont} Datos son mayores que el promediocont")